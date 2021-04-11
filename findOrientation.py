"""
Orientation of 3 points is known by slopes:

orientation = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

orientation > 0: Clockwise orientation
orientation < 0: Counterclockwise orientation
orientation = 0: Colinear orientation

"""


class Point:

    points = []

    def __init__(self, xCoordinate, yCoordinate):

        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate

        self.checkDuplicatedPoints()

    def checkDuplicatedPoints(self):

        if (self.xCoordinate, self.yCoordinate) not in self.points:
            self.points.append((self.xCoordinate, self.yCoordinate))
            print(f"Point {(self.xCoordinate, self.yCoordinate)} was read")

        else:
            print(f"{(self.xCoordinate, self.yCoordinate)} Point was already given")


def calculateSlopes(point1, point2, point3):

    try:
        firstSlope = float(
            (point2.yCoordinate - point1.yCoordinate)
            * (point3.xCoordinate - point2.xCoordinate)
        )
        secondSlope = float(
            (point2.xCoordinate - point1.xCoordinate)
            * (point3.yCoordinate - point2.yCoordinate)
        )

        slopeCalcuation = firstSlope - secondSlope

        return slopeCalcuation

    except Exception as e:
        print(e)


def getOrientation(point1, point2, point3):

    slopeCalcuation = calculateSlopes(point1, point2, point3)

    if slopeCalcuation > 0:

        return "Clockwise orientation"

    elif slopeCalcuation < 0:

        return "Counterclockwise orientation"

    else:

        return "Colinear orientation"


if __name__ == "__main__":

    point1 = Point(0, 0)
    point2 = Point(2, 2)
    point3 = Point(3, 1)

    orientation = getOrientation(point1, point2, point3)
    print(orientation)
