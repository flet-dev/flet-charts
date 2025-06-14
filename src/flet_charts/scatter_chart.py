from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import flet as ft

from .chart_axis import ChartAxis
from .scatter_chart_spot import ScatterChartSpot
from .types import ChartEventType, ChartHorizontalAlignment

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
class ScatterChartEvent(ft.ControlEvent):
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

    animate: Optional[ft.AnimationValue] = None
    """
    TBD
    """

    interactive: bool = True
    """
    TBD
    """

    handle_built_in_touches: bool = True
    """
    TBD
    """

    long_press_duration: Optional[int] = None
    """
    TBD
    """

    bgcolor: Optional[ft.ColorValue] = None
    """
    TBD
    """

    border: Optional[ft.Border] = None
    """
    TBD
    """

    horizontal_grid_lines: Optional[ft.ChartGridLines] = None
    """
    TBD
    """

    vertical_grid_lines: Optional[ft.ChartGridLines] = None
    """
    TBD
    """

    left_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    TBD
    """

    top_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    TBD
    """

    right_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    TBD
    """

    bottom_axis: ChartAxis = field(default_factory=lambda: ChartAxis())
    """
    TBD
    """

    baseline_x: Optional[ft.Number] = None
    """
    TBD
    """

    min_x: Optional[ft.Number] = None
    """
    TBD
    """

    max_x: Optional[ft.Number] = None
    """
    TBD
    """

    baseline_y: Optional[ft.Number] = None
    """
    TBD
    """

    min_y: Optional[ft.Number] = None
    """
    TBD
    """

    max_y: Optional[ft.Number] = None
    """
    TBD
    """

    tooltip: Optional[ScatterChartTooltip] = None
    """
    The tooltip configuration for the chart.
    """

    on_event: ft.OptionalEventCallable[ScatterChartEvent] = None
    """
    TBD
    """
