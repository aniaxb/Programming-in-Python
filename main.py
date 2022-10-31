import logging
import argparse

from project.logic.gameSimulation import GameSimulation


def is_positive(value):
    local_value = int(value)
    if local_value <= 0:
        raise argparse.ArgumentTypeError("%s the value cannot be less than 0" % local_value)
    logging.debug("the value entered ", value, " is positive")
    return local_value


def parameter_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help="an auxiliary configuration file", action='store', dest='config',
                        metavar='FILE')
    parser.add_argument('-d', '--dir', action='store', help="subdirectory where files should be placed",
                        dest='directory', metavar='DIR')
    parser.add_argument('-l', '--log', action='store', help="events logged level", dest='logger_lvl',
                        metavar='LEVEL')
    parser.add_argument('-r', '--rounds', action='store', help=" the number of rounds", dest='round_number',
                        type=is_positive, metavar='NUM')
    parser.add_argument('-s', '--sheep', action='store', help="the number of sheep in a flock",
                        dest='sheep_number', type=is_positive, metavar='NUM')
    parser.add_argument('-w', '--wait', action='store_true',
                        help="if simulation should be paused at the end of each round", dest='wait')
    return parser.parse_args()


def main():
    number_of_sheep = 15
    number_of_rounds = 50
    init_pos_limit: 10.0
    sheep_move_dist: 0.5
    wolf_move_dist: 1.0
    wait = False
    directory = None

    args = parameter_parser()
    print(args.wait)

    logging.basicConfig(level=logging.INFO)
    # game = GameSimulation(init_pos_limit, number_of_sheep, sheep_move_dist, wolf_move_dist, wait, directory)
    # game.start_simulation(number_of_rounds)


if __name__ == '__main__':
    main()
