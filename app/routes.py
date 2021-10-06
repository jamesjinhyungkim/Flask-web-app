from flask import render_template, flash, redirect, url_for
from app import app 
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'James'}
    #username
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Beautiful day in West Hollywood!'
            },
            {
                'author': {'username': 'Susan'},
                'body': 'The Dodgers will beat the Cardinals on wednesday!'
            }     
        
     ]
     #Create fake posts & users
    return render_template('index.html', title='Home', user=user, posts=posts)

# Add Login view Function
@app.route('/login', methods=['GET', 'POST']) 
#Function accepts GET and POST requests
def login():
    form = LoginForm()
    #Validators for login 
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)