from geom import Geom


def test(*params):
    pts = [*params]
    geom = Geom(pts)
    perimeter = geom.length()
    area = geom.area()
    centroid = geom. centroid()
    print(centroid)


if __name__ == '__main__':
    # test([5, 8], [9, 8])
    test([4, 5], [20, 25], [30, 6])
    test([0, 0], [71, 71], [148, 163], [-25, 263])
    test([1, 3], [4, -3], [-4, -3])
    test([211765, 201564], [211657, 201443],
         [211896, 201887], [211686, 201488], [211765, 201564])
