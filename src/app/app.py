from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from api import api as api_app
import numpy as np

app = Flask(__name__)
#model = load('../models/rbm.h5')

app.register_blueprint(api_app)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)

