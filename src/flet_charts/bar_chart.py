from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Optional

import flet as ft

from .bar_chart_group import BarChartGroup
from .chart_axis import ChartAxis
from .types import ChartEventType, ChartGridLines

__all__ = [
    "BarChart",
    "BarChartEvent",
    "BarChartTooltipDirection",
    "BarChartTooltip",
]


class BarChartTooltipDirection(Enum):
    """Controls showing tooltip on top or bottom."""

    AUTO = "auto"
    """Tooltip shows on top if value is positive, on bottom if value is negative."""

    TOP = "top"
    """Tooltip always shows on top."""

    BOTTOM = "bottom"
    """Tooltip always shows on bottom."""


@dataclass
class BarChartTooltip:
    """Configuration of the tooltip for [`BarChart`][(p).]s."""

    bgcolor: ft.ColorValue = ft.Colors.SECONDARY
    """
    Background [color](https://flet.dev/docs/reference/colors) of tooltips.
    """

    border_radius: Optional[ft.BorderRadiusValue] = None
    """
    The border radius of the tooltip.
    """

    margin: Optional[ft.Number] = None
    """
    Applies a bottom margin for showing tooltip on top of rods.
    """

    padding: Optional[ft.PaddingValue] = None
    """
    Applies a padding for showing contents inside the tooltip.
    """

    max_width: Optional[ft.Number] = None
    """
    Restricts the tooltip's width.
    """

    rotate_angle: Optional[ft.Number] = None
    """
    The rotation angle of the tooltip.
    """

    horizontal_offset: Optional[ft.Number] = None
    """
    Applies horizontal offset for showing tooltip.
    """

    border_side: Optional[ft.BorderSide] = None
    """
    The tooltip border side.
    """

    fit_inside_horizontally: Optional[bool] = None
    """
    Forces the tooltip to shift horizontally inside the chart, if overflow happens.

    Value is of type `bool`.
    """

    fit_inside_vertically: Optional[bool] = None
    """
    Forces the tooltip to shift vertically inside the chart, if overflow happens.

    Value is of type `bool`.
    """

    direction: Optional[BarChartTooltipDirection] = None
    """
    Controls showing tooltip on top or bottom, default is auto.
    """


@dataclass
class BarChartEvent(ft.Event["BarChart"]):
    type: ChartEventType
    """
    The type of event that occurred on the chart.
    """

    group_index: Optional[int] = None
    """
    Bar's index or `-1` if chart is hovered or clicked outside of any bar.
    """

    rod_index: Optional[int] = None
    """
    Rod's index or `-1` if chart is hovered or clicked outside of any bar.
    """

    stack_item_index: Optional[int] = None
    """
    Stack item's index or `-1` if chart is hovered or clicked outside of any bar.
    """


@ft.control("BarChart")
class BarChart(ft.ConstrainedControl):
    """
    Draws a bar chart.

    ![Overview](assets/bar-chart/diagram.svg)
    """

    groups: list[BarChartGroup] = field(default_factory=list)
    """
    The list of [`BarChartGroup`][(p).]s to draw.
    """

    spacing: Optional[ft.Number] = None
    """
    A amount of space between bar groups.
    """

    animation: ft.AnimationValue = field(
        default_factory=lambda: ft.Animation(
            duration=ft.Duration(milliseconds=150), curve=ft.AnimationCurve.LINEAR
        )
    )
    """
    Controls chart implicit animation.

    Value is of [`AnimationValue`](https://flet.dev/docs/reference/types/animationvalue)
    type.
    """

    interactive: bool = True
    """
    Enables automatic tooltips when hovering chart bars.
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
    The appearance of the left axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    top_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=30))
    """
    The appearance of the top axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    right_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=44))
    """
    The appearance of the right axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    bottom_axis: ChartAxis = field(default_factory=lambda: ChartAxis(label_size=30))
    """
    The appearance of the bottom axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    baseline_y: Optional[ft.Number] = None
    """
    Baseline value for Y axis.
    """

    min_y: Optional[ft.Number] = None
    """
    The minimum displayed value for Y axis.
    """

    max_y: Optional[ft.Number] = None
    """
    The maximum displayed value for Y axis.
    """

    tooltip: Optional[BarChartTooltip] = None
    """
    The tooltip configuration for the chart.
    """

    on_event: ft.OptionalEventHandler[BarChartEvent["BarChart"]] = None
    """
    Fires when a bar is hovered or clicked.

    Event handler receives an instance of [`BarChartEvent`][(p).].
    """

    def __post_init__(self, ref: Optional[ft.Ref[Any]]):
        super().__post_init__(ref)
        self._internals["skip_properties"] = ["tooltip"]
