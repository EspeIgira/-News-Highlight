class Article:
    '''
    Article class that defines the article objects
    '''

    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


# 1. Title - The name of the movie
# 2. Overview - A short description on the movie
# 3. image- The poster image for the movie
# 4. vote_average - Average rating of the movie
# 5. vote_count - How many people have rated the movie
# 6. id - The movie id