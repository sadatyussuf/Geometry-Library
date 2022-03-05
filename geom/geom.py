import math


class Geom(object):
    def __init__(self, args=None):
        self.coordinates = []
        self.lines = []
        self.linelength = []
        self.Northerns = []
        self.Easterns = []
        if args is not None:
            for arg in args:
                self.coordinates.append(arg)

    def __str__(self):
        return f'Points {self.pts}'

    def __groupCoords(self, coords):
        for index, item in enumerate(coords):
            self.Northerns.append(item[0])
            self.Easterns.append(item[1])
            # print(item)
        self.Northerns.append(self.Northerns[0])
        self.Easterns.append(self.Easterns[0])
        print(f'N={self.Northerns}, E={self.Easterns}')

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
        return self.lines

    def length(self):
        lines = self.__groupLines(self.coordinates)
        for line in lines:
            pt1, pt2 = line
            pt1sq = (pt1[0] - pt2[0])**2
            pt2sq = (pt1[1]-pt2[1])**2
            dist_Line = round(math.sqrt((pt1sq + pt2sq)), 3)
            self.linelength.append(dist_Line)
        perimeter = sum(self.linelength)
        perimeter = round(perimeter, 3)
        return perimeter

    def area(self):
        self.__groupCoords(self.coordinates)
        leftSide = []
        rightSide = []
        for i in range(len(self.Northerns)-1):
            leftSide.append(self.Northerns[i] * self.Easterns[i+1])
            rightSide.append(self.Easterns[i] * self.Northerns[i+1])

        sumLeftSide = sum(leftSide)
        sumRightSide = sum(rightSide)

        diffSides = (sumLeftSide - sumRightSide)
        area = abs(round((diffSides/2), 3))
        print(area)

        return area

    def centroid(self):
        centroid = []
        print(len(self.Northerns[:-1]))
        Ox = sum(self.Northerns[:-1])/len(self.Northerns[:-1])
        Oy = sum(self.Easterns[:-1])/len(self.Northerns[:-1])

        centroid.append(round(Ox, 2))
        centroid.append(round(Oy, 2))
        # centroid.append(Oy)
        # print(centroid)
        return centroid
