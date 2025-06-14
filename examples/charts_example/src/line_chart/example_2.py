import flet as ft

import flet_charts as fch


class State:
    toggle = True


s = State()


def main(page: ft.Page):
    data_1 = [
        fch.LineChartData(
            data_points=[
                fch.LineChartDataPoint(0, 3),
                fch.LineChartDataPoint(2.6, 2),
                fch.LineChartDataPoint(4.9, 5),
                fch.LineChartDataPoint(6.8, 3.1),
                fch.LineChartDataPoint(8, 4),
                fch.LineChartDataPoint(9.5, 3),
                fch.LineChartDataPoint(11, 4),
            ],
            stroke_width=5,
            color=ft.Colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    data_2 = [
        fch.LineChartData(
            data_points=[
                fch.LineChartDataPoint(0, 3.44),
                fch.LineChartDataPoint(2.6, 3.44),
                fch.LineChartDataPoint(4.9, 3.44),
                fch.LineChartDataPoint(6.8, 3.44),
                fch.LineChartDataPoint(8, 3.44),
                fch.LineChartDataPoint(9.5, 3.44),
                fch.LineChartDataPoint(11, 3.44),
            ],
            stroke_width=5,
            color=ft.Colors.CYAN,
            curved=True,
            stroke_cap_round=True,
        )
    ]

    chart = fch.LineChart(
        data_series=data_1,
        border=ft.border.all(3, ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE)),
        horizontal_grid_lines=fch.ChartGridLines(
            interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE), width=1
        ),
        vertical_grid_lines=fch.ChartGridLines(
            interval=1, color=ft.Colors.with_opacity(0.2, ft.Colors.ON_SURFACE), width=1
        ),
        left_axis=fch.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=1,
                    label=ft.Text("10K", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=3,
                    label=ft.Text("30K", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Text("50K", size=14, weight=ft.FontWeight.BOLD),
                ),
            ],
            labels_size=40,
        ),
        bottom_axis=fch.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=2,
                    label=ft.Container(
                        ft.Text(
                            "MAR",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Container(
                        ft.Text(
                            "JUN",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=8,
                    label=ft.Container(
                        ft.Text(
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
            ],
            labels_size=32,
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY),
        min_y=0,
        max_y=6,
        min_x=0,
        max_x=11,
        # animate=5000,
        expand=True,
    )

    def toggle_data(e):
        if s.toggle:
            chart.data_series = data_2
            chart.interactive = False
        else:
            chart.data_series = data_1
            chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

    page.add(ft.ElevatedButton("avg", on_click=toggle_data), chart)


ft.run(main)
