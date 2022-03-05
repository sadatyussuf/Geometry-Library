from geom import Geom

import math


class Point(Geom):
    def __init__(self, x: float, y: float):
        super().__init__()
        self.x = x
        self.y = y

    def length(self, otherX, otherY):
        #  pt1, pt2 = line
        pt1sq = (otherX - self.x)**2
        pt2sq = (otherY - self.y)**2
        dist_Line = round(math.sqrt((pt1sq + pt2sq)), 3)
        print(dist_Line)

        return dist_Line

    def __str__(self):
        return f'POINT ({self.x} {self.y})'


if __name__ == "__main__":
    # WKT : https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry
    p = Point(9, 7)  # POINT (3 4)
    p.length(3, 2)
    print(p)
