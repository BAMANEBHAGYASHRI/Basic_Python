class book:
    def __init__(self):
        self.book="harry potter"
        self.author="j.k.rowling"
        self.price="200"
        self.publisher="bloomsbury"
        self.parts="8"

    def b_details(self):
        print("BookDEtails---","\n",self.book,"\n",self.author,"\n",self.price,"\n",self.publisher,"\n",self.parts)

    class bookAuthor:
        def __init__(self):
            self.name="j.k.rowling"
            self.country="UK"
            self.age="53"
            self.dob="23/09/1988"
        def a_details(self):
            print("AUthor DTails","\n",self.name,"\n",self.country,"\n",self.age,"\n",self.dob)

obj=book()
obj1=obj.bookAuthor()
obj1.a_details()
print("----------------------------------------")
obj.b_details()
