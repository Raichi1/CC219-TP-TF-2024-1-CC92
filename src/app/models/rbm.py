import os
import json
import numpy as np
from tensorflow.keras.models import load_model

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import load_movies


# Cargar el modelo RBM preentrenado
path_model = '../../models/rbm.h5'  # Ajusta la ruta según sea necesario
rbm_model = load_model(path_model)

# Suponiendo que tienes las matrices de embeddings ya extraídas
weights_hidden_layer = rbm_model.layers[1].get_weights()[0]  # Pesos entre la capa visible y la capa oculta
weights_visible_layer = rbm_model.layers[2].get_weights()[0]  # Pesos entre la capa oculta y la capa visible

user_embedding = weights_hidden_layer.T  # Transponer para obtener la matriz de embeddings de usuarios
item_embedding = weights_visible_layer  # Matriz de embeddings de elementos/películas

def predict_ratings_for_new_user(new_user_interactions):
    # Crear un vector para el nuevo usuario con sus interacciones
    new_user_vector = np.zeros((1, user_embedding.shape[1]))  # Asumiendo que el número de usuarios es la dimensión correcta
    print(len(new_user_vector[0]))
    for movie_id, rating in new_user_interactions.items():
        new_user_vector[0, movie_id] = rating  # -1 porque los índices comienzan desde 0
    
    # Hacer predicciones multiplicando los embeddings
    predicted_ratings = np.dot(user_embedding, new_user_vector[0])
    
    # Ordenar las películas por las predicciones de calificación (en orden descendente)
    recommended_movies = np.argsort(predicted_ratings)[::-1]
    
    return recommended_movies

# Ejemplo de uso:
new_user_interactions = {
    5: 4,   # El nuevo usuario dio una calificación de 4.0 a la película con movieId 5
    79: 3, # Calificación de 3.5 para la película con movieId 869, etc.
    25: 2,
    43: 4,
    58: 1
}

movies = load_movies()
recommended_movies = predict_ratings_for_new_user(new_user_interactions)
print("Películas recomendadas para el nuevo usuario:")

cont = 0
print(len(recommended_movies))
for movie_id in recommended_movies:  # Mostrar las primeras 10 recomendaciones
    if cont == 10:
        break
    if movie_id in movies :
        print(f"MovieID: {movies[movie_id]['title']}") 
        cont += 1
