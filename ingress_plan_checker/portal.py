from .link import Link

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

    def __repr__(self):
        return "<Portal %s (%s) at (%s, %s), %s key(s)>" % (
                self.index, self.name, self.x, self.y, self.keys)

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
            return (False, "Portal In Field")
        if len(self.outs) >= 8:
            return (False, "Out Link Limit Reached")

        # Check intersections.
        new_link = Link(self, target)
        for link in context.links:
            if new_link.intersect(link):
                return (False, "Intersects Other Link")

        # Link possible.
        self.outs.append(new_link)
        target.ins.append(new_link)
        target.keys -= 1
        context.add_link(new_link)

        return (True, "Success")
