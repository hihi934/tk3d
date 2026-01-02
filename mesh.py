import math

class Mesh:
    def __init__(self, vertices, faces, pos=(0,0,200), scale=50, color="white"):
        self.vertices = vertices
        self.faces = faces
        self.x, self.y, self.z = pos
        self.scale = scale
        self.color = color

    def draw(self, r):
        cam = r.camera
        a = cam.angle

        transformed = []
        for x, y, z in self.vertices:
            x *= self.scale
            y *= self.scale
            z *= self.scale

            xr = x * math.cos(a) - z * math.sin(a)
            zr = x * math.sin(a) + z * math.cos(a)

            transformed.append((xr+self.x, y+self.y, zr+self.z))

        def project(p):
            z = p[2] + cam.zoom
            if z <= 0:
                z = 0.1
            s = cam.zoom / z
            return (p[0]*s + 300, p[1]*s + 300)

        pts = [project(p) for p in transformed]

        for face in self.faces:
            poly = []
            for i in face:
                poly.extend(pts[i])

            r.canvas.create_polygon(
                *poly,
                outline=self.color,
                fill=self.color if r.solid else "",
                width=2
            )
