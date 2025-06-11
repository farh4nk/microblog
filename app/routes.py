from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route('/')
@app.route('/index')

def index():
    #placeholder user
    user = {
        "username": "Bob"
    }
    #placeholder database
    posts = [
        {
            'author': {'username': 'John'},
            'body': "John's post here."
        },
        {
            'author': {'username': 'Susan'},
            'body': "Susan's post here."
        },
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)