import random
import math

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
    shortestDistanceSheep: Sheep = entityRepository[0]
    for entity in entityRepository:
        if entity.isAlive:
            entity.distance = round(math.sqrt(pow(entity.getX() - local_wolf.getX(), 2) + pow(entity.getY() - local_wolf.getY(), 2)), 3)
            if entity.distance < shortestDistanceSheep.distance:
                shortestDistanceSheep = entity
    entityRepository.append(local_wolf)
    return shortestDistanceSheep


def simulate_direction():
    return random.choice("NEWS")


def get_sheep_cords(sheep: Sheep, wolf: Wolf):
    wolf.coX = sheep.coX
    wolf.coY = sheep.coY
