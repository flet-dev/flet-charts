from io import BytesIO
import logging
import flet as ft
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet_charts

matplotlib.use("module://flet_charts.matplotlib_backends.backend_flet_agg")

#logging.basicConfig(level=logging.DEBUG)

state = {}

def main(page: ft.Page):

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    X = np.random.rand(100, 200)
    xs = np.mean(X, axis=1)
    ys = np.std(X, axis=1)

    fig, (ax, ax2) = plt.subplots(2, 1)
    ax.set_title('click on point to plot time series')
    line, = ax.plot(xs, ys, 'o', picker=True, pickradius=5)

    class PointBrowser:
        """
        Click on a point to select and highlight it -- the data that
        generated the point will be shown in the lower Axes.  Use the 'n'
        and 'p' keys to browse through the next and previous points
        """

        def __init__(self):
            self.lastind = 0

            self.text = ax.text(0.05, 0.95, 'selected: none',
                                transform=ax.transAxes, va='top')
            self.selected, = ax.plot([xs[0]], [ys[0]], 'o', ms=12, alpha=0.4,
                                    color='yellow', visible=False)

        def on_press(self, event):
            if self.lastind is None:
                return
            if event.key not in ('n', 'p'):
                return
            if event.key == 'n':
                inc = 1
            else:
                inc = -1

            self.lastind += inc
            self.lastind = np.clip(self.lastind, 0, len(xs) - 1)
            self.update()

        def on_pick(self, event):

            print("ON PICK")

            if event.artist != line:
                return True

            N = len(event.ind)
            if not N:
                return True

            # the click locations
            x = event.mouseevent.xdata
            y = event.mouseevent.ydata

            distances = np.hypot(x - xs[event.ind], y - ys[event.ind])
            indmin = distances.argmin()
            dataind = event.ind[indmin]

            self.lastind = dataind
            self.update()

        def update(self):
            if self.lastind is None:
                return

            dataind = self.lastind

            ax2.clear()
            ax2.plot(X[dataind])

            ax2.text(0.05, 0.9, f'mu={xs[dataind]:1.3f}\nsigma={ys[dataind]:1.3f}',
                    transform=ax2.transAxes, va='top')
            ax2.set_ylim(-0.5, 1.5)
            self.selected.set_visible(True)
            self.selected.set_data([xs[dataind]], [ys[dataind]])

            self.text.set_text('selected: %d' % dataind)
            fig.canvas.draw()

    browser = PointBrowser()
    state["browser"] = browser

    fig.canvas.mpl_connect('pick_event', browser.on_pick)
    fig.canvas.mpl_connect('key_press_event', browser.on_press)

    plt.show()

    download_formats = [
        "eps",
        "jpeg",
        "pgf",
        "pdf",
        "png",
        "ps",
        "raw",
        "svg",
        "tif",
        "webp"
    ]

    fp = ft.FilePicker()
    page.services.append(fp)

    msg = ft.Text()
    def on_message(e: flet_charts.MatplotlibChartMessageEvent):
        msg.value = e.message

    def on_toolbar_update(e: flet_charts.MatplotlibChartToolbarButtonsUpdateEvent):
        back_btn.disabled = not e.back_enabled
        fwd_btn.disabled = not e.forward_enabled

    def pan_click():
        mpl.pan()
        pan_btn.selected = not pan_btn.selected
        zoom_btn.selected = False

    def zoom_click():
        mpl.zoom()
        pan_btn.selected = False
        zoom_btn.selected = not zoom_btn.selected

    async def download_click():
        fmt = dwnld_fmt.value
        buffer = mpl.download(fmt)
        title = fig.canvas.manager.get_window_title()
        await fp.save_file_async(file_name=f"{title}.{fmt}", src_bytes=buffer)

    mpl = flet_charts.MatplotlibChart(figure=fig, expand=True, on_message=on_message, on_toolbar_buttons_update=on_toolbar_update)

    # fig1.canvas.start()
    page.add(
        ft.Row([
            ft.IconButton(ft.Icons.HOME, on_click=lambda: mpl.home()),
            back_btn := ft.IconButton(ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda: mpl.back()),
            fwd_btn := ft.IconButton(ft.Icons.ARROW_FORWARD_ROUNDED, on_click=lambda: mpl.forward()),
            pan_btn := ft.IconButton(ft.Icons.OPEN_WITH, selected_icon=ft.Icons.OPEN_WITH, selected_icon_color=ft.Colors.AMBER_800, on_click=pan_click),
            zoom_btn := ft.IconButton(ft.Icons.SEARCH, selected_icon=ft.Icons.SEARCH, selected_icon_color=ft.Colors.AMBER_800, on_click=zoom_click),
            ft.IconButton(ft.Icons.DOWNLOAD, on_click=download_click),
            dwnld_fmt := ft.Dropdown(value="png", options=[ft.DropdownOption(fmt) for fmt in download_formats]),
            msg
        ]),
        mpl,
    )


ft.run(main)
