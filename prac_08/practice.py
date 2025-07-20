from kivy.app import App
from kivy.lang import builder

class BoxlayoutDemo(App):

    def build(self):
        self.title = "layout demo"
        self.root = Bulder.load_file("box_layout.kv")
        return self.root

BoxLayoutDemo().run()

