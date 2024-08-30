class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.update_authors(self)
        
    @classmethod
    def update_authors(cls, author):
        if isinstance(author, Author):
            cls.all.append(author)
        else:
            raise Exception
        
    def contracts(self):
        all_my_contracts = []
        for contract in Contract.all:
            if contract.author == self:
                all_my_contracts.append(contract)
        return all_my_contracts
    
    def books(self):
        all_my_books = []
        for contract in Contract.all:
            if contract.author == self:
                all_my_books.append(contract.book)
        return all_my_books
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total += contract.royalties
        return total



class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.update_books(self)

    @classmethod
    def update_books(cls, book):
        if isinstance(book, Book):
            cls.all.append(book)
        else:
            raise Exception
        
    def contracts(self):
        all_my_contracts = []
        for contract in Contract.all:
            if contract.book == self:
                all_my_contracts.append(contract)
        return all_my_contracts
    
    def authors(self):
        all_my_authors = []
        for contract in Contract.all:
            if contract.book == self:
                all_my_authors.append(contract.author)
        return all_my_authors


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.update_contracts(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
    
    @classmethod
    def update_contracts(cls, contract):
        if isinstance(contract, Contract):
            cls.all.append(contract)
        else:
            raise Exception
        
    @classmethod
    def contracts_by_date(cls, date):
        contract_list = []
        for contract in cls.all:
            if contract.date == date:
                contract_list.append(contract)
        return contract_list

