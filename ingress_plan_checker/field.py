class Field(object):
    """Field"""
    def __init__(self, apexes):
        super(Field, self).__init__()
        self.apexes = apexes

        self.signed_area = (
            apexes[0].x * (apexes[1].y - apexes[2].y) +
            apexes[1].x * (apexes[2].y - apexes[0].y) +
            apexes[2].x * (apexes[0].y - apexes[1].y)) / 2
        self.area = abs(self.signed_area)

    def cover(self, context):
        """Cover portals in the context"""
        for po in context.portals:
            if (not po.in_field and self.contains(po)):
                po.in_field = True

    def contains(self, portal):
        """Check whether a portal is inside this field"""
        # Using barycentric coordinates.
        # Algorithm from http://stackoverflow.com/questions/2049582/
        #                how-to-determine-a-point-in-a-triangle.
        # Thanks Andreas Brinck & andreasdr.
        s = 1 / (2 * self.signed_area) * (
            portal.x * (apexes[2].y - apexes[0].y) +
            apexes[0].x * (portal.y - apexes[2].y) +
            apexes[2].x * (apexes[0].y - portal.y))

        s = 1 / (2 * self.signed_area) * (
            portal.x * (apexes[0].y - apexes[1].y) +
            apexes[0].x * (apexes[1].y - portal.y) +
            apexes[1].x * (portal.y - apexes[0].y))

        return s > 0 and t > 0 and 1 - s - t > 0

def new_fields(context, new_link):
    pass

