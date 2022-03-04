import math


class Geom(object):
    def __init__(self, args):
        self.pts = []
        self.lines = []
        self.linelength = []
        for arg in args:
            self.pts.append(arg)
        # self.x = None
        # self.y = None
        # self.diffX = None
        # self.diffY = None

    def __str__(self):
        return f'Points {self.pts}'

    def __groupLines(self, ptsLines):
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
            self.lines = [self.lines[0]]
            return self.lines

            # print(line)
        # print(self.lines)
        return self.lines

    def length(self):
        lines = self.__groupLines(self.pts)
        # print(lines)
        for line in lines:
            pt1, pt2 = line

            pt1sq = (pt1[0] - pt2[0])**2
            pt2sq = (pt1[1]-pt2[1])**2
            dist_Line = round(math.sqrt((pt1sq + pt2sq)), 3)
            self.linelength.append(dist_Line)
        # print(self.linelength)
        # print(sum(self.linelength))
        perimeter = sum(self.linelength)
        return perimeter

    def area(self):
        print(self.linelength)

        return 0.0

    def centroid(self):
        return None
