class Entity:
    def __init__(self, coX, coY):
        self.coX = coX
        self.coY = coY

    def __eq__(self, other):
        if isinstance(other, Entity):
            return self.coX == other.coX and self.coY == other.coY
        return False
