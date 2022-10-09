class addition:
    def __init__(self):
        self.x=10
        self.y=60
    def sum(self):
        print("addition of x and y-",self.x+self.y)

    class division:
        def __init__(self):
            self.a=3
            self.b=9

        def div(self):
            print("division of a and b- ",self.a/self.b)

obj=addition()
a=obj.division()
a.div()