# triplet-points-geometric-orientation
Get the geometric orientation of a set of 3 points

Finding the orientation of given points is the basic for geometric algorithms such as Jarvis and the intersection of 2 lines.
The orientation is found by the slopes among the points:

Slope of a created line between Point1 and Point2: (y2 - y1)/(x2 - x1)
Slope of a created line between Point2 and Point3: (y3 - y2)/(x3 - x2)

# orientation = (y2 - y1)*(x3 - x2) - (y3 - y2)*(x2 - x1)

orientation > 0: Clockwise orientation
orientation < 0: Counterclockwise orientation
orientation = 0: collinear orientation
