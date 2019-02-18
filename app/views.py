from flask import render_template
from app import app

from .request import get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general source
    general_source = get_source('general')
    upcoming_source = get_source('upcoming')
    now_showing_source = get_source('now_playing')
    #print(general_source)
    message = 'News Highlight'
    title = 'Our News Info' 
    return render_template('index.html',message = message,title = title,general = general_source,upcoming = upcoming_source,now_showing = now_showing_source)

    