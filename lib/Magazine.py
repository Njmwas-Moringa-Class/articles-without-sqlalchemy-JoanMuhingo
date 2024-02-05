class Magazine:

    all.magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        self._articles = []
        Magazine._all_magazines.append(self)


    def get_name(self):    
        
        return self.name

    def get_category(self):   

        return self.category

    
    def contributors(self):
        
        return self._contributors

    def add_contributors(self, author):

        if author not in self.add_contributors:
            self.add_contributors.append(author)    
    
    @classmethod
    def find_by_name(cls, name):

        for magazine in cls.get_all_magazines:
            if magazine.get_name() == name:
                return magazine
        return None        

    @classmethod
    def article_titles(cls):

        all_titles= []
        for magazine in cls.get_all_magazines:
            all_titles.extend(article.get_title() for article in magazine._articles)
        return all_titles

    def contributing_authors(self):

        authours_count ={}   
        for articles in self._articles:
            author = article.get.author()     
            authors_count[author] = authors_count.get(author, 0) + 1

        return [author for author, count in author_count.items()if count > 2]    
    
    @classmethod
    def get_all_magazines(cls):  

        return cls.all_magazines