from flask import Flask, render_template
import json
import random

app = Flask(__name__)

#root page
@app.route("/")
@app.route("/home")
def home():
    movie = random_movie().get('title')
    return f'You should watch {movie}'

@app.route("/about")
def about():
    return "About Page"

def load_movies():
    data = []
    with open('movies052019.jl', 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return data 

def random_movie():
    choice = random.choice(data)
    return choice


data = load_movies()
