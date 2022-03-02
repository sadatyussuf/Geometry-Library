from geom.geom import Geom


class Point(Geom):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def length(self):
        pass

    def __str__(self):
        return f'POINT ({self.x} {self.y})'


if __name__ == "__main__":
    # WKT : https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    p = Point(3, 4)  # POINT (3 4)
    print(p)
