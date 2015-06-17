class Context(object):
    """Context"""
    def __init__(self, portals):
        super(Context, self).__init__()
        self.portals = portals
        self.links = []
        self.fields = []

    def add_link(self, new_link):
        self.links.append(new_link)

        # Add fields here to ensure that we are in a valid state.
        for new_field in new_link.new_fields():
            self.fields.append(new_field)
            new_field.cover(self.portals)
