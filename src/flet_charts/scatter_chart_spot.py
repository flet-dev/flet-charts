from dataclasses import dataclass, field
from typing import Any, Optional, Union

import flet as ft

from .types import ChartDataPointTooltip, ChartPointShape

__all__ = ["ScatterChartSpot", "ScatterChartSpotTooltip"]


@dataclass
class ScatterChartSpotTooltip(ChartDataPointTooltip):
    """
    Tooltip configuration for the [`ScatterChartSpot`][(p).].
    """

    text: Optional[str] = None
    """
    The text to display in the tooltip.

    When `None`, defaults to [`ScatterChartSpot.y`][(p).].
    """


@ft.control("ScatterChartSpot")
class ScatterChartSpot(ft.BaseControl):
    """A spot on a scatter chart."""

    x: Optional[ft.Number] = None
    """
    The position of a spot on `X` axis.
    """

    y: Optional[ft.Number] = None
    """
    The position of a spot on `Y` axis.
    """

    visible: bool = True
    """
    Determines wether to show or hide the spot.
    """

    radius: Optional[ft.Number] = None
    """
    Radius of a spot.
    """

    color: Optional[ft.ColorValue] = None
    """
    Color of a spot.
    """

    render_priority: ft.Number = 0
    """
    Sort by this to manage overlap.
    """

    x_error: Optional[Any] = None
    """
    Determines the error range of the data point using 
    (FlErrorRange)[https://github.com/imaNNeo/fl_chart/blob/main/repo_files/documentations/base_chart.md#flerrorrange] 
    (which ontains lowerBy and upperValue) for the `X` axis.
    """

    y_error: Optional[Any] = None
    """
    Determines the error range of the data point using 
    (FlErrorRange)[https://github.com/imaNNeo/fl_chart/blob/main/repo_files/documentations/base_chart.md#flerrorrange] 
    (which ontains lowerBy and upperValue) for the `Y` axis.
    """

    selected: bool = False
    """
    TBD
    """

    tooltip: ScatterChartSpotTooltip = field(default_factory=lambda: ScatterChartSpotTooltip())
    """
    Tooltip configuration for this spot.
    """

    show_tooltip: bool = True
    """
    Wether to show the tooltip.
    """

    label_text: Optional[str] = None
    """
    TBD
    """

    label_style: Optional[ft.TextStyle] = None
    """
    TBD
    """

    point: Union[None, bool, ChartPointShape] = None
    """
    TBD
    """

