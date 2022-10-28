class Entity:
    def __init__(self, coX, coY):
        self.coX = coX
        self.coY = coY

    def getX(self):
        return round(self.coX, 3)

    def getY(self):
        return round(self.coY, 3)