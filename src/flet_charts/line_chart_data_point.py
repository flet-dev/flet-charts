from dataclasses import dataclass
from typing import Optional, Union

import flet as ft

from .types import ChartDataPointTooltip, ChartPointLine, ChartPointShape

__all__ = ["LineChartDataPoint", "LineChartDataPointTooltip"]


@dataclass
class LineChartDataPointTooltip(ChartDataPointTooltip):
    """Tooltip configuration for the [`LineChartDataPoint`][(p).]."""

    text: Optional[str] = None
    """
    The text to display in the tooltip.

    When `None`, defaults to [`LineChartDataPoint.y`][(p).].
    """


@ft.control("LineChartDataPoint")
class LineChartDataPoint(ft.BaseControl):
    """A [`LineChartData`][(p).] point."""

    x: ft.Number
    """
    The position of a point on `X` axis.
    """

    y: ft.Number
    """
    The position of a point on `Y` axis.
    """

    selected: Optional[bool] = None
    """
    Draw the point as selected when `LineChart.interactive` is set to False.
    """

    point: Union[None, bool, ChartPointShape] = None
    """
    Defines the appearance and shape of a line point.

    Value is of type [`ChartPointShape`][(p).].
    """

    selected_point: Union[None, bool, ChartPointShape] = None
    """
    Defines the appearance and shape of a selected line point.

    Value is of type [`ChartPointShape`][(p).].
    """

    show_above_line: Optional[bool] = None
    """
    Whether to display a line above data point.

    Defaults to `True`.
    """

    show_below_line: Optional[bool] = None
    """
    Whether to display a line below data point.

    Defaults to `True`.
    """

    selected_below_line: Union[None, bool, ChartPointLine] = None
    """
    A vertical line drawn between selected line point and the bottom adge of the chart.

    The value is either `True` - draw a line with default style, `False` - do not draw a
    line under selected point, or an instance of
    [`ChartPointLine`](https://flet.dev/docs/reference/types/chartpointline) class to
    specify line style to draw.
    """

    tooltip: Optional[LineChartDataPointTooltip] = None
    """
    Configuration of the tooltip for this data point.
    """

    show_tooltip: bool = True
    """
    Whether a tooltip should be shown on top of hovered data point.
    """
