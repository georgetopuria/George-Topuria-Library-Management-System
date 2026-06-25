#book class, book info here
class Book:
    #create new book
    #axali wigni
    def __init__(self, book_id, title, author, genre, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = True
#qiraoba
#borrowing
    def borrow_book(self):
        self.available = False
#returning books
    def return_book(self):
        self.available = True
#availability checj
    def get_status(self):
        if self.available:
            return "available"
        return "BOrrowed"
#layout
    def to_csv_row(self):
        return [
            self.book_id,
            self.title,
            self.author,
            self.genre,
            self.year,
            self.available
        ]

    def __str__(self):
        return (
            "ID: " + str(self.book_id) +
            " | Title: " + self.title +
            " | author: " + self.author +
            " | genre: " + self.genre +
            " | Year: " + str(self.year) +
            " | status: " + self.get_status()
        )