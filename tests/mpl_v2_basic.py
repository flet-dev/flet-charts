from io import BytesIO
import logging
import flet as ft
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import flet_charts

matplotlib.use("module://flet_charts.matplotlib_backends.backend_flet_agg")

logging.basicConfig(level=logging.DEBUG)

def main(page: ft.Page):
    # Sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot
    fig = plt.figure()
    print("Figure number:", fig.number)
    plt.plot(x, y)
    plt.title("Interactive Sine Wave")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.grid(True)

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
            pan_btn := ft.IconButton(ft.Icons.PAN_TOOL_OUTLINED, selected_icon=ft.Icons.PAN_TOOL_OUTLINED, selected_icon_color=ft.Colors.AMBER_800, on_click=pan_click),
            zoom_btn := ft.IconButton(ft.Icons.ZOOM_IN, selected_icon=ft.Icons.ZOOM_IN, selected_icon_color=ft.Colors.AMBER_800, on_click=zoom_click),
            ft.IconButton(ft.Icons.DOWNLOAD, on_click=download_click),
            dwnld_fmt := ft.Dropdown(value="png", options=[ft.DropdownOption(fmt) for fmt in download_formats]),
            msg
        ]),
        mpl,
    )


ft.run(main)
