class Link(object):
    """Link"""
    def __init__(self, out_po, in_po):
        super(Link, self).__init__()
        self.out_po = out_po
        self.in_po = in_po

    def __str__(self):
        return "%s => %s" % (out_po.name, in_po.name)

    def intersect(self, other):
        pass
