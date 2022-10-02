class mobile:
    def __init__(self):
        self.mobname="Redmi 7A"
        self.version="Android10"
        self.RAM="2GB"
        self.ROM="16GM"

    def config(self):
        print("mobile name",self.mobname)
        print("Android version",self.version)
        print("RAM,ROM",self.RAM,self.ROM)

object=mobile()
object.config()