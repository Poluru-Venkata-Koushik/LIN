
class linBus():

    def __init__(self):
        self.Highvalue = True
        self.bus = []
        self.slaves = {

        }
    
    def addSlave(self, ID, lenData):
        if not ID in self.slaves.keys():
            self.slaves[ID] = lenData
        else:
            pass

class messages():
    def __init__(self, id , p0, p1):
        self.breakval = "0b0000000000000"
        self.sync = "0b01010101"
        self.id = None
        self.p0 = None
        self.p1 = None
    
