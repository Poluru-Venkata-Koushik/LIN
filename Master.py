import asyncio
import time
class linBus():

    def __init__(self):
        self.Highvalue = True
        self.bus = []
        self.slaves = []
        self.scheduleTable = {

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
        self.id = id
        self.p0 = p0
        self.p1 = p1


class Slave():
    def __init__(self, name):
        self.ID = []
        self.name = name
        self.bus = None
        self.currentValue = None
        self.LastUpdated = None
        self.hasUpdates = False
    
    def printName(self):
        return self.name
    
    async def ProcessMessage(self):
        if self.bus != []:
            msg = self.bus
            print(msg)
            print([x for x in self.bus])
            self.bus=[]
        else:
            pass

            
                

    

