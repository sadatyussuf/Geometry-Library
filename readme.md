# lab 2 - 2D geometry library

    # Geom - base class

    # Point(Geom)
        dim : x:float, y:float

    # LineSegment(Geom)
        components , Point-A .........Point-B

    # LineString(Geom)
        components , [Point-A, Point-B , Point-c, Point-D .......Point-Q]
    # LinearRing(Geom)
        components , [Point-A, Point-B , Point-c, Point-D .......Point-Q, Point-A]
    # Polygon(Geom)
        components , Shell: LinearRing, Holes: [LinearRings]


## method of geometry

    - length
    - area
    - centroid
    - str - output wkt string

# Next

Algorithms & Data Structures
