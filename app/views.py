from flask import render_template, redirect, url_for, flash
from app import app
from app.forms import Form, GeminiForm

@app.route('/')
def home():
    form = Form()
    return render_template('home.html', title='Home Page', form=form)

@app.route('/about')
def about():
    form = Form()
    return render_template('home.html', title='Home Page', form=form)