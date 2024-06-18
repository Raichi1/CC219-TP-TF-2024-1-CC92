from dotenv import load_dotenv
import json
import os

# ************************************ Load the dataset ************************************ #
def load_dataset():
    load_dotenv()
    DATASET_PATH = os.getenv('DATASET_PATH', '../models/data/dataset.json')
    with open(DATASET_PATH, 'r') as file:
        dataset = json.load(file)
    return dataset

def load_movies():
    movies_dict = dict()
    data = load_dataset()
    for dt_json in data:
        id = int(dt_json['id'])
        movies_dict[id] = dt_json
    return movies_dict