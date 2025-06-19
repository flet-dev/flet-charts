from dataclasses import dataclass, field
from typing import Any, Optional

import flet as ft

from .chart_axis import ChartAxis
from .scatter_chart_spot import ScatterChartSpot
from .types import ChartEventType, ChartGridLines, ChartHorizontalAlignment

__all__ = ["ScatterChart", "ScatterChartEvent", "ScatterChartTooltip"]


@dataclass
class ScatterChartTooltip:
    """Configuration of the tooltip for [`ScatterChart`][(p).]s."""

    bgcolor: ft.ColorValue = "#FF607D8B"
    """
    The tooltip's background [color](https://flet.dev/docs/reference/colors).
    """

    border_radius: Optional[ft.BorderRadiusValue] = None
    """
    The tooltip's border radius.
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
    The tooltip's rotation angle in degrees.
    """

    horizontal_offset: Optional[ft.Number] = None
    """
    Applies horizontal offset for showing tooltip.
    """

    horizontal_alignment: Optional[ChartHorizontalAlignment] = None
    """
    The tooltip's horizontal alignment.
    """

    border_side: Optional[ft.BorderSide] = None
    """
    The tooltip's border side.
    """

    fit_inside_horizontally: Optional[bool] = None
    """
    Forces the tooltip to shift horizontally inside the chart, if overflow happens.
    """

    fit_inside_vertically: Optional[bool] = None
    """
    Forces the tooltip to shift vertically inside the chart, if overflow happens.
    """


@dataclass
class ScatterChartEvent(ft.Event[ft.EventControlType]):
    type: ChartEventType
    """
    Type of the event (e.g. tapDown, panUpdate)
    """

    spot_index: Optional[int] = None
    """
    Index of the touched spot, if any
    """


@ft.control("ScatterChart")
class ScatterChart(ft.ConstrainedControl):
    """
    A scatter chart control.

    ScatterChart draws some points in a square space,
    points are defined by [`ScatterChartSpot`][(p).]s.
    """

    spots: list[ScatterChartSpot] = field(default_factory=list)
    """
    List of [`ScatterChartSpot`][(p).]s to show on the chart.
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

    handle_built_in_touches: bool = True
    """
    Whether to show a tooltip popup on top of the spots if a touch occurs.
    """

    long_press_duration: Optional[ft.DurationValue] = None
    """
    The duration of a long press on the chart.
    """

    bgcolor: Optional[ft.ColorValue] = None
    """
    The chart's background color.
    """

    border: Optional[ft.Border] = None
    """
    The border around the chart.
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

    left_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    Configures the appearance of the left axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    top_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    Configures the appearance of the top axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    right_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    Configures the appearance of the right axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    bottom_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    Configures the appearance of the bottom axis, its title and labels.

    Value is of type [`ChartAxis`][(p).].
    """

    baseline_x: Optional[ft.Number] = None
    """
    The baseline value for X axis.
    """

    min_x: Optional[ft.Number] = None
    """
    The minimum displayed value for X axis.
    """

    max_x: Optional[ft.Number] = None
    """
    The maximum displayed value for X axis.
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

    tooltip: Optional[ScatterChartTooltip] = None
    """
    The tooltip configuration for the chart.
    """

    on_event: ft.OptionalEventHandler[ScatterChartEvent["ScatterChart"]] = None
    """
    Fires when an event occurs on the chart.
    
    Event handler receives an instance of [`ScatterChartEvent`][(p).].
    """

    def __post_init__(self, ref: Optional[ft.Ref[Any]]):
        super().__post_init__(ref)
        self._internals["skip_properties"] = ["tooltip"]
