class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author name={self.name}>"

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list({contract.author for contract in self.contracts()})

    def __repr__(self):
        return f"<Book title={self.title}>"

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = self._validate_author(author)
        self.book = self._validate_book(book)
        self.date = self._validate_date(date)
        self.royalties = self._validate_royalties(royalties)
        Contract.all.append(self)

    @staticmethod
    def _validate_author(author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        return author

    @staticmethod
    def _validate_book(book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        return book

    @staticmethod
    def _validate_date(date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return date

    @staticmethod
    def _validate_royalties(royalties):
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        return royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"<Contract {self.author.name}, {self.book.title}, {self.date}, {self.royalties}>"
