from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)


class CheckScreen(Screen):
    pass
class BlockPhotoScreen(Screen):
    pass
class BlockAlcoScreen(Screen):
    pass
class SuccessScreen(Screen):
    pass


class CameraClickScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))

GUI = Builder.load_file("layout.kv")

class TestCamera(App):
    def build(self):
        return GUI

TestCamera().run()
