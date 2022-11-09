from chase.model.entity import Entity


class Sheep(Entity):
    _id_iterator: int = 0

    def __init__(self, coX, coY):
        super().__init__(coX, coY)
        self.distance = 0
        self.id = self.get_new_id()
        self.isAlive = True

    def __str__(self):
        return "Sheep[id= " + str(self.id) \
               + ", coX= " + str(round(self.coX, 3)) \
               + ", coY= " + str(round(self.coY, 3)) \
               + ", isAlive= " \
               + str(self.isAlive) \
               + "]"

    @classmethod
    def get_new_id(cls):
        cls._id_iterator += 1
        return cls._id_iterator
