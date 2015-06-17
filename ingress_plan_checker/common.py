SUCCESS = 0
PORTAL_IN_FIELD = 1
OUT_LINK_LIMIT_REACHED = 2
INTERSECT_OTHER_LINK = 3

def ccw(a, b, c):
    return (c.y - a.y) * (b.x - a.x) > (b.y - a.y) * (c.x - a.x)
