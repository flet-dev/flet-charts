import asyncio
import logging
from dataclasses import field

import flet as ft
import flet.canvas as fc

logging.basicConfig(level=logging.INFO)

try:
    from matplotlib.figure import Figure
except ImportError as e:
    raise Exception(
        'Install "matplotlib" Python package to use MatplotlibChart control.'
    ) from e

__all__ = ["MatplotlibChart"]


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

    def init(self):
        # self.on_resize = self.on_canvas_resize
        # self.shapes = [fc.Line(x1=0, y1=0, x2=50, y2=50)]
        self.mouse_cursor = ft.MouseCursor.WAIT
        self.__started = False
        self.__dpr = self.page.media.device_pixel_ratio
        print("DPR:", self.__dpr)
        self.__image_mode = "full"

        self.canvas = fc.Canvas(
            # resize_interval=10,
            on_resize=self.on_canvas_resize,
            expand=True,
        )
        self.content = self.canvas
        self.on_pan_start = self._pan_start
        self.on_pan_update = self._pan_update
        self.on_pan_end = self._pan_end
        self.img_count = 1
        self._receive_queue = asyncio.Queue()
        self._main_loop = asyncio.get_event_loop()
        self._width = 0
        self._height = 0
        self._waiting = False

    # def before_update(self):
    #     super().before_update()

    def _pan_start(self, e: ft.DragStartEvent):
        # print("MPL._pan_start:", e.local_x, e.local_y)
        self.send_message(
            {
                "type": "button_press",
                "x": e.local_x * self.__dpr,
                "y": e.local_y * self.__dpr,
                "button": 0,
                "buttons": 1,
                "modifiers": [],
            }
        )

    def _pan_update(self, e: ft.DragUpdateEvent):
        # print("MPL._pan_update:", e.local_x, e.local_y)
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
        # print("MPL._pan_end:", e.local_x, e.local_y)
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

    def will_unmount(self):
        self.figure.canvas.manager.remove_web_socket(self)

    def pan(self):
        print("MPL.pan()")
        self.send_message({"type": "toolbar_button", "name": "pan"})

    async def _receive_loop(self):
        while True:
            is_binary, content = await self._receive_queue.get()
            if is_binary:
                print(f"MPL.receive_binary({len(content)})")
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
                self.update()
                await self.canvas.capture_async()
                self.img_count += 1
                self._waiting = False
            else:
                print(f"MPL.receive_json({content})")
                if content["type"] == "image_mode":
                    self.__image_mode = content["mode"]
                elif content["type"] == "draw" and not self._waiting:
                    self._waiting = True
                    await self.send_message_async({"type": "draw"})
                elif content["type"] == "resize":
                    self.send_message({"type": "refresh"})

    async def send_message_async(self, message):
        print(f"MPL.send_message_async({message})")
        manager = self.figure.canvas.manager
        if manager is not None:
            await asyncio.to_thread(manager.handle_json, message)

    def send_message(self, message):
        print(f"MPL.send_message({message})")
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
        print("on_canvas_resize:", e.width, e.height)

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
