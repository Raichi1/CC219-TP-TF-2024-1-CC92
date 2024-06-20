from dotenv import load_dotenv
import json
import os
from datetime import datetime
import requests

# ************************************ Load the dataset ************************************ #
def load_dataset():
    load_dotenv()
    with open('../models/data/dataset.json', 'r') as file:
        dataset = json.load(file)
    return dataset

def load_movies():
    movies_dict = dict()
    data = load_dataset()
    for dt_json in data:
        id = int(dt_json['id'])
        movies_dict[id] = dt_json
    return movies_dict

# Api to parse the date
def parse_date(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d")
    return date.strftime("%b %d, %Y")
        
# Conseguir las películas populares
def get_popular_movies():
    # URL de la API y cabeceras de autenticación
    url = 'https://api.themoviedb.org/3/movie/popular?language=en-US&page=1'
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZGQ4YjQ1YjM5NzE0NGRjOTQ5ZDQ1NGFkY2NlMDU3YiIsInN1YiI6IjY2NzIxODJkZGJmMWRhNzk1ZjM0M2M2ZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XUcx3n9aQrpyt4_GLLpFK5EcAS-NzoSZJq_A3v-c_7Y',
        'accept': 'application/json'
    }
    # Realizar la solicitud GET
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        # return cached data
        return None
        
def json_popular_movies():
    movies_data = get_popular_movies()['results']
    return list(
        map(
            lambda movie: {
                "id": movie["id"],
                "title": movie["title"],
                "release_date": parse_date(movie["release_date"]),
                "image": f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
            },
            movies_data,
        )
    )
     