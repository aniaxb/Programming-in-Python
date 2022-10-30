import csv
import logging


def csv_export(round_no, sheep_no):
    logging.debug("csv_export(", round_no, sheep_no, ")")
    if round_no == 1:
        with open('alive.csv', mode='w', newline='') as csv_file:
            fieldnames = ['round', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'round': round_no, 'alive': sheep_no})
    else:
        with open('alive.csv', mode='a', newline='') as csv_file:
            fieldnames = ['round', 'alive']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'round': round_no, 'alive': sheep_no})