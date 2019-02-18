from app import app
import urllib.request,json
from .models import article
from .models import source

Article = article.Article
Source = source.Source

# Getting api key
api_key = app.config['ARTICLE_API_KEY']


# Getting the article base url
base_url = app.config["SOURCE_API_BASE_URL"]



#get the API key and the source URL

def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)


    return source_results


#process the results and create source objects

    
def process_results(source_list):
    
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category= source_item.get('category')
        country= source_item.get('country')
        language = source_item.get('language')

        if id:
            source_object = Source(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results 



#get the API key and the article URL
# def get_article(category):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_article_url = base_url.format(category,api_key)

#     with urllib.request.urlopen(get_article_url) as url:
#         get_article_data = url.read()
#         get_article_response = json.loads(get_article_data)

#         article_results = Nonearticle

#         if get_article_response['results']:
#             article_results_list = get_article_response['results']
#             article_results = process_results(article_results_list)


#     return article_result


#process the results and create article objects

# def process_results(article_list):
    
#     article_results = []
#     for article_item in article_list:
#         author = article_item.get('author')
#         title = article_item.get('title')
#         description = article_item.get('description')
#         url = article_item.get('url')
#         urlToImage = article_item.get('urlToImage')
#         publishedAt = article_item.get('publishedAt')

#         if poster:
#             article_object = Article(author,title,description,url,urlToImage,publishedAt)
#             article_results.append(article_object)

#     return article_results


 
