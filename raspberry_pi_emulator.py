from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, SmoothLine
from kivy.clock import Clock

from pin_patterns import PatternAlgorithm


class RPApp(App):
    def __init__(self, **kwargs):
        super(RPApp, self).__init__(**kwargs)
        self.widget = Widget()
        self.pattern_algorithm = PatternAlgorithm(loop_count=18)

    def build(self):
        Clock.schedule_interval(self.setpinsauto, 0.1)
        return self.widget

    def setpinsauto(self, cb):
        self.setpins(self.pattern_algorithm.next())

    def setpins(self, pins):
        if len(pins) != 8:
            raise ValueError("Pins size should be 8")

        with self.widget.canvas:
            for idx, pin in enumerate(pins):
                if pin == 1:
                    Color(0, 0.9, 0)
                else:
                    Color(0, 0, 0)
                ''' Straight line
                Ellipse(pos=(60 + idx * 90, 300), size=(50, 50))
                Color(0.3, 0.3, 0.3)
                SmoothLine(circle=[85 + idx * 90, 325, 25], width=3)
                '''
                ''' Two lines '''
                Ellipse(pos=(60 + (idx%4) * 90, 300 + (idx/4)*75), size=(50, 50))
                Color(0.3, 0.3, 0.3)
                SmoothLine(circle=[85 + (idx%4) * 90, 325 + (idx/4)*75, 25], width=3)



if __name__ == '__main__':
    app = RPApp()
    app.run()
