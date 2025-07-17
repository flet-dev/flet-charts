import flet as ft
import matplotlib
import matplotlib.pyplot as plt

import flet_charts

matplotlib.use("module://flet_charts.matplotlib_backends.backend_flet_agg")


def main(page: ft.Page):
    # Create first figure
    fig1, ax1 = plt.subplots()
    ax1.plot([0, 1], [0, 1], label="Line 1")
    ax1.text(0.5, 0.5, "Hello Flutter 1", fontsize=12)
    ax1.legend()

    mpl = flet_charts.MatplotlibChart(figure=fig1, expand=True)

    # fig1.canvas.start()
    page.add(
        ft.Row([
            ft.Button("Home", on_click=lambda: mpl.home()),
            ft.Button("Back", on_click=lambda: mpl.back()),
            ft.Button("Forward", on_click=lambda: mpl.forward()),
            ft.Button("Pan", on_click=lambda: mpl.pan()),
            ft.Button("Zoom", on_click=lambda: mpl.zoom())
        ]),
        mpl,
    )


ft.run(main)
