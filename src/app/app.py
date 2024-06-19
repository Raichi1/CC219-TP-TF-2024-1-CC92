from flask import Flask, request, jsonify, render_template
from api import api as api_app
from utils import load_dataset, json_popular_movies


app = Flask(__name__)
#model = load('../models/rbm.h5')

app.register_blueprint(api_app)

data = load_dataset()
 
@app.route('/')
def home():
    popular_movies = json_popular_movies()
    popular_movies = popular_movies[:8]
    return render_template("index.html", popular_movies = popular_movies)

if __name__ == '__main__':
    app.run(debug=True)

