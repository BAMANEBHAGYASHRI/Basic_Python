class laptop:
    def __init__(self):
        self.lname="Intel core i7 8gen "
        self.RAM="8 GB RAM"
        self.harddisk="512 GB HARDDISk"
        self.os="Windows 10 OS"

    def laptopconfig(self):
        print("laptop",self.lname)
        print("RAM",self.RAM)
        print("hard disk",self.harddisk)
        print("operting system",self.os)

object=laptop()
object.laptopconfig()








