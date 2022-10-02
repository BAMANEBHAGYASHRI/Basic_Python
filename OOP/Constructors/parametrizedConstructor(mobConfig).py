class mobile:
    def __init__(self,mobname,version,RAM,ROM):
        self.mobname=mobname
        self.version=version
        self.RAM=RAM
        self.ROM=ROM

    def config(self):
        print("mobile name",self.mobname)
        print("android version",self.version)
        print("RAM,ROM",self.RAM,self.ROM)

object=mobile("Redmi 7A","Android10","2GB","16GM")
object.config()