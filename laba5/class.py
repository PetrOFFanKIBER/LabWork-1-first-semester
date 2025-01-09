class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def get_unfo(self):
        return "Название книги:{}, Автор: {}, Год издания: {}".format(self.title, self.author, self.year)
        
literature = Book('Война и мир','Л. Н. Толстой', 1873)
print(literature.get_unfo())
        