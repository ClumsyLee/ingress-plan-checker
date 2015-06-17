from math import sqrt
from .common import *

class Link(object):
    """Link"""
    def __init__(self, out_po, in_po):
        super(Link, self).__init__()
        self.out_po = out_po
        self.in_po = in_po

        self.length = sqrt((out_po.x - in_po.x)**2 +
                           (out_po.y - in_po.y)**2)

    def __str__(self):
        return "%s => %s" % (out_po.name, in_po.name)

    def intersect(self, other):
        return (ccw(self.out_po, other.out_po, other.in_po) !=
                ccw(self.in_po, other.out_po, other.in_po) and
                ccw(self.out_po, self.in_po, other.out_po) !=
                ccw(self.out_po, self.in_po, other.in_po))

    def new_fields(self):
        pass
