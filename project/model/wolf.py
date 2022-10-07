class Wolf:
    sheep_counter: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.sheep_counter = 0

    def __str__(self):
        return "Wolf[" \
               + ", x= " + str(self.x) \
               + ", y= " + str(self.y) \
               + ", kills= " + str(self.sheep_counter) \
               + "]"
