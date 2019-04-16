from flask import render_template
from flask import Flask
from tinydb import TinyDB
import random

app = Flask(__name__)
db = TinyDB('db.json')
recipes = db.all()


@app.route('/')
def index():
    # breakpoint()    
    recipe = random.choice(recipes)
    return render_template('recipe.html', context=recipe)

