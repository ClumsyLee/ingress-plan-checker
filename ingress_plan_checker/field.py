class Field(object):
    """Field"""
    def __init__(self, apexes):
        super(Field, self).__init__()
        self.apexes = apexes
        self.area = abs(
            (apexes[0].x * (apexes[1].y - apexes[2].y) +
             apexes[1].x * (apexes[2].y - apexes[0].y) +
             apexes[2].x * (apexes[0].y - apexes[1].y)) / 2)

    def cover(self, context):
        pass
