import flet as ft

import flet_charts as fch


class State:
    toggle = True


s = State()


def main(page: ft.Page):
    data_1 = [
        fch.LineChartData(
            stroke_width=8,
            color=ft.Colors.LIGHT_GREEN,
            curved=True,
            stroke_cap_round=True,
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 1.5),
                ft.LineChartDataPoint(5, 1.4),
                ft.LineChartDataPoint(7, 3.4),
                ft.LineChartDataPoint(10, 2),
                ft.LineChartDataPoint(12, 2.2),
                ft.LineChartDataPoint(13, 1.8),
            ],
        ),
        fch.LineChartData(
            color=ft.Colors.PINK,
            below_line_bgcolor=ft.Colors.with_opacity(0, ft.Colors.PINK),
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
            data_points=[
                fch.LineChartDataPoint(1, 1),
                fch.LineChartDataPoint(3, 2.8),
                fch.LineChartDataPoint(7, 1.2),
                fch.LineChartDataPoint(10, 2.8),
                fch.LineChartDataPoint(12, 2.6),
                fch.LineChartDataPoint(13, 3.9),
            ],
        ),
        fch.LineChartData(
            color=ft.Colors.CYAN,
            stroke_width=8,
            curved=True,
            stroke_cap_round=True,
            data_points=[
                fch.LineChartDataPoint(1, 2.8),
                fch.LineChartDataPoint(3, 1.9),
                fch.LineChartDataPoint(6, 3),
                fch.LineChartDataPoint(10, 1.3),
                fch.LineChartDataPoint(13, 2.5),
            ],
        ),
    ]

    data_2 = [
        fch.LineChartData(
            stroke_width=4,
            color=ft.Colors.with_opacity(0.5, ft.Colors.LIGHT_GREEN),
            stroke_cap_round=True,
            data_points=[
                fch.LineChartDataPoint(1, 1),
                fch.LineChartDataPoint(3, 4),
                fch.LineChartDataPoint(5, 1.8),
                fch.LineChartDataPoint(7, 5),
                fch.LineChartDataPoint(10, 2),
                fch.LineChartDataPoint(12, 2.2),
                fch.LineChartDataPoint(13, 1.8),
            ],
        ),
        fch.LineChartData(
            color=ft.Colors.with_opacity(0.5, ft.Colors.PINK),
            below_line_bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.PINK),
            stroke_width=4,
            curved=True,
            stroke_cap_round=True,
            data_points=[
                ft.LineChartDataPoint(1, 1),
                ft.LineChartDataPoint(3, 2.8),
                ft.LineChartDataPoint(7, 1.2),
                ft.LineChartDataPoint(10, 2.8),
                ft.LineChartDataPoint(12, 2.6),
                ft.LineChartDataPoint(13, 3.9),
            ],
        ),
        fch.LineChartData(
            color=ft.Colors.with_opacity(0.5, ft.Colors.CYAN),
            stroke_width=4,
            stroke_cap_round=True,
            data_points=[
                fch.LineChartDataPoint(1, 3.8),
                fch.LineChartDataPoint(3, 1.9),
                fch.LineChartDataPoint(6, 5),
                fch.LineChartDataPoint(10, 3.3),
                fch.LineChartDataPoint(13, 4.5),
            ],
        ),
    ]

    chart = fch.LineChart(
        data_series=data_1,
        border=ft.Border(
            bottom=ft.BorderSide(4, ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE))
        ),
        tooltip_bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.BLUE_GREY),
        min_y=0,
        max_y=4,
        min_x=0,
        max_x=14,
        # animate=5000,
        expand=True,
        left_axis=ft.ChartAxis(
            labels=[
                fch.ChartAxisLabel(
                    value=1,
                    label=ft.Text("1m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=2,
                    label=ft.Text("2m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=3,
                    label=ft.Text("3m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=4,
                    label=ft.Text("4m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=5,
                    label=ft.Text("5m", size=14, weight=ft.FontWeight.BOLD),
                ),
                fch.ChartAxisLabel(
                    value=6,
                    label=ft.Text("6m", size=14, weight=ft.FontWeight.BOLD),
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
                            "SEP",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=7,
                    label=ft.Container(
                        ft.Text(
                            "OCT",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.with_opacity(0.5, ft.Colors.ON_SURFACE),
                        ),
                        margin=ft.margin.only(top=10),
                    ),
                ),
                fch.ChartAxisLabel(
                    value=12,
                    label=ft.Container(
                        ft.Text(
                            "DEC",
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
    )

    def toggle_data(e):
        if s.toggle:
            chart.data_series = data_2
            chart.data_series[2].point = True
            chart.max_y = 6
            chart.interactive = False
        else:
            chart.data_series = data_1
            chart.max_y = 4
            chart.interactive = True
        s.toggle = not s.toggle
        chart.update()

    page.add(ft.IconButton(ft.Icons.REFRESH, on_click=toggle_data), chart)


ft.run(main)
