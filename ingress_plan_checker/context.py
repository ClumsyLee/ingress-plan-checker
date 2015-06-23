class Context(object):
    """Context"""
    def __init__(self, portals):
        super(Context, self).__init__()
        self.portals = portals
        self.links = []
        self.fields = []
        self.distance = 0
        self.ap = 0

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

        self.ap += new_link.ap  # Receive AP here to include AP of fields.

    def teamwork(self, num):
        ap = 0
        avg_ap = self.ap / num
        index = 0

        start_indexes = []
        aps = []

        for i in range(1, num):
            start_indexes.append(index)

            start_ap = ap
            target_ap = avg_ap * i
            while ap < target_ap:
                # Add this link.
                ap += self.links[index].ap
                index += 1
            aps.append(ap - start_ap)

        start_indexes.append(index)  # For the last one.
        aps.append(self.ap - ap)

        return (start_indexes, aps)
