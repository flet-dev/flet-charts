from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

import flet as ft

__all__ = [
    "ChartPointShape",
    "ChartCirclePoint",
    "ChartSquarePoint",
    "ChartCrossPoint",
    "ChartPointLine",
    "ChartEventType",
    "ChartGridLines",
    "ChartDataPointTooltip",
    "ChartHorizontalAlignment",
]


@dataclass
class ChartGridLines:
    """
    Configures the appearance of horizontal and vertical grid lines within the chart.
    """

    interval: Optional[ft.Number] = None
    """
    The interval between grid lines.

    Defaults to `1`.
    """

    color: Optional[ft.ColorValue] = None
    """
    The [color](https://flet.dev/docs/reference/colors) of a grid line.
    """

    width: Optional[ft.Number] = None
    """
    The width of a grid line.

    Defaults to `1`.
    """

    dash_pattern: Optional[list[int]] = None
    """
    Defines dash effect of the line. The value is a circular list of dash offsets
    and lengths. For example, the list `[5, 10]` would result in dashes 5 pixels long
    followed by blank spaces 10 pixels long. By default, a solid line is drawn.
    """


@dataclass(kw_only=True)
class ChartPointShape:
    type: str = ""


@dataclass
class ChartCirclePoint(ChartPointShape):
    color: Optional[ft.ColorValue] = None
    """
    The fill [color](https://flet.dev/docs/reference/colors) to use for the circle.
    """

    radius: Optional[ft.Number] = None
    """
    The radius of the circle.
    """

    stroke_color: Optional[ft.ColorValue] = None
    """
    The stroke [color](https://flet.dev/docs/reference/colors) to use for the circle
    """

    stroke_width: ft.Number = 0
    """
    The stroke width to use for the circle.

    Defaults to `1.0`.
    """

    def __post_init__(self):
        self.type = "circle"


@dataclass
class ChartSquarePoint(ChartPointShape):
    color: Optional[ft.ColorValue] = None
    """
    The fill [color](https://flet.dev/docs/reference/colors) to use for the square.
    """

    size: ft.Number = 4.0
    """
    The size of the square.

    Defaults to `4.0`.
    """

    stroke_color: Optional[ft.ColorValue] = None
    """
    The stroke [color](https://flet.dev/docs/reference/colors) to use for the square.
    """

    stroke_width: ft.Number = 1.0
    """
    The stroke width to use for the square.

    Defaults to `1.0`.
    """

    def __post_init__(self):
        self.type = "square"


@dataclass
class ChartCrossPoint(ChartPointShape):
    color: Optional[ft.ColorValue] = None
    """
    The fill [color](https://flet.dev/docs/reference/colors) to use for the 
    cross-mark(X).
    """

    size: ft.Number = 8.0
    """
    The size of the cross-mark.

    Defaults to `8.0`.
    """

    width: ft.Number = 2.0
    """
    The thickness of the cross-mark.

    Defaults to `2.0`.
    """

    def __post_init__(self):
        self.type = "cross"


@dataclass
class ChartPointLine:
    """"""

    color: Optional[ft.ColorValue] = None
    """
    The line's [color](https://flet.dev/docs/reference/colors).
    """

    width: Optional[float] = None
    """
    The line's width.
    """

    dash_pattern: Optional[list[int]] = None
    """
    The line's dash pattern.
    """


class ChartEventType(Enum):
    """The type of event that occurred on the chart."""

    PAN_END = "PanEnd"
    """
    When a pointer that was previously in contact with 
    the screen and moving is no longer in contact with the screen.
    """

    PAN_CANCEL = "PanCancel"
    """
    When the pointer that previously triggered a pan-start did not complete.
    """

    POINTER_EXIT = "PointerExit"
    """
    The pointer has moved with respect to the device while the 
    pointer is or is not in contact with the device, and exited our chart.
    """

    LONG_PRESS_END = "LongPressEnd"
    """
    When a pointer stops contacting the screen after a long press 
    gesture was detected. Also reports the position where the 
    pointer stopped contacting the screen.
    """

    TAP_UP = "TapUp"
    """
    When a pointer that will trigger a tap has stopped contacting the screen.
    """

    TAP_CANCEL = "TapCancel"
    """
    When the pointer that previously triggered a tap-down will not end up causing a tap.
    """

    POINTER_ENTER = "pointerEnter"
    """
    
    """

    POINTER_HOVER = "pointerHover"
    """

    """

    PAN_DOWN = "panDown"
    """

    """

    PAN_START = "panStart"
    """

    """

    PAN_UPDATE = "panUpdate"
    """

    """

    LONG_PRESS_MOVE_UPDATE = "longPressMoveUpdate"
    """

    """

    LONG_PRESS_START = "longPressStart"
    """

    """

    TAP_DOWN = "tapDown"
    """

    """

    UNDEFINED = "undefined"
    """

    """


@dataclass
class ChartDataPointTooltip:
    """
    Configuration of the tooltip for data points in charts.
    """

    text: Optional[str] = None
    """
    The text to display in the tooltip.
    """

    text_style: ft.TextStyle = field(default_factory=lambda: ft.TextStyle())
    """
    A text style to display tooltip with.

    Value is of type [`TextStyle`](https://flet.dev/docs/reference/types/textstyle).
    """

    text_align: ft.TextAlign = ft.TextAlign.CENTER
    """
    An align for the tooltip.

    Value is of type [`TextAlign`](https://flet.dev/docs/reference/types/textalign).
    """

    text_spans: Optional[list[ft.TextSpan]] = None
    """
    Additional text spans to show on a tooltip.
    """


class ChartHorizontalAlignment(Enum):
    """Defines an element's horizontal alignment to given point."""
    LEFT = "left"
    """Element shown on the left side of the given point."""

    CENTER = "center"
    """Element shown horizontally center aligned to a given point."""

    RIGHT = "right"
    """Element shown on the right side of the given point."""