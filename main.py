from kivy.app import App
from views.cosplay_view import CosplayView

class CosplayApp(App):
    def build(self):
        return CosplayView()

if __name__ == '__main__':
    CosplayApp().run()

