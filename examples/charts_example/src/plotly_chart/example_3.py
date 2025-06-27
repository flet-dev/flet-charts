import flet as ft
import plotly.graph_objects as go

import flet_charts as fch


def main(page: ft.Page):

    labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    page.add(fch.PlotlyChart(figure=fig, expand=True))


ft.run(main)
