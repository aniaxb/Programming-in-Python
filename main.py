from project.factories.SheepFactory import SheepFactory
from project.model.Sheep import Sheep

if __name__ == '__main__':
    # sample = Sheep(1, 2.0, 3.0)
    # print(sample.__str__())

    factory = SheepFactory()
    factory.createSheep(5)