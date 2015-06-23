from math import sqrt
from .common import *
from .field import Field

class Link(object):
    AP = 313

    """Link"""
    def __init__(self, out_po, in_po):
        super(Link, self).__init__()
        self.out_po = out_po
        self.in_po = in_po

        self.length = sqrt((out_po.x - in_po.x)**2 +
                           (out_po.y - in_po.y)**2)

        self.ap = self.AP

    def __repr__(self):
        return "<link from %s to %s, %s AP>" % (self.out_po.index,
                                                self.in_po.index,
                                                self.ap)

    def intersect(self, other):
        if ({self.in_po, self.out_po} &
            {other.in_po, other.out_po}):
            return False  # Share a portal.

        return (ccw(self.out_po, other.out_po, other.in_po) !=
                ccw(self.in_po, other.out_po, other.in_po) and
                ccw(self.out_po, self.in_po, other.out_po) !=
                ccw(self.out_po, self.in_po, other.in_po))

    def new_fields(self):
        choices = set(self.out_po.neighbors) & set(self.in_po.neighbors)

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

        # Receive APs.
        self.ap += Field.AP * len(new_fields)

        return new_fields
