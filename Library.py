
class Book:
    def __init__(self, year, author, title):
        self.year = year
        self.author = author
        self.title = title
    
class Library:
    
    def __init__(self):
        self.books = []
    
    
    def add_book(self, year, author, title):
        new_book = Book(year ,author ,title)
        self.books.append(new_book)
        
    
    def show_book(self):
        for book in self.books:
            print(f"It is {book.title}, published in {book.year} and the auther is {book.author}.")
        
        
        
    def find_book(self, title):
        found = False
        
        for book in self.books:
            if title.lower() == book.title.lower():
                print("It already exists i library")
                found = True
                break
            
        if not found:
                print("This book does'nt exist in the library")
    
    
    
    
    def remove_book(self, title):
        found = False
                          
        for book in self.books:
              if book.title.lower() == title.lower():
                  self.books.remove(book)
                  print("book is removed")
                  found = True
                  break
              
        if not found:
                  print("I did'nt found any book like this")
                  
                  

       
            
    

