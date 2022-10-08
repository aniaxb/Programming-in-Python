from project.model.Sheep import Sheep
from project.model.Wolf import Wolf


class MapHelper:
    @staticmethod
    def isCoordinateFree(coX: float, coY: float, entityRepository: list):
        for entity in entityRepository:
            if (coX is entity.coX) and (coY is entity.coY):
                if isinstance(entity, Sheep):
                    return not entity.isAlive
                elif isinstance(entity, Wolf):
                    return False
        return True
