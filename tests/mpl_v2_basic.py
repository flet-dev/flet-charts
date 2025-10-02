import logging

import flet as ft
import matplotlib.pyplot as plt
import numpy as np

import flet_charts

logging.basicConfig(level=logging.INFO)


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

    page.add(flet_charts.MatplotlibChartWithToolbar(figure=fig, expand=True))


ft.run(main)
