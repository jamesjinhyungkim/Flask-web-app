from flask import render_template
from app import app 

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
              {     
        
     ]
     #Create fake posts & users
     return render_template('index.html', title='Home', user=user, posts=posts)     
    
