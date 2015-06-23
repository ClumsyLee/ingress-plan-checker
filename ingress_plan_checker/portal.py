from .link import Link
from .common import *

class Portal(object):
    """Portal"""
    def __init__(self, x, y, index, name="NO NAME", keys=0):
        super(Portal, self).__init__()
        self.x = x
        self.y = y
        self.index = index
        self.name = name
        self.keys = keys

        # In links & out links.
        self.ins = []
        self.outs = []

        self.in_field = False

    @property
    def neighbors(self):
        ns = []
        for l in self.ins:
            ns.append(l.out_po)
        for l in self.outs:
            ns.append(l.in_po)

        return ns

    def link(self, context, target):
        if self.in_field:
            return PORTAL_IN_FIELD
        if len(self.outs) >= 8:
            return OUT_LINK_LIMIT_REACHED

        # Check intersections.
        new_link = Link(self, target)
        for link in context.links:
            if new_link.intersect(link):
                return INTERSECT_OTHER_LINK

        # Link possible.
        self.outs.append(new_link)
        target.ins.append(new_link)
        target.keys -= 1
        context.add_link(new_link)

        return SUCCESS
