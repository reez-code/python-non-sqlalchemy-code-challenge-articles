class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
            
    @property 
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if(hasattr(self, "title")):
            print("Already Exists")
        else:
            if isinstance(title, str) and 5 <= len(title) <= 50:
                self._title = title

    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine




class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if(hasattr(self, "name")):
            print("Already Exists")
        else:
             if isinstance(name, str) and len(name) > 0:
                  self._name = name

    
    def articles(self):
        return [article for article in Article.all if article.author == self._name]
    
    
    
    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

   
    
   