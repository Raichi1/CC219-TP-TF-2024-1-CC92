from flask import Flask, Blueprint, request, jsonify
from utils import load_dataset, load_movies, json_popular_movies
import json
import os
import random

api = Blueprint('api', __name__)

# Load the dataset
data = load_dataset()

# Load the movies dictionary
movies = load_movies()
    
# ************************************ API Endpoints ************************************ #
# Api endpoint to get the dataset
@api.route('/api', methods=['GET'])
def get_dataset():
    dataset = data[:50]
    return jsonify(dataset)

# Api endpoint to get the dataset by id
@api.route('/api/<int:id>', methods=['GET'])
def get_dataset_by_id(id):
    if movies[id] is not None:
        return jsonify(movies[id])
    return jsonify({'message': 'data not found'})

@api.route('/api/movies', methods=['GET'])
def test_movies():
    popular_movies = json_popular_movies()
    popular_movies = random.sample(popular_movies, 8)
    return jsonify(popular_movies)