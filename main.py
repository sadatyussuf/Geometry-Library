from geom import Geom


def test(*params):
    pts = [*params]
    geom = Geom(pts)
    perimeter = geom.length()
    area = geom.area()
    print(perimeter)


if __name__ == '__main__':
    test([5, 8], [9, 8])
    test([5, 8], [9, 7], [84, 17])
    test([96, 85], [51, 81], [91, 78])
