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


GUI = Builder.load_string("""

GridLayout:
    cols: 1
    ScreenManager:
        id: screen_manager
        CameraClickScreen:
            name: "camera_click_screen"
            id: camera_click_screen
        CheckScreen:
            name: "check_screen"
            id: check_screen
        SuccessScreen:
            name: "success_screen"
            id: success_screen
        BlockAlcoScreen:
            name: "block_alco_screen"
            id: block_alco_screen
        BlockPhotoScreen:
            name: "block_photo_screen"
            id: block_photo_screen


<CameraClickScreen>:
    orientation: 'vertical'
    GridLayout:
        size_hint: (0.8, 0.9)
        cols: 1
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        Image:
            id: gif
            source: 'fizzzgen-development-logo.png'
            allow_stretch: True
            size_hint_y: None
            height: '90dp'
        Camera:
            id: camera
            resolution: (640, 480)
            play: True
            allow_stretch: True
        Button:
            text: 'Войти'
            background_color: (0,1,0,1)
            size_hint_y: None
            height: '90dp'
            font_size: 50
            on_press:
                root.capture()
                # root refers to <CameraClickScreen>
                # app refers to TestCamera, app.root refers to the GridLayout: at the top
                app.root.ids['screen_manager'].transition.direction = 'left'
                app.root.ids['screen_manager'].current = 'check_screen'

<CheckScreen>:
    orientation: 'vertical'
    GridLayout:
        size_hint: (0.8, 0.9)
        cols: 1
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        Image:
            id: gif
            source: 'fizzzgen-development-logo.png'
            allow_stretch: True
            size_hint_y: None
            height: '90dp'
        Label:
            text: "Приветствуем, Кирилл Богатырев!\\nПожалуйста, подуйте в алкотестер..."
            font_size: 60
            color: 0,0,0,1
            size_hint_y: None
            height: '180dp'
        Image:
            id: gif
            source: 'loading-9.gif'
            allow_stretch: True
            anim_delay: 0.03
            anim_loop: 1000
        Button:
            text: "Назад"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'camera_click_screen'
            font_size: 50
        Button:
            text: "Алко Стоп Экран"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'block_alco_screen'
            font_size: 50
        Button:
            text: "Фото Стоп Экран"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'block_photo_screen'
            font_size: 50
        Button:
            text: "Успешное прохождение экран"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'success_screen'
            font_size: 50

<BlockAlcoScreen>:
    orientation: 'vertical'
    GridLayout:
        size_hint: (0.8, 0.9)
        cols: 1
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        Image:
            id: gif
            source: 'fizzzgen-development-logo.png'
            allow_stretch: True
            size_hint_y: None
            height: '90dp'
        Label:
            text: "Вы не прошли тестирование."
            font_size: 60
            color: 1,0,0,1
            size_hint_y: None
            height: '180dp'
        Image:
            id: gif
            source: 'stop.png'
            allow_stretch: True
            anim_delay: 0.03
            anim_loop: 1000
        Button:
            text: "Пройти заново"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'camera_click_screen'
            font_size: 50

<BlockPhotoScreen>:
    orientation: 'vertical'
    GridLayout:
        size_hint: (0.8, 0.9)
        cols: 1
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        Image:
            id: gif
            source: 'fizzzgen-development-logo.png'
            allow_stretch: True
            size_hint_y: None
            height: '90dp'
        Label:
            text: "Ваше фото неопознано.\\nПройдите распознавание заново,\\nлибо зарегистрируйтесь"
            font_size: 60
            color: 0,0,0,1
            size_hint_y: None
            height: '180dp'
        Image:
            id: gif
            source: 'stop.png'
            allow_stretch: True
            anim_delay: 0.03
            anim_loop: 1000
        Button:
            text: "Регистрация"
            background_color: (0,1,0,1)
            size_hint_y: None
            height: '90dp'
            font_size: 50
        Button:
            text: "Пройти заново"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'camera_click_screen'
            font_size: 50

<SuccessScreen>:
    orientation: 'vertical'
    GridLayout:
        size_hint: (0.8, 0.9)
        cols: 1
        pos_hint: {'center_y': 0.5, 'center_x': 0.5}
        Image:
            id: gif
            source: 'fizzzgen-development-logo.png'
            allow_stretch: True
            size_hint_y: None
            height: '90dp'
        Label:
            text: "Проходите.\\nНе забывайте надевать каску."
            font_size: 60
            color: 0,0,0,1
            size_hint_y: None
            height: '180dp'
        Image:
            id: gif
            source: 'helmet.jpg'
            allow_stretch: True
            anim_delay: 0.03
            anim_loop: 1000
        Button:
            text: "Пройти заново"
            size_hint_y: None
            height: '90dp'
            on_press:
                app.root.ids['screen_manager'].transition.direction = 'right'
                app.root.ids['screen_manager'].current = 'camera_click_screen'
            font_size: 50
""")

class TestCamera(App):
    def build(self):
        return GUI

TestCamera().run()
