import json
import numpy as np
from tensorflow.keras.models import load_model
from flask import Flask, Blueprint, request, jsonify

# Crear el blueprint
rmb_bp = Blueprint('rmb_bp', __name__)

class RecommendationSystem:
    def __init__(self, model_path, dataset_path):
        self.model_path = model_path
        self.dataset_path = dataset_path
        self.rbm_model = load_model(self.model_path)
        
        # Extraer los pesos del modelo
        self.weights_hidden_layer = self.rbm_model.layers[1].get_weights()[0]
        self.weights_visible_layer = self.rbm_model.layers[2].get_weights()[0]
        
        self.user_embedding = self.weights_hidden_layer.T
        self.item_embedding = self.weights_visible_layer
        
        self.movies = self._load_movies()

    def _load_dataset(self):
        with open(self.dataset_path, 'r') as file:
            dataset = json.load(file)
        return dataset

    def _load_movies(self):
        movies_dict = {}
        data = self._load_dataset()
        for dt_json in data:
            id = int(dt_json['id'])
            movies_dict[id] = dt_json
        return movies_dict
    
    # Function to predict ratings for a new user
    def predict_ratings_for_new_user(self, new_user_interactions):
        # Create a new user vector
        new_user_vector = np.zeros((1, self.user_embedding.shape[1]))
        
        movieId_to_index = {}
        index_to_movieId = {}
        with open('../models/data/movieId_to_index.json', 'r') as file:
            movieId_to_index = json.load(file)
        with open('../models/data/index_to_movieId.json', 'r') as file:
            index_to_movieId = json.load(file)
            
        # TRANSFORM movieId_to_index IN A MAP
        movieId_to_index = {int(movie_id): index for movie_id, index in movieId_to_index.items()}
        index_to_movieId = {int(index): movie_id for index, movie_id in index_to_movieId.items()}
        
        seen_movies_indices = set()
        
        for movie_id, rating in new_user_interactions.items():
            index = movieId_to_index[movie_id]
            new_user_vector[0, index] = rating > 0
            # Save the indices of the movies that the user has seen
            if rating > 0:
                seen_movies_indices.add(index)
        
        # Multiply the user vector with the item embeddings to get the predicted ratings
        predicted_ratings = np.dot(self.user_embedding, new_user_vector[0])
        # Argsort to get the indices of the movies with the highest predicted ratings
        recommended_movies = np.argsort(predicted_ratings)[::-1]
        # Convert the indices of user_matrix_binary to movieId and verify if the movie has been seen by the user
        recommended_movie_ids = [index_to_movieId[index] for index in recommended_movies if index not in seen_movies_indices]
        return recommended_movie_ids
    
    def recommend(self, new_user_interactions):
        new_user_interactions = {int(movie_id): rating for movie_id, rating in new_user_interactions.items()}
        recommended_movies = self.predict_ratings_for_new_user(new_user_interactions)
        
        recommendations = []
        cont = 0

        for movie_id in recommended_movies:
            if cont == 10:
                break
            if movie_id in self.movies:
                recommendations.append(
                    {"movie_id": self.movies[movie_id]['id'], 
                    "title": self.movies[movie_id]['title'], 
                    "date": self.movies[movie_id]['release_date'],
                    "poster": self.movies[movie_id]['poster_path']
                    })
                cont += 1
        
        return recommendations

# Crear una instancia de la clase RecommendationSystem
model_path = '../models/rbm.h5'
dataset_path = '../models/data/dataset2.json'
recommendation_system = RecommendationSystem(model_path, dataset_path)

@rmb_bp.route('/recommend', methods=['POST'])
def recommend():
    new_user_interactions = request.json
    recommendations = recommendation_system.recommend(new_user_interactions)[:8]
    return jsonify(recommendations)
