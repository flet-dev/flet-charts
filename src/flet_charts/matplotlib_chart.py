import asyncio
from io import BytesIO
import logging
from dataclasses import dataclass, field

import flet as ft
import flet.canvas as fc

try:
    from matplotlib.figure import Figure
except ImportError as e:
    raise Exception(
        'Install "matplotlib" Python package to use MatplotlibChart control.'
    ) from e

__all__ = ["MatplotlibChart", "MatplotlibChartMessageEvent", "MatplotlibChartToolbarButtonsUpdateEvent"]

logger = logging.getLogger("flet-charts.matplotlib")

figure_cursors = {
    "default": None,
    "pointer": ft.MouseCursor.CLICK,
    "crosshair": ft.MouseCursor.PRECISE,
    "move": ft.MouseCursor.MOVE,
    "wait": ft.MouseCursor.WAIT,
    "ew-resize": ft.MouseCursor.RESIZE_LEFT_RIGHT,
    "ns-resize": ft.MouseCursor.RESIZE_UP_DOWN
}

@dataclass
class MatplotlibChartMessageEvent(ft.Event["MatplotlibChart"]):    
    message: str
    """
    Message text.
    """

@dataclass
class MatplotlibChartToolbarButtonsUpdateEvent(ft.Event["MatplotlibChart"]):    
    back_enabled: bool
    """
    Whether Back button is enabled or not.
    """
    forward_enabled: bool
    """
    Whether Forward button is enabled or not.
    """

@ft.control(kw_only=True)
class MatplotlibChart(ft.GestureDetector):
    """
    Displays a [Matplotlib](https://matplotlib.org/) chart.

    Warning:
        This control requires the [`matplotlib`](https://matplotlib.org/) Python package
        to be installed.

        See this [installation guide](index.md#installation) for more information.
    """

    figure: Figure = field(metadata={"skip": True})
    """
    Matplotlib figure to draw - an instance of 
    [`matplotlib.figure.Figure`](https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.html#matplotlib.figure.Figure).
    """

    on_message: ft.OptionalEventHandler[MatplotlibChartMessageEvent] = None
    """
    The event is triggered on figure message update.
    """

    on_toolbar_buttons_update: ft.OptionalEventHandler[MatplotlibChartToolbarButtonsUpdateEvent] = None
    """
    Triggers when toolbar buttons status is updated.
    """

    def init(self):
        # self.on_resize = self.on_canvas_resize
        # self.shapes = [fc.Line(x1=0, y1=0, x2=50, y2=50)]
        self.mouse_cursor = ft.MouseCursor.WAIT
        self.__started = False
        self.__dpr = self.page.media.device_pixel_ratio
        logger.debug(f"DPR: {self.__dpr}")
        self.__image_mode = "full"

        self.canvas = fc.Canvas(
            # resize_interval=10,
            on_resize=self.on_canvas_resize,
            expand=True,
        )
        self.keyboard_listener = ft.KeyboardListener(self.canvas, autofocus=True, on_key_down=self._on_key_down, on_key_up=self._on_key_up)
        self.content = self.keyboard_listener
        self.on_enter = self._on_enter
        self.on_hover = self._on_hover
        self.on_exit = self._on_exit
        self.on_pan_start = self._pan_start
        self.on_pan_update = self._pan_update
        self.on_pan_end = self._pan_end
        self.on_right_pan_start = self._right_pan_start
        self.on_right_pan_update = self._right_pan_update
        self.on_right_pan_end = self._right_pan_end
        self.img_count = 1
        self._receive_queue = asyncio.Queue()
        self._main_loop = asyncio.get_event_loop()
        self._width = 0
        self._height = 0
        self._waiting = False

    # def before_update(self):
    #     super().before_update()

    def _on_key_down(self, e):
        logger.debug(f"ON KEY DOWN: {e}")

    def _on_key_up(self, e):
        logger.debug(f"ON KEY UP: {e}")

    def _on_enter(self, e: ft.HoverEvent):
        logger.debug(f"_on_enter: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "figure_enter",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 0,
                "modifiers": [],
            }
        )

    def _on_hover(self, e: ft.HoverEvent):
        logger.debug(f"_on_hover: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "motion_notify",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 0,
                "modifiers": [],
            }
        )

    def _on_exit(self, e: ft.HoverEvent):
        logger.debug(f"_on_exit: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "figure_leave",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 0,
                "modifiers": [],
            }
        )

    def _pan_start(self, e: ft.DragStartEvent):
        logger.debug(f"_pan_start: {e.local_x}, {e.local_y}")
        self.keyboard_listener.focus()
        self.send_message(
            {
                "type": "button_press",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 1,
                "modifiers": []
            }
        )

    def _pan_update(self, e: ft.DragUpdateEvent):
        logger.debug(f"_pan_update: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "motion_notify",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 1,
                "modifiers": [],
            }
        )

    def _pan_end(self, e: ft.DragEndEvent):
        logger.debug(f"_pan_end: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "button_release",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 0,
                "modifiers": [],
            }
        )

    def _right_pan_start(self, e: ft.DragStartEvent):
        logger.debug(f"_pan_start: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "button_press",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 2,
                "buttons": 2,
                "modifiers": [],
            }
        )

    def _right_pan_update(self, e: ft.DragUpdateEvent):
        logger.debug(f"_pan_update: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "motion_notify",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 2,
                "modifiers": [],
            }
        )

    def _right_pan_end(self, e: ft.DragEndEvent):
        logger.debug(f"_pan_end: {e.local_x}, {e.local_y}")
        self.send_message(
            {
                "type": "button_release",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 2,
                "buttons": 0,
                "modifiers": [],
            }
        )

    def will_unmount(self):
        self.figure.canvas.manager.remove_web_socket(self)

    def home(self):
        logger.debug("home)")
        self.send_message({"type": "toolbar_button", "name": "home"})

    def back(self):
        logger.debug("back()")
        self.send_message({"type": "toolbar_button", "name": "back"})

    def forward(self):
        logger.debug("forward)")
        self.send_message({"type": "toolbar_button", "name": "forward"})

    def pan(self):
        logger.debug("pan()")
        self.send_message({"type": "toolbar_button", "name": "pan"})

    def zoom(self):
        logger.debug("zoom()")
        self.send_message({"type": "toolbar_button", "name": "zoom"})

    def download(self, format):
        logger.debug(f"Download in format: {format}")
        buff = BytesIO()
        self.figure.savefig(buff, format=format, dpi=self.figure.dpi * self.__dpr)
        return buff.getvalue()

    async def _receive_loop(self):
        while True:
            is_binary, content = await self._receive_queue.get()
            if is_binary:
                logger.debug(f"receive_binary({len(content)})")
                if self.__image_mode == "full":
                    await self.canvas.clear_capture_async()

                self.canvas.shapes = [
                    fc.Image(
                        src_bytes=content,
                        x=0,
                        y=0,
                        width=self.figure.bbox.size[0] / self.__dpr,
                        height=self.figure.bbox.size[1] / self.__dpr,
                    )
                ]
                self.canvas.update()
                await self.canvas.capture_async()
                self.img_count += 1
                self._waiting = False
            else:
                logger.debug(f"receive_json({content})")
                if content["type"] == "image_mode":
                    self.__image_mode = content["mode"]
                elif content["type"] == "cursor":
                    self.mouse_cursor = figure_cursors[content["cursor"]]
                    self.update()
                elif content["type"] == "draw" and not self._waiting:
                    self._waiting = True
                    self.send_message({"type": "draw"})
                elif content["type"] == "rubberband":
                    if content["x0"] == -1 and content["y0"] == -1 and content["x1"] == -1 and content["y1"] == -1:
                        if len(self.canvas.shapes) == 2:
                            self.canvas.shapes.pop()
                            self.canvas.update()
                    else:
                        x0 = content["x0"] / self.__dpr
                        y0 = self._height - content["y0"] / self.__dpr
                        x1 = content["x1"] / self.__dpr
                        y1 = self._height - content["y1"] / self.__dpr
                        rubberband_rect = self.canvas.shapes.pop() if len(self.canvas.shapes) == 2 else fc.Rect(paint=ft.Paint(stroke_width=1, style=ft.PaintingStyle.STROKE))
                        rubberband_rect.x = x0
                        rubberband_rect.y = y0
                        rubberband_rect.width = x1 - x0
                        rubberband_rect.height = y1 - y0
                        self.canvas.shapes.append(rubberband_rect)
                        self.canvas.update()
                elif content["type"] == "resize":
                    self.send_message({"type": "refresh"})
                elif content["type"] == "message":
                    await self._trigger_event("message", {"message": content["message"]})
                elif content["type"] == "history_buttons":
                    await self._trigger_event("toolbar_buttons_update", {"back_enabled": content["Back"],"forward_enabled": content["Forward"]})

    def send_message(self, message):
        logger.debug(f"send_message({message})")
        manager = self.figure.canvas.manager
        if manager is not None:
            manager.handle_json(message)

    def send_json(self, content):
        self._main_loop.call_soon_threadsafe(
            lambda: self._receive_queue.put_nowait((False, content))
        )

    def send_binary(self, blob):
        self._main_loop.call_soon_threadsafe(
            lambda: self._receive_queue.put_nowait((True, blob))
        )

    async def on_canvas_resize(self, e: fc.CanvasResizeEvent):
        logger.debug(f"on_canvas_resize: {e.width}, {e.height}")

        if not self.__started:
            self.__started = True
            asyncio.create_task(self._receive_loop())
            self.figure.canvas.manager.add_web_socket(self)
            self.send_message({"type": "send_image_mode"})
            self.send_message(
                {"type": "set_device_pixel_ratio", "device_pixel_ratio": self.__dpr}
            )
            self.send_message({"type": "refresh"})
        self._width = e.width
        self._height = e.height
        self.send_message({"type": "resize", "width": e.width, "height": e.height})
