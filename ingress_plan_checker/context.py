from .field import new_fields

class Context(object):
    """Context"""
    def __init__(self, portals):
        super(Context, self).__init__()
        self.portals = portals
        self.links = []
        self.fields = []

    def add_link(self, new_link):
        self.links.append(new_link)
        self.fields.append(new_fields(context, new_link))
