class Source:
    '''
    Source class that defines source objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        '''
        Function that initiates the source class
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country

        