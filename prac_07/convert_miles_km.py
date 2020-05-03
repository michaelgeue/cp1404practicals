"""
CP 1404
Convert Miles to KM Practical
By Michael Geue
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesToKmConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value):
        try:
            self.root.ids.input_number.text = str(int(self.root.ids.input_number.text) + value)
        except ValueError:
            self.root.ids.input_number.text = str(0 + value)

    def handle_calculate(self, value):
        try:
            result = int(value) * MILES_TO_KM
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0.0"


MilesToKmConverter().run()
