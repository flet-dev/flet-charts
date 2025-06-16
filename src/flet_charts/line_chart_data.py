from dataclasses import field
from typing import Optional, Union

import flet as ft

from .line_chart_data_point import LineChartDataPoint
from .types import ChartPointLine, ChartPointShape

__all__ = ["LineChartData"]


@ft.control("LineChartData")
class LineChartData(ft.BaseControl):
    points: list[LineChartDataPoint] = field(default_factory=list)
    """
    A list of points (dots) of [`LineChartDataPoint`][(p).]
    type representing a single chart line.
    """

    curved: bool = False
    """
    Set to `True` to draw chart line as a curve.
    """

    color: ft.ColorValue = ft.Colors.CYAN
    """
    A [color](https://flet.dev/docs/reference/colors) of chart line.
    """

    gradient: Optional[ft.Gradient] = None
    """
    Gradient to draw line's background.

    Value is of type [`Gradient`](https://flet.dev/docs/reference/types/gradient).
    """

    stroke_width: ft.Number = 2.0
    """
    The width of a chart line.
    """

    rounded_stroke_cap: bool = False
    """
    Whether to draw rounded line caps.
    """

    prevent_curve_over_shooting: bool = False
    """
    Whether to prevent overshooting when draw curve line on linear sequence spots.
    """

    prevent_curve_over_shooting_threshold: ft.Number = 10.0
    """
    Threshold to prevent overshooting algorithm.
    """

    dash_pattern: Optional[list[int]] = None
    """
    Defines dash effect of the line. The value is a circular list of dash offsets
    and lengths. For example, the list `[5, 10]` would result in dashes 5 pixels
    long followed by blank spaces 10 pixels long. By default, a solid line is
    drawn.
    """

    shadow: ft.BoxShadow = field(default_factory=lambda: ft.BoxShadow(color=ft.Colors.TRANSPARENT))
    """
    Shadow to drop by a chart line.

    Value is of type [`BoxShadow`](https://flet.dev/docs/reference/types/boxshadow).
    """

    above_line_bgcolor: Optional[ft.ColorValue] = None
    """
    Fill the area above chart line with the specified
    [color](https://flet.dev/docs/reference/colors).
    """

    above_line_gradient: Optional[ft.Gradient] = None
    """
    Fill the area above chart line with the specified gradient.
    """

    above_line_cutoff_y: Optional[ft.Number] = None
    """
    Cut off filled area above line chart at specific Y value.
    """

    above_line: Optional[ChartPointLine] = None
    """
    A vertical line drawn between a line point and the top edge of the chart.

    Value is of type [`ChartPointLine`][(p).].
    """

    below_line_bgcolor: Optional[ft.ColorValue] = None
    """
    Fill the area below chart line with the specified
    [color](https://flet.dev/docs/reference/colors).
    """

    below_line_gradient: Optional[ft.Gradient] = None
    """
    Fill the area below chart line with the specified gradient.
    """

    below_line_cutoff_y: Optional[ft.Number] = None
    """
    Cut off filled area below line chart at specific Y value.
    """

    below_line: Optional[ChartPointLine] = None
    """
    A vertical line drawn between a line point and the bottom edge of the chart.

    Value is of type [`ChartPointLine`][(p).].
    """

    selected_below_line: Union[None, bool, ChartPointLine] = None
    """
    A vertical line drawn between selected line point and the bottom adge of the
    chart. The value is either `True` - draw a line with default style, `False` - do
    not draw a line under selected point, or an instance of
    [`ChartPointLine`][(p).] class to
    specify line style to draw.
    """

    point: Union[None, bool, ChartPointShape] = None
    """
    Defines the appearance and shape of a line point (dot).

    Value is of type bool (`True` - draw a point with default style or `False` - do
    not draw a line point) or of type [`ChartPointShape`][(p).].
    """

    selected_point: Union[None, bool, ChartPointShape] = None
    """
    Defines the appearance and shape of a selected line point.

    Value is of type [`ChartPointShape`][(p).].
    """
