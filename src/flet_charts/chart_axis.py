from dataclasses import field
from typing import Optional, Union

import flet as ft

__all__ = ["ChartAxis", "ChartAxisLabel"]


@ft.control("ChartAxisLabel")
class ChartAxisLabel(ft.BaseControl):
    """
    Configures a custom label for specific value.
    """

    value: Optional[ft.Number] = None
    """
    A value to draw label for.
    """

    label: Optional[Union[ft.Control, str]] = None
    """
    The label to display for the specified `value`.
    
    Can be a string or a `Control`.
    """


@ft.control("ChartAxis")
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
    The list of [`ChartAxisLabel`][(p).]
    objects to set custom axis labels for only specific values.
    """

    label_spacing: Optional[ft.Number] = None
    """
    The interval between automatic labels.
    """

    label_size: ft.Number = 22
    """
    Width or height of labels area.
    """
