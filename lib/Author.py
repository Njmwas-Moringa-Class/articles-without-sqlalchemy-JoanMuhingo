class Author:
    _all.authors =[]
   def __init__(self, name):
        self._name = name 
        Author._all_authors.append(self)     
        self._articles =[]      


    def get_name(self):

        return self._name
    

    def article(self):

        return self._articles
    

    def magazines(self):
        unique_magazines = set(articles.get_magazine()for article in self ._articles)
        return list(unique_magazines)    

    def write_article(self, magazine, title):
        new_article = Article(self, magazine, title)   
        self._articles.append(new_article)

    def add_article(self, magazine, title):

        new_article = Article(self, magazine, title)
        self._articles.append(new_article)

    def topic_areas(self):

        return list(set(article.get_magazine().get_category() for article in self._articles))    


    def get_all_authours(cls):

        return cls._all_authors
