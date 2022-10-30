import csv
import logging

from project.exceptions.exceptions import file_exception

filename = 'alive.csv'


def save_csv(round_number, sheep_amount):
    try:
        logging.debug("attempting to write values to the file (" + str(round_number) + ", " + str(sheep_amount) + ")")
        column_titles = ['round', 'alive']
        if round_number == 1:
            logging.debug("Create a new file")
            with open(filename, mode='w', newline='') as file:
                file_writer = csv.DictWriter(file, fieldnames=column_titles)
                file_writer.writeheader()
                file_writer.writerow({'round': round_number, 'alive': sheep_amount})
        else:
            with open(filename, mode='a', newline='') as file:
                file_writer = csv.DictWriter(file, fieldnames=column_titles)
                file_writer.writerow({'round': round_number, 'alive': sheep_amount})
    except IOError:
        raise file_exception()
