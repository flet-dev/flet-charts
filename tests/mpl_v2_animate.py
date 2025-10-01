import logging

import flet as ft
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import flet_charts

matplotlib.use("module://flet_charts.matplotlib_backends.backend_flet_agg")

logging.basicConfig(level=logging.INFO)

state = {}


def main(page: ft.Page):
    import matplotlib.animation as animation

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    def random_walk(num_steps, max_step=0.05):
        """Return a 3D random walk as (num_steps, 3) array."""
        start_pos = np.random.random(3)
        steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
        walk = start_pos + np.cumsum(steps, axis=0)
        return walk

    def update_lines(num, walks, lines):
        for line, walk in zip(lines, walks):
            line.set_data_3d(walk[:num, :].T)
        return lines

    # Data: 40 random walks as (num_steps, 3) arrays
    num_steps = 30
    walks = [random_walk(num_steps) for index in range(40)]

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")

    # Create lines initially without data
    lines = [ax.plot([], [], [])[0] for _ in walks]

    # Setting the Axes properties
    ax.set(xlim3d=(0, 1), xlabel="X")
    ax.set(ylim3d=(0, 1), ylabel="Y")
    ax.set(zlim3d=(0, 1), zlabel="Z")

    # Creating the Animation object
    state["anim"] = animation.FuncAnimation(
        fig, update_lines, num_steps, fargs=(walks, lines), interval=100
    )

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
        "webp",
    ]

    fp = ft.FilePicker()

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
        await fp.save_file(file_name=f"{title}.{fmt}", src_bytes=buffer)

    mpl = flet_charts.MatplotlibChart(
        figure=fig,
        expand=True,
        on_message=on_message,
        on_toolbar_buttons_update=on_toolbar_update,
    )

    # fig1.canvas.start()
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.HOME, on_click=lambda: mpl.home()),
                back_btn := ft.IconButton(
                    ft.Icons.ARROW_BACK_ROUNDED, on_click=lambda: mpl.back()
                ),
                fwd_btn := ft.IconButton(
                    ft.Icons.ARROW_FORWARD_ROUNDED, on_click=lambda: mpl.forward()
                ),
                pan_btn := ft.IconButton(
                    ft.Icons.PAN_TOOL_OUTLINED,
                    selected_icon=ft.Icons.PAN_TOOL_OUTLINED,
                    selected_icon_color=ft.Colors.AMBER_800,
                    on_click=pan_click,
                ),
                zoom_btn := ft.IconButton(
                    ft.Icons.ZOOM_IN,
                    selected_icon=ft.Icons.ZOOM_IN,
                    selected_icon_color=ft.Colors.AMBER_800,
                    on_click=zoom_click,
                ),
                ft.IconButton(ft.Icons.DOWNLOAD, on_click=download_click),
                dwnld_fmt := ft.Dropdown(
                    value="png",
                    options=[ft.DropdownOption(fmt) for fmt in download_formats],
                ),
                msg,
            ]
        ),
        mpl,
    )


ft.run(main)
