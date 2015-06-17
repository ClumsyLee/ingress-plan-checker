class Portal(object):
    """Portal"""
    def __init__(self, x, y, index, name="NO NAME", key=0):
        super(Portal, self).__init__()
        self.x = x
        self.y = y
        self.index = index
        self.name = name
        self.key = key

        # In links & out links.
        self.ins = []
        self.outs = []

        self.in_field = False

    def link(self, context, target):
        pass
