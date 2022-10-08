from project.logic.gameSimulation import GameSimulation

if __name__ == '__main__':
    game = GameSimulation(10, 15, 0.5, 1)
    game.start_simulation(200)

