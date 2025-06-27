from dataclasses import dataclass, field
from typing import Optional

import flet as ft

from .pie_chart_section import PieChartSection
from .types import ChartEventType

__all__ = ["PieChart", "PieChartEvent"]


@dataclass
class PieChartEvent(ft.Event[ft.EventControlType]):
    type: ChartEventType
    """
    Type of the event.

    Value is of type [`ChartEventType`][(p).].
    """

    section_index: Optional[int] = None
    """
    Section's index or `-1` if no section was hovered.
    """

    local_x: Optional[float] = None
    """
    X coordinate of the local position where the event occurred.
    """

    local_y: Optional[float] = None
    """
    Y coordinate of the local position where the event occurred.
    """


@ft.control("PieChart")
class PieChart(ft.ConstrainedControl):
    """
    A pie chart control displaying multiple sections as slices of a circle.

    ![Overview](assets/pie-chart/diagram.svg)
    """

    sections: list[PieChartSection] = field(default_factory=list)
    """
    A list of [`PieChartSection`][(p).]
    controls drawn in a circle.
    """

    center_space_color: Optional[ft.ColorValue] = None
    """
    Free space [color](https://flet.dev/docs/reference/colors) in the middle of a chart.
    """

    center_space_radius: Optional[ft.Number] = None
    """
    Free space radius in the middle of a chart.
    """

    sections_space: Optional[ft.Number] = None
    """
    A gap between `sections`.
    """

    start_degree_offset: Optional[ft.Number] = None
    """
    By default, `sections` are drawn from zero degree (right side of the circle)
    clockwise. You can change the starting point by setting `start_degree_offset`
    (in degrees).
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

    on_event: ft.OptionalEventHandler[PieChartEvent["PieChart"]] = None
    """
    Fires when a chart section is hovered or clicked.

    Event data is an instance [`PieChartEvent`][(p).].
    """
