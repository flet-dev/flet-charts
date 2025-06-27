import io
import re
import xml.etree.ElementTree as ET
from dataclasses import field

import flet as ft

try:
    from matplotlib.figure import Figure
except ImportError as e:
    raise Exception(
        'Install "matplotlib" Python package to use MatplotlibChart control.'
    ) from e

__all__ = ["MatplotlibChart"]


@ft.control(kw_only=True)
class MatplotlibChart(ft.Container):
    """
    Displays a [Matplotlib](https://matplotlib.org/) chart.

    Warning:
        This control requires the [`matplotlib`](https://matplotlib.org/) Python package to be installed.

        See this [installation guide](index.md#installation) for more information.
    """

    figure: Figure = field(metadata={"skip": True})
    """
    Matplotlib figure to draw - an instance of 
    [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure).
    """

    original_size: bool = False
    """
    Whether to display chart in original size.

    Set to `False` to display a chart that fits configured bounds.
    """

    transparent: bool = False
    """
    Whether to remove the background from the chart.
    """

    def init(self):
        self.alignment = ft.Alignment.center()
        self.__img = ft.Image(fit=ft.BoxFit.FILL)
        self.content = self.__img

    def before_update(self):
        super().before_update()
        if self.figure is not None:
            s = io.StringIO()
            self.figure.savefig(s, format="svg", transparent=self.transparent)
            svg = s.getvalue()

            if not self.original_size:
                root = ET.fromstring(svg)
                w = float(re.findall(r"\d+", root.attrib["width"])[0])
                h = float(re.findall(r"\d+", root.attrib["height"])[0])
                self.__img.aspect_ratio = w / h
            self.__img.src = svg
