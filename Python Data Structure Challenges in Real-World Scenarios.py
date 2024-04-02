#Question 2 
#Task 1
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def add_book(library, book_name, author):
    for books in library:
        if book_name.lower() == books[0].lower():
            exist = True
            print(f"{book_name.title()} is already in the Library.")
            break
        else:
            exist= False 
    if not exist:
        library.append((book_name.title(), author.title()))
        print(f"{book_name.title()} has been added to the Library.")

        


add_book(library, "brave new world", "B")
add_book(library, "1984", "George Orwell")
add_book(library, "the alchemist", "Paulo Coelho")
print(library)