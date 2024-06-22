import json
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from flask import Flask, Blueprint, request, jsonify

# Crear el blueprint
embeddings_bp = Blueprint('embeddings_bp', __name__)

class Embeddings:
    def __init__(self, model_path, dataset_path):
        self.model_path = model_path
        self.dataset_path = dataset_path
        self.model = load_model(self.model_path, custom_objects={'mse': MeanSquaredError()})
        
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
    def predict_ratings_for_new_user(self, userId, new_user_interactions):
        movie_id_mapping = {}
        index_to_movieId = {}
        with open('src/models/data/movieId_to_index_embedding.json', 'r') as file:
            movie_id_mapping = json.load(file)
        with open('src/models/data/index_to_movieId_embedding.json', 'r') as file:
            index_to_movieId = json.load(file)
        movie_id_mapping = {int(movie_id): index for movie_id, index in movie_id_mapping.items()}
        index_to_movieId = {int(index): movie_id for index, movie_id in index_to_movieId.items()}
        
        # Ids de todas las peliculas
        movie_ids = np.arange(10417)
        # Convert the movie IDs to the internal IDs used by the model
        movies_already_seen = []
        for movie_id, rating in new_user_interactions.items():
            index = movie_id_mapping[int(movie_id)]
            movies_already_seen.append(index)
            
        # Filtrar las películas que el usuario ya ha visto
        movie_ids_to_predict = np.setdiff1d(movie_ids, movies_already_seen)
        # Generar predicciones para las películas que el usuario no ha visto
        user_id_array = np.array([userId] * (10417 - len(new_user_interactions)))
        
        predicted_ratings = self.model.predict([user_id_array, movie_ids_to_predict])
        # Ordenar las películas por calificación predicha de mayor a menor y seleccionar los índices de las 10 películas más altas
        #top_recommended_indices = np.argsort(predicted_ratings[:, 0])[-10:][::-1]
        top_indices = np.argsort(predicted_ratings[:, 0])[::-1]
        top_10_indices = top_indices[:10]
        # Convertir los índices de las películas recomendadas a sus IDs originales
        #recommended_movie_ids = [int(index_to_movieId[index]) for index in top_recommended_indices]
        recommended_movie_ids = [index_to_movieId[int(index)] for index in top_10_indices]
        return recommended_movie_ids
    
    def recommend(self, new_user_interactions):
        new_user_interactions = {int(movie_id): rating for movie_id, rating in new_user_interactions.items()}
        recommended_movies = self.predict_ratings_for_new_user(1, new_user_interactions)
        
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
model_path = 'src/models/embeddings.h5'
dataset_path = 'src/models/data/dataset2.json'
recommendation_system = Embeddings(model_path, dataset_path)

@embeddings_bp.route('/embeddings', methods=['POST'])
def recommend():
    new_user_interactions = request.json
    print(new_user_interactions)
    recommendations = recommendation_system.recommend(new_user_interactions)[:8]
    return jsonify(recommendations)
