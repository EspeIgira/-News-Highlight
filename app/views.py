from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'News Highlight'
    return render_template('index.html',message = message)


    title = 'Home// Our News Info'
    return render_template('index.html', title = title)

#the API call

from .request import get_article


   # Getting general article

    general_article = get_article('general')
    print(general_article)
    title = 'Home// Our News Info' 
    return render_template('index.html', title = title,general = general_article)
