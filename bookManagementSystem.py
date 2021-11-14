class Book:
    __Slots__ =  ['title', 'author']
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Patron:
    __Slots__ =  ['ID', 'name', 'wantlist']
    def __init__(self, ID, name, wantlist):
        self.ID = ID
        self.name = name
        self.wantlist = wantlist

