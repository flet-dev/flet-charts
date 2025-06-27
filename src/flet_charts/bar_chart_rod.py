from dataclasses import dataclass, field
from typing import Any, Optional

import flet as ft

from .bar_chart_rod_stack_item import BarChartRodStackItem
from .types import ChartDataPointTooltip

__all__ = ["BarChartRod", "BarChartRodTooltip"]


@dataclass
class BarChartRodTooltip(ChartDataPointTooltip):
    """
    Tooltip configuration for the  [`BarChartRod`][(p).].
    """

    text: Optional[str] = None
    """
    The text to display in the tooltip.

    When `None`, defaults to [`BarChartRod.to_y`][(p).].
    """


@ft.control("BarChartRod")
class BarChartRod(ft.BaseControl):
    """A bar rod in a [`BarChartGroup`][(p).]."""

    stack_items: list[BarChartRodStackItem] = field(default_factory=list)
    """
    Optional list of [`BarChartRodStackItem`][(p).] objects to draw a stacked bar.
    """

    from_y: ft.Number = 0
    """
    Specifies a starting position of this rod on Y axis.
    """

    to_y: Optional[ft.Number] = None
    """
    Specifies an ending position of this rod on Y axis.
    """

    width: Optional[ft.Number] = None
    """
    The width of this rod.
    """

    color: Optional[ft.ColorValue] = None
    """
    Rod [color](https://flet.dev/docs/reference/colors).
    """

    gradient: Optional[ft.Gradient] = None
    """
    Gradient to draw rod's background.

    Value is of type [`Gradient`](https://flet.dev/docs/reference/types/gradient).
    """

    border_radius: Optional[ft.BorderRadiusValue] = None
    """
    Border radius of a bar rod.
    """

    border_side: Optional[ft.BorderSide] = None
    """
    Border to draw around rod.

    Value is of type [`BorderSide`](https://flet.dev/docs/reference/types/borderside)
    class.
    """

    bg_from_y: Optional[ft.Number] = None
    """
    An optional starting position of a background behind this rod.
    """

    bg_to_y: Optional[ft.Number] = None
    """
    An optional ending position of a background behind this rod.
    """

    bgcolor: Optional[ft.ColorValue] = None
    """
    An optional [color](https://flet.dev/docs/reference/colors) of a background behind
    this rod.
    """

    background_gradient: Optional[ft.Gradient] = None
    """
    An optional gradient to draw a background with.
    """

    selected: bool = False
    """
    If set to `True` a tooltip is always shown on top of the bar when
    `BarChart.interactive` is set to `False`.
    """

    tooltip: BarChartRodTooltip = field(default_factory=lambda: BarChartRodTooltip())
    """
    The rod's tooltip configuration for this rod.
    """

    show_tooltip: bool = True
    """
    Whether a tooltip should be shown on top of hovered bar.
    """

