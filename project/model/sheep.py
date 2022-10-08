from project.model.entity import Entity


class Sheep(Entity):

    def __init__(self, id, coX, coY):
        super().__init__(coX, coY)
        self.id = id
        self.isAlive = True

    def __str__(self):
        return "Sheep[id= " + str(self.id) \
               + ", coX= " + str(self.coX) \
               + ", coY= " + str(self.coY) \
               + ", isAlive= " \
               + str(self.isAlive) \
               + "]"
