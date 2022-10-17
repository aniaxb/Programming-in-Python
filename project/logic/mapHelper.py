import random

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


def detect_nearest_sheep(entityRepository: list):
    local_wolf = entityRepository[len(entityRepository) - 1]
    copy_list = entityRepository
    copy_list.remove(local_wolf)
    for entity in entityRepository:
        print(entity)
    return None


def simulate_direction():
    return random.choice("NEWS")
