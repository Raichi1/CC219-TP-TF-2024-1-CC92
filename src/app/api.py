from flask import Flask, Blueprint, request, jsonify
from utils import load_dataset, load_movies
import json
import os

api = Blueprint('api', __name__)

# Load the dataset

# Load the movies dictionary
# movies = load_movies()

# ************************************ API Endpoints ************************************ #
# Api endpoint to get the dataset
@api.route('/api', methods=['GET'])
def get_dataset():
    data = load_dataset()
    dataset = data[:10]
    return jsonify(dataset)

# Api endpoint to get the dataset by id
@api.route('/api/<int:id>', methods=['GET'])
def get_dataset_by_id(id):
    data = load_dataset()
    for dt_json in data[:10]:
        if dt_json['id'] == id:
            return jsonify(dt_json)
    return jsonify({'message': 'data not found'})
