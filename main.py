from project.logic.GameSimulation import GameSimulation

if __name__ == '__main__':
    game = GameSimulation(10, 15, 0.5, 1)
    game.startSimulation(200)

