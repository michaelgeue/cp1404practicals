"""
CP 1404
Dynamic Labels Practical
By Michael Geue
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ['Michael Geue', 'Darcy Jones', 'John Smith', 'Some Guy', 'Another Guy']


class DynamicLabels(App):

    def build(self):
        self.title = "Dynamic Name Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in NAMES:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_label)


DynamicLabels().run()
