from dataclasses import dataclass, field
from typing import Any, Optional

import flet as ft

from .chart_axis import ChartAxis
from .line_chart_data import LineChartData
from .types import ChartEventType, ChartGridLines

__all__ = [
    "LineChart",
    "LineChartEvent",
    "LineChartEventSpot",
    "LineChartTooltip",
]


@dataclass
class LineChartEventSpot:
    bar_index: int
    """
    The line's index or `-1` if no line was hovered.
    """

    spot_index: int
    """
    The line's point index or `-1` if no point was hovered.
    """


@dataclass
class LineChartEvent(ft.Event[ft.EventControlType]):
    type: ChartEventType
    """
    The type of event that occured.
    """

    spots: list[LineChartEventSpot]
    """
    Spots on which the event occurred.
    """


@dataclass
class LineChartTooltip:
    """Configuration of the tooltip for [`LineChart`][(p).]s."""

    bgcolor: ft.ColorValue = "#FF607D8B"
    """
    Background [color](https://flet.dev/docs/reference/colors) of tooltip.
    """

    border_radius: Optional[ft.BorderRadiusValue] = None
    """
    The tooltip's border radius.
    """

    margin: ft.Number = 16
    """
    Applies a bottom margin for showing tooltip on top of rods.
    """

    padding: ft.PaddingValue = field(
        default_factory=lambda: ft.Padding.symmetric(vertical=8, horizontal=16)
    )
    """
    Applies a padding for showing contents inside the tooltip.

    Value is of type [`PaddingValue`](https://flet.dev/docs/reference/types/aliases#paddingvalue).
    """

    max_width: ft.Number = 120
    """
    Restricts the tooltip's width.
    """

    rotate_angle: ft.Number = 0.0
    """
    The tooltip's rotation angle in degrees.
    """

    horizontal_offset: ft.Number = 0.0
    """
    Applies horizontal offset for showing tooltip.
    """

    border_side: ft.BorderSide = field(default_factory=lambda: ft.BorderSide.none())
    """
    The tooltip's border side.
    """

    fit_inside_horizontally: bool = False
    """
    Forces the tooltip to shift horizontally inside the chart, if overflow happens.
    """

    fit_inside_vertically: bool = False
    """
    Forces the tooltip to shift vertically inside the chart, if overflow happens.
    """

    show_on_top_of_chart_box_area: bool = False
    """
    Whether to force the tooltip container to top of the line.
    """


@ft.control("LineChart")
class LineChart(ft.ConstrainedControl):
    """
    Draws a line chart.

    ![Overview](assets/line-chart/diagram.svg)
    """

    data_series: list[LineChartData] = field(default_factory=list)
    """
    A list of [`LineChartData`][(p).]
    controls drawn as separate lines on a chart.
    """

    animation: ft.AnimationValue = field(
        default_factory=lambda: ft.Animation(
            duration=ft.Duration(milliseconds=150), curve=ft.AnimationCurve.LINEAR
        )
    )
    """
    Controls chart implicit animation.

    Value is of type [`AnimationValue`](https://flet.dev/docs/reference/types/animationvalue).
    """

    interactive: bool = True
    """
    Enables automatic tooltips and points highlighting when hovering over the chart.
    """

    point_line_start: Optional[ft.Number] = None
    """
    The start of the vertical line drawn under the selected point.

    Defaults to chart's bottom edge.
    """

    point_line_end: Optional[ft.Number] = None
    """
    The end of the vertical line drawn at selected point position.

    Defaults to data point's `y` value.
    """

    bgcolor: Optional[ft.ColorValue] = None
    """
    Background [color](https://flet.dev/docs/reference/colors) of the chart.
    """

    border: Optional[ft.Border] = None
    """
    The border around the chart.

    Value is of type [`Border`](https://flet.dev/docs/reference/types/border).
    """

    horizontal_grid_lines: Optional[ChartGridLines] = None
    """
    Controls drawing of chart's horizontal lines.

    Value is of type [`ChartGridLines`][(p).].
    """

    vertical_grid_lines: Optional[ChartGridLines] = None
    """
    Controls drawing of chart's vertical lines.

    Value is of type [`ChartGridLines`][(p).].
    """

    left_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=44))
    """
    Defines the appearance of the left axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    top_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=30))
    """
    Defines the appearance of the top axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    right_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=44))
    """
    Defines the appearance of the right axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    bottom_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=30))
    """
    Defines the appearance of the bottom axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    baseline_x: Optional[ft.Number] = None
    """
    Baseline value for X axis.
    """

    min_x: Optional[ft.Number] = None
    """
    Defines the minimum displayed value for X axis.
    """

    max_x: Optional[ft.Number] = None
    """
    Defines the maximum displayed value for X axis.
    """

    baseline_y: Optional[ft.Number] = None
    """
    Baseline value for Y axis.
    """

    min_y: Optional[ft.Number] = None
    """
    Defines the minimum displayed value for Y axis.
    """

    max_y: Optional[ft.Number] = None
    """
    Defines the maximum displayed value for Y axis.
    """

    tooltip: LineChartTooltip = field(default_factory=lambda: LineChartTooltip())
    """
    The tooltip configuration for this chart.
    """

    on_event: ft.OptionalEventHandler[LineChartEvent["LineChart"]] = None
    """
    Fires when a chart line is hovered or clicked.

    Value is of type [`LineChartEvent`][(p).].
    """

    def __post_init__(self, ref: Optional[ft.Ref[Any]]):
        super().__post_init__(ref)
        self._internals["skip_properties"] = ["tooltip"]
        self._internals["skip_inherited_notifier"] = True
