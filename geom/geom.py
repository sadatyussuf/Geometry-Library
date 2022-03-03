import math


class Geom(object):
    def __init__(self, args):
        self.pts = []
        self.lines = []
        for arg in args:
            self.pts.append(arg)
        # self.x = None
        # self.y = None
        # self.diffX = None
        # self.diffY = None

    def __str__(self):
        return f'Points {self.pts}'

    def groupLines(self, ptsLines):
        for index, pt in enumerate(ptsLines):
            line = []
            line.append(ptsLines[index])
            if index == len(ptsLines)-1:
                line.append(ptsLines[0])
            else:
                line.append(ptsLines[index+1])
            line.reverse()
            self.lines.append(line)

        if len(self.lines) == 2:
            return self.lines[0]

            # print(line)
        # print(self.lines)
        return self.lines

    def length(self):
        lines = self.groupLines(self.pts)
        print(lines)
        return 0.0

    def area(self):
        return 0.0

    def centroid(self):
        return None
