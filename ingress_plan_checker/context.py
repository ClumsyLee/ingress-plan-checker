class Context(object):
    """Context"""
    def __init__(self, portals):
        super(Context, self).__init__()
        self.portals = portals
        self.links = []
        self.fields = []
