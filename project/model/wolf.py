from project.model.entity import Entity


class Wolf(Entity):

    def __init__(self, coX, coY):
        super().__init__(coX, coY)
        self.sheep_counter = 0

    def __str__(self):
        return "Wolf[" \
               + "coX= " + str(round(self.coX, 3)) \
               + ", coY= " + str(round(self.coY, 3)) \
               + ", kills= " + str(self.sheep_counter) \
               + "]"
