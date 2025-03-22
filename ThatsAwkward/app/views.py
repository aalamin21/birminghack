from flask import render_template, redirect, url_for, flash
from app import app

@app.route('/')
def home():
    return render_template('home.html')