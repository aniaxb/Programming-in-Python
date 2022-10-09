from project.model.sheep import Sheep
from project.model.wolf import Wolf


def is_coordinate_empty(coX: float, coY: float, entityRepository: list):
    for entity in entityRepository:
        if (coX is entity.coX) and (coY is entity.coY):
            if isinstance(entity, Sheep):
                return not entity.isAlive
            elif isinstance(entity, Wolf):
                return False
    return True