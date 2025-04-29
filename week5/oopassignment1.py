class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self._pages = pages          
        self.__current_page = 1       

    def read(self):
        print(f"Reading '{self.title}' by {self.author}... Page {self.__current_page}")

    def turn_page(self):
        if self.__current_page < self._pages:
            self.__current_page += 1
        else:
            print("You are at the end of the book!")
    
    def get_current_page(self):
        return self.__current_page


class EBook(Book):
    def __init__(self, title, author, pages, file_size):
        super().__init__(title, author, pages)
        self.file_size = file_size  

    def read(self):
        print(f"Opening eBook '{self.title}' on your device... Page {self.get_current_page()}")



physical_book = Book("Awaken the Giant Within", "Tony Robbins", 304)
ebook = EBook("You Are a Badass", "Jen Sincero", 384, 5.2)


physical_book.read()
physical_book.turn_page()
physical_book.read()

print()

ebook.read()
ebook.turn_page()
ebook.read()