from math import sqrt
from .common import *
from .field import Field

class Link(object):
    """Link"""
    def __init__(self, out_po, in_po):
        super(Link, self).__init__()
        self.out_po = out_po
        self.in_po = in_po

        self.length = sqrt((out_po.x - in_po.x)**2 +
                           (out_po.y - in_po.y)**2)

    def __str__(self):
        return "%s => %s" % (self.out_po.name, self.in_po.name)

    def intersect(self, other):
        return (ccw(self.out_po, other.out_po, other.in_po) !=
                ccw(self.in_po, other.out_po, other.in_po) and
                ccw(self.out_po, self.in_po, other.out_po) !=
                ccw(self.out_po, self.in_po, other.in_po))

    def new_fields(self):
        choices = set(self.out_po.neighbors + self.in_po.neighbors)

        pos_max = neg_max = 0  # Find the largest field on the each side.
        pos_field = neg_field = None

        for po in choices:
            field = Field(self.out_po, self.in_po, po)
            area = field.signed_area

            if area > pos_max:
                pos_max = area
                pos_field = field
            elif area < neg_max:
                neg_max = area
                neg_field = field

        new_fields = []
        if pos_field:
            new_fields.append(pos_field)
        if neg_field:
            new_fields.append(neg_field)

        return new_fields
