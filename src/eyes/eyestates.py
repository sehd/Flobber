from abc import ABC, abstractmethod
from PIL import Image


class Animation(ABC):
    width = 240
    height = 240

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
        return 3 if self.frame == 0 else 0.1 if self.frame == 1 else 0.2

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
        return 1 if self.frame != 2 else 0

    def update(self):
        if self.frame == 0:
            self.frame = 1
            return self.open
        if self.frame == 1:
            self.frame == 2
            return self.close
        return self.off
