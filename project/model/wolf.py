from project.model.entity import Entity


class Wolf(Entity):

    def __init__(self, coX, coY):
        super().__init__(coX, coY)
        self.sheep_counter = 0

    def __str__(self):
        return "Wolf[" \
               + ", coX= " + str(self.coX) \
               + ", coY= " + str(self.coY) \
               + ", kills= " + str(self.sheep_counter) \
               + "]"
