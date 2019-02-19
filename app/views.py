from flask import render_template
from app import app

from .request import get_source,get_article

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general source
    general_source = get_source('general')
    health_source = get_source('health')
    business_source = get_source('business')
    #print(general_source)
    message = 'News Highlight'
    title = 'Our News Info' 
    return render_template('index.html',message = message,title = title,general = general_source,health = health_source ,business = business_source)

@app.route('/article/<source_id>')
def article(source_id):

    '''
    View root page function that returns the index page and its data
    '''
    # Getting general source
    general_source = get_article(source_id)
    # health_source = get_article('health')
    # business_source = get_article('business')
    #print(general_source)
    message = 'News Highlight'
    title = 'Our News Info' 
    return render_template('articles.html',message = message,title = title,source_id = general_source)
     
     