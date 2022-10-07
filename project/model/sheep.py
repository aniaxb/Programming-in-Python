class Sheep:
    isAlive: bool

    def __init__(self, id, x, y):
        self.id = id+1
        self.x = x
        self.y = y
        self.isAlive = True

    def __str__(self):
        return "Sheep[id= " + str(self.id) \
               + ", x= " + str(self.x) \
               + ", y= " + str(self.y) \
               + ", isAlive= " \
               + str(self.isAlive) \
               + "]"
