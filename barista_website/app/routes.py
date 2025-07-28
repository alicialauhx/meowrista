from app import app
# from app.models import User, Messages
# from app.forms import LoginForm, RegisterForm, FindForm, ResetForm
from flask import render_template, flash, redirect, url_for, request
# from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.urls import url_parse
# import sqlite3 as sql

##### main website #######
@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template("home.html")

##### About Matcha ############
@app.route('/about_matcha', methods = ['GET', 'POST'])
def about_matcha():
    return render_template("about_matcha.html")

##### Drink preparation tips ############
@app.route('/drink_preparation_tips', methods = ['GET', 'POST'])
def drink_prep_tips():
    return render_template("drink_prep_tips.html")

#### Recipes page #####
@app.route('/recipes', methods = ['GET', 'POST'])
def recipes():
    return render_template('recipes.html')

#### Drink recipes page #####
@app.route('/recipes/<name>', methods = ['GET', 'POST'])
def recipes_name(name):
    return render_template(f'{name}.html', name=name)