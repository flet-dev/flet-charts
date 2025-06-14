from dataclasses import field
from typing import Optional

import flet as ft

__all__ = ["ChartAxis", "ChartAxisLabel"]


@ft.control("l")
class ChartAxisLabel(ft.BaseControl):
    """
    Configures a custom label for specific value.
    """

    value: Optional[ft.Number] = None
    """
    A value to draw label for.
    """

    label: Optional[ft.Control] = None
    """
    A `Control` to draw as a label.
    """


@ft.control("a")
class ChartAxis(ft.BaseControl):
    """
    Configures chart axis.
    """

    title: Optional[ft.Control] = None
    """
    A `Control` to display as axis title.
    """

    title_size: ft.Number = 16
    """
    Width or height of title area.
    """

    show_labels: bool = True
    """
    Whether to display the `labels` along the axis. 
    If `labels` is empty then automatic labels are displayed.
    """

    labels: list[ChartAxisLabel] = field(default_factory=list)
    """
    The list of [`ChartAxisLabel`][...]
    objects to set custom axis labels for only specific values.
    """

    labels_interval: Optional[ft.Number] = None
    """
    The interval between automatic labels.
    """

    labels_size: ft.Number = 22
    """
    Width or height of labels area.
    """
