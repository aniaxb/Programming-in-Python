import random

from project.exceptions.exceptions import sheep_viability_exception
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


def calculate_distances(entityRepository: list):
    local_wolf: Wolf = entityRepository[len(entityRepository) - 1]
    if local_wolf.sheep_counter == len(entityRepository) - 1:
        raise sheep_viability_exception()
    entityRepository.remove(local_wolf)
    for entity in entityRepository:
        if entity.isAlive:
            entity.distance = 1
    entityRepository.append(local_wolf)


def simulate_direction():
    return random.choice("NEWS")


def get_sheep_cords(sheep: Sheep, wolf: Wolf):
    wolf.coX = sheep.coX
    wolf.coY = sheep.coY
    print(str(sheep.coX) + " " + str(sheep.coY))
