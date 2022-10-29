class Entity:
    def __init__(self, coX, coY):
        self.coX = coX
        self.coY = coY

    def get_x(self):
        return round(self.coX, 3)

    def get_y(self):
        return round(self.coY, 3)