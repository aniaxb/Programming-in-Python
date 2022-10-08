class Sheep:
    isAlive: bool
    
    def __init__(self, id, coX, coY):
        self.id = id
        self.coX = coX
        self.coY = coY

    def __str__(self):
        return "Sheep[id= " + str(self.id) \
               + ", coX= " + str(self.coX) \
               + ", coY= " + str(self.coY) \
               + ", isAlive= " \
               + str(self.isAlive) \
               + "]"
