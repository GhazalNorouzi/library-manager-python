"""
پروژه: مدیریت کتابخانه شخصی
هدف: کار با کلاس‌ها، متدها، لیست‌ها و دیکشنری‌ها.
کلاس Book بساز که ویژگی‌هایی مثل title, author, year داشته باشه.
کلاس Library بساز که لیست کتاب‌ها رو نگه داره و متدهای اضافه کردن، حذف کردن، و جستجو داشته باشه.
کاربر از طریق ترمینال می‌تونه کتاب اضافه کنه یا جستجو کنه.
راهنمایی برای شروع:
اول کلاس Book بساز با __init__ برای ویژگی‌ها.
بعد کلاس Library بساز و یک لیست خالی برای کتاب‌ها تعریف کن.
متد add_book بنویس که یک کتاب جدید به لیست اضافه کنه.
برای جستجو، یک متد بساز که روی لیست کتاب‌ها بگرده و کتاب‌ها با عنوان مشخص رو برگردونه
"""

class Book:
    def __init__(self, year, auther, title):
        self.year = year
        self.auther = auther
        self.title = title
    
class Library:
    
    def __init__(self):
        self.books = []
    
    
    def add_book(self, year, auther, title):
        new_book = Book(year ,auther ,title)
        self.books.append(new_book)
        
    
    def show_book(self):
        for book in self.books:
            print(f"It is {book.title}, published in {book.year} and the auther is {book.auther}.")
        
        
        
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
                  
                  
my_library = Library()

while True:
    print("""
          1. Add Book
          2. Show Books
          3. Find Book
          4. Remove Book
          5. Exit
          """)
    choice =input("please enter your choice:")
    if choice.isdigit():
        choice = int(choice)


        if 1 <=choice <= 5:
            if choice == 1:
                title = input("please enter the name of the book:")
                year = input("please enter the year of pubkish:")
                auther = input("please write the name of the auther:")
                my_library.add_book(year, auther, title)
            elif choice == 2:
                my_library.show_book()
            elif choice == 3:
                title = input("please enter the name of the book:")
                my_library.find_book(title)
            elif choice == 4:
                title = input("please enter the name of the book:")
                my_library.remove_book(title)
            elif choice == 5:
                break
        else:
            print("please enter a number")
            
    else:
        print("you didn't enter a number!")
            
        
            
    
