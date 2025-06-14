import flet as ft

import flet_charts as fch


def main(page: ft.Page):
    normal_border = ft.BorderSide(0, ft.Colors.with_opacity(0, ft.Colors.WHITE))
    hovered_border = ft.BorderSide(6, ft.Colors.WHITE)

    def on_chart_event(e: fch.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            section.border_side = (
                hovered_border if idx == e.section_index else normal_border
            )
        chart.update()

    chart = fch.PieChart(
        sections=[
            fch.PieChartSection(
                25,
                color=ft.Colors.BLUE,
                radius=80,
                border_side=normal_border,
            ),
            fch.PieChartSection(
                25,
                color=ft.Colors.YELLOW,
                radius=65,
                border_side=normal_border,
            ),
            fch.PieChartSection(
                25,
                color=ft.Colors.PINK,
                radius=60,
                border_side=normal_border,
            ),
            fch.PieChartSection(
                25,
                color=ft.Colors.GREEN,
                radius=70,
                border_side=normal_border,
            ),
        ],
        sections_space=1,
        center_space_radius=0,
        on_chart_event=on_chart_event,
        expand=True,
    )

    page.add(chart)


ft.run(main)
