from tk3d.core.fake3d import FakeRenderer

class App:
    def __init__(self, solid=False, rotate=True):
        self.renderer = FakeRenderer(solid=solid, rotate=rotate)

    def add(self, obj):
        self.renderer.add(obj)

    def run(self):
        self.renderer.run()
