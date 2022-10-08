class Wolf:
    sheep_counter: int

    def __init__(self, coX, coY):
        self.coX = coX
        self.coY = coY
        self.sheep_counter = 0

    def __str__(self):
        return "Wolf[" \
               + ", coX= " + str(self.coX) \
               + ", coY= " + str(self.coY) \
               + ", kills= " + str(self.sheep_counter) \
               + "]"
