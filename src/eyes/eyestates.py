from abc import ABC, abstractmethod
from PIL import Image, ImageDraw
from datetime import datetime
from math import cos, sin, pi


class Animation(ABC):
    width = 240
    height = 240

    @staticmethod
    def load_image(path: str) -> Image.Image:
        image = Image.open(path)
        return image.rotate(180)

    def prepare_image(self, leftImage, rightImage):
        return [
            self.displays[0].prepare_image(leftImage),
            self.displays[1].prepare_image(rightImage),
        ]

    @abstractmethod
    def init(self, displays):
        self.displays = displays

    @abstractmethod
    def update_interval(self):
        pass

    @abstractmethod
    def update(self):
        pass


class Off(Animation):
    def init(self, displays):
        super().init(displays)
        image = Image.new("RGB", (self.width, self.height), "BLACK")
        self.images = self.prepare_image(image, image)

    def update_interval(self):
        return 0

    def update(self):
        return self.images


class FullOpen(Animation):
    def init(self, displays):
        super().init(displays)
        image = self.load_image("assets/eyes/Open.jpg")
        self.images = self.prepare_image(image, image)

    def update_interval(self):
        return 0

    def update(self):
        return self.images


class Blinking(Animation):
    frame = 0

    def init(self, displays):
        super().init(displays)
        openImage = self.load_image("assets/eyes/Open.jpg")
        halfOpenImage = self.load_image("assets/eyes/HalfOpen.jpg")
        closeImage = self.load_image("assets/eyes/Close.jpg")
        self.open = self.prepare_image(openImage, openImage)
        self.halfOpen = self.prepare_image(halfOpenImage, halfOpenImage)
        self.close = self.prepare_image(closeImage, closeImage)

    def update_interval(self):
        return 3 if self.frame == 1 else 0.1 if self.frame == 2 else 0.2

    def update(self):
        if self.frame == 0:
            self.frame = 1
            return self.open
        if self.frame == 1:
            self.frame == 2
            return self.halfOpen
        self.frame = 0
        return self.close


class BlinkOnce(Animation):
    frame = 0

    def init(self, displays):
        super().init(displays)
        openImage = self.load_image("assets/eyes/Open.jpg")
        closeImage = self.load_image("assets/eyes/Close.jpg")
        offImage = Image.new("RGB", (self.width, self.height), "BLACK")
        self.open = self.prepare_image(openImage, openImage)
        self.close = self.prepare_image(closeImage, closeImage)
        self.off = self.prepare_image(offImage, offImage)

    def update_interval(self):
        return 1 if self.frame != 3 else 0

    def update(self):
        if self.frame == 0:
            self.frame = 1
            return self.open
        if self.frame == 1:
            self.frame == 2
            return self.close
        self.frame = 3
        return self.off


class ClockMode(Animation):
    color_outer = "#D35400"
    color_inner = "#FF8A00"

    def init(self, displays):
        super().init(displays)
        self.clockFace = self.load_image("assets/eyes/ClockFaceBlue.png")
        self.blankImage = Image.new("RGB", (self.width, self.height), "BLACK")

        center = (120, 120)
        l_h = 60
        w_h = 6

        l_m = 85
        w_m = 5

        rim_outer = 7
        self.rim_inner = 3

        self.hour_hand_coordinates = []
        for h in range(720):
            s = sin(pi * h / 360)
            c = cos(pi * h / 360)
            c1 = (center[0] - l_h * s, center[1] + l_h * c)
            c2 = (center[0] - w_h * c, center[1] - w_h * s)
            c3 = (center[0] + w_h * c, center[1] + w_h * s)
            self.hour_hand_coordinates.append([c1, c2, c3])

        self.minute_hand_coordinates = []
        for m in range(60):
            s = sin(pi * m / 30)
            c = cos(pi * m / 30)
            c1 = (center[0] - l_m * s, center[1] + l_m * c)
            c2 = (center[0] - w_m * c, center[1] - w_m * s)
            c3 = (center[0] + w_m * c, center[1] + w_m * s)
            self.minute_hand_coordinates.append([c1, c2, c3])

        self.outer_circle = [
            center[0] - rim_outer,
            center[1] - rim_outer,
            center[0] + rim_outer,
            center[1] + rim_outer,
        ]

    def update_interval(self):
        return 60

    def update(self):
        h = datetime.now().hour % 12
        m = datetime.now().minute

        clock = self.clockFace.copy()
        draw = ImageDraw.Draw(clock)
        draw.polygon(
            self.hour_hand_coordinates[h * 60 + m],
            fill=self.color_inner,
            outline=self.color_outer,
            width=2,
        )
        draw.polygon(
            self.minute_hand_coordinates[m],
            fill=self.color_inner,
            outline=self.color_outer,
            width=2,
        )
        draw.ellipse(
            self.outer_circle,
            fill="black",
            outline=self.color_outer,
            width=self.rim_inner,
        )

        return self.prepare_image(clock, self.blankImage)
