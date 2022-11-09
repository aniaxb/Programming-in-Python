import csv
import json
import logging
import os

csv_file_name = 'alive.csv'
json_file_name = 'pos.json'


def check_path(directory):
    if directory:
        logging.debug("Entering a path")
        os.makedirs(directory, exist_ok=True)
        os.chdir(directory)


def save_csv(round_number, sheep_amount, directory):
    try:
        logging.debug("attempting to write values to the file (" + str(round_number) + ", " + str(sheep_amount) + ")")
        column_titles = ['round', 'alive']
        mode = lambda x: 'w' if (x == 1) else 'a'
        with open(csv_file_name, mode=mode(round_number), newline='') as file:
            file_writer = csv.DictWriter(file, fieldnames=column_titles)
            if round_number == 1:
                logging.info("Create a new csv file")
                check_path(directory)
                file_writer.writeheader()
            file_writer.writerow({'round': round_number, 'alive': sheep_amount})
    except IOError as e:
        logging.error("error while trying to save csv file: " + e)


def save_json(round_number, sheep_list, wolf):
    try:
        logging.debug("trying to write data to json")
        simplified_Sheep = list()
        for sheep in sheep_list:
            if sheep.isAlive:
                json_sheep = {
                    "ID": str(sheep.id),
                    "coX": str(round(sheep.coX, 3)),
                    "coY": str(round(sheep.coY, 3))
                }
            else:
                json_sheep = {
                    "ID": str(sheep.id),
                    "coX": "null",
                    "coY": "null"
                }
            simplified_Sheep.append(json_sheep)
        json_message = {
            "round_number": round_number,
            "Sheep": simplified_Sheep,
            "wolf": str(wolf.coX) + ", " + str(wolf.coY)
        }
        data = []
        if round_number != 1:
            with open(json_file_name, "r") as file:
                data = json.load(file)
        data.append(json_message)
        with open(json_file_name, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        logging.error("error while trying to save json file: " + e)
