class laptop:
    def __init__(self ,lname,RAM,harddisk,os):
        self.lname=lname
        self.RAM=RAM
        self.harddisk=harddisk
        self.os=os

    def laptopconfig(self):
        print("laptop",self.lname)
        print("RAM",self.RAM)
        print("hard disk",self.harddisk)
        print("operting system",self.os)

object=laptop("Intel core i7 8gen ","8 GB RAM","512 GB HARDDISk","Windows 10 OS")
object.laptopconfig()








