class Context(object):
    """Context"""
    def __init__(self, portals):
        super(Context, self).__init__()
        self.portals = portals
        self.links = []
        self.fields = []
        self.distance = 0

    def add_link(self, new_link):
        if len(self.links):  # Not first link, need to walk.
            pos_before = self.links[-1].out_po
            pos_now = new_link.out_po
            self.distance += pos_before.distance(pos_now)

        self.links.append(new_link)

        # Add fields here to ensure that we are in a valid state.
        for new_field in new_link.new_fields():
            self.fields.append(new_field)
            new_field.cover(self.portals)
