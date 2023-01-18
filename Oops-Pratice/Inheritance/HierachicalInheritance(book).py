class book:
    def __init__(self):
        self.book="harry potter"
        self.author="j.k.rowling"
        self.price="200"
        self.publisher="bloomsbury"
        self.parts="8"

    def b_details(self):
        print("BookDEtails---","\n",self.book,"\n",self.author,"\n",self.price,"\n",self.publisher,"\n",self.parts)


class bookAuthor(book):
    def __init__(self):
        book.__init__(self)
        self.name="j.k.rowling"
        self.country = "UK"
        self.age = "53"
        self.dob = "23/09/1988"

    def a_details(self):
        print(self.name)


class customer(book):
    def __init__(self):
        book.__init__(self)


    def customerdetails(self):
        print(self.book)
        print(self.author)
        print(self.price)



obj=customer()
obj.customerdetails()





