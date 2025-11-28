from library import Library

my_library = Library()

while True:
    print("""
1. Add Book
2. Show Books
3. Find Book
4. Remove Book
5. Exit
""")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        title = input("Enter the name of the book: ")
        year = input("Enter the year of publication: ")
        author = input("Enter the name of the author: ")
        my_library.add_book(year, author, title)
    elif choice == 2:
        my_library.show_book()
    elif choice == 3:
        title = input("Enter the name of the book: ")
        my_library.find_book(title)
    elif choice == 4:
        title = input("Enter the name of the book to remove: ")
        my_library.remove_book(title)
    elif choice == 5:
        break
    else:
        print("Please enter a number between 1 and 5")

print("Goodbye! Thanks for using My Library.")
