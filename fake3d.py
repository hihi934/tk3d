import tkinter as tk
from tk3d.core.camera import Camera

class FakeRenderer:
    def __init__(self, solid=False, rotate=True):
        self.root = tk.Tk()
        self.root.title("tk3d")

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="black")
        self.canvas.pack()

        self.camera = Camera()
        self.objects = []

        self.solid = solid
        self.rotate = rotate

    def add(self, obj):
        self.objects.append(obj)

    def update(self):
        self.canvas.delete("all")

        for obj in self.objects:
            obj.draw(self)

        if self.rotate:
            self.camera.angle += 0.03

        self.root.after(30, self.update)

    def run(self):
        self.update()
        self.root.mainloop()
