class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    
    def add_book(self, book):
        self.books.append(book)
        
        
    def search_books(self, title = None, author = None):
        bookcart = []
        if title == None and author == None:
            return "error"
        elif author == None:
            for i in self.books:
                if title.lower() in i.title.lower():
                    bookcart.append(i)
                    
        elif title == None:
            for i in self.books:
                if i.author == author:
                    bookcart.append(i)
        else:
            for i in self.books:
                if i.author == author and title.lower() in i.title.lower():
                    bookcart.append(i)
                    
        return bookcart
        
    def get_books(self):
        return self.books
        

class Author(object):
    def __init__(self, author, nationality):
        self.name = author
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books
        
        

class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)

