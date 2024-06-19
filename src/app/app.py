import random
from flask import Flask, request, jsonify, render_template
from api import api as api_app
from utils import load_dataset, json_popular_movies


app = Flask(__name__)
#model = load('../models/rbm.h5')

app.register_blueprint(api_app)

data = load_dataset()

@app.route('/test')
def test_movies():
    popular_movies = json_popular_movies()
    popular_movies = random.sample(popular_movies, 8)
    return jsonify(popular_movies)
 
@app.route('/')
def home():
    popular_movies = json_popular_movies()
    # get 8 popular movies random in popular_movies
    popular_movies = random.sample(popular_movies, 8)
    return render_template("index.html", popular_movies = popular_movies)

if __name__ == '__main__':
    app.run(debug=True)

