import random
from flask import Flask, render_template
from api import api as api_app
from models.rbm import rmb_bp as rbm_model
from utils import load_dataset, json_popular_movies

app = Flask(__name__)

app.register_blueprint(api_app)
app.register_blueprint(rbm_model)

data = load_dataset()
 
@app.route('/')
def home():
    popular_movies = json_popular_movies()
    popular_movies = random.sample(popular_movies, 8)
    return render_template("index.html", popular_movies = popular_movies)

if __name__ == '__main__':
    app.run(debug=True)

