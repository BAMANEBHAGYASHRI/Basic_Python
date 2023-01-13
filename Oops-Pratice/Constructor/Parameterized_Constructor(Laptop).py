class laptop:
    def __init__(self):
        print("---------LAPTOP CONFIGURATION-----------")
        self.processor="Intel Core i5 (sixth generation or newer) or equivalent"
        self.os="Microsoft Windows 10 Professional x64"
        self.ram="16 GB RAM"
        self.storge="500 GB internal storage drive"
        self.display="14 LCD monitor, resolution of 1600 x 900 or better"
        self.network="802.11ac 2.4/5 GHz wireless adapter"
        self.other="Internal or external Webcam, lock, carrying case, external hard drive for backups"

    def config(self):
        print("PROSSEOR-",self.processor)
        print("OPERATING SYSTEM-",self.os)
        print("MEMORY-",self.ram)
        print("STORAGE-",self.storge)
        print("DISPLAY-",self.display)
        print("NETWORKK ADAPTER-",self.network)
        print("OTHER-",self.other)

obj=laptop()

print("OPERTING SYSTEM",obj.os)
m2=obj.os="Microsoft Windows 10 x64(free via Azure Dev Tools for Teaching)"
print("OPERTING SYSTEM",m2)
print("----------------------------------------")
print("MEMORY-",obj.ram)
m1=obj.storge+" 64 GB RAM"
print("MEMORY/STORAGE--",m1)
