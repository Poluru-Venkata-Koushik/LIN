from Master import linBus, messages, Slave
import time
import os
import asyncio


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    #pass # will remove it after testing

global inputDict,a,lin


def PrintMenu():
    print("============================================")
    for i in inputDict:
        print(f"{i} - {inputDict[i][0]}")
    print("============================================")

def ValidateInput():
    global a
    if a in inputDict.keys():
        return True
    else:
        return False

def addSlave():
    clear_screen()
    Name = input( "Enter the name of the slave/ECU: ")
    if all(s.name != Name for s in lin.slaves) and len(lin.slaves) < 16:
        new_slave = Slave(Name)
        new_slave.bus = lin.bus
        lin.slaves.append(new_slave)
        print([slave.printName() for slave in lin.slaves])
    else:
        print("Cannot add slave. Either already exists or max limit reached.")
    time.sleep(0.7)

def RemoveSlave():
    clear_screen()
    if len(lin.slaves)==0:
        print("Nothing to Remove ")
    else:
        print("Current Slaves" , [slave.printName() for slave in lin.slaves])
        Name = input("Enter the name of the slave/ECU to remove: ")
        try:
            slave_to_remove = next(x for x in lin.slaves if x.name == Name)
            print(slave_to_remove)
            lin.slaves.remove(slave_to_remove)
        except ValueError:
            print("Slave not found")
        print("Removed Slave: ", Name)
        print([slave.printName() for slave in lin.slaves])
    time.sleep(0.95)

def showSlaves():
    clear_screen()
    if not len(lin.slaves)==0:
        print([(x.name, [y for y in x.ID]) for x in lin.slaves])
    else:
        print("No Slaves")
    time.sleep(1)

def addID():
    
    clear_screen()
    if not len(lin.slaves)==0 :
        print(" Current ECUs ", [slaves.name for slaves in lin.slaves])
        slave_to_add = next( x for x in lin.slaves if x.name == input("Enter the ECU name : "))
        slave_to_add.ID.append(input("Enter ID:"))
    else:
        print("No ECUs to add ID to")
        return
    time.sleep(0.9)

async def processMessages():
    while True:
        await asyncio.gather(*(s.ProcessMessage() for s in lin.slaves))
        await asyncio.sleep(1)    

def calculateP0P1(hex_id):
    value = int(hex_id, 0)  
    if value > 63 or value < 0:
        return "Invalid ID"
    result = (f"{value & 0xFF:06b}")
    I0 = bool(result[-1])
    I1 = bool(result[-2])
    I2 = bool(result[-3])
    I3 = bool(result[-4])
    I4 = bool(result[-5])
    I5 = bool(result[-6])
    p0 = int(I0 ^ I1 ^ I2 ^ I4)
    P1 = int(not( I1 ^ I3 ^ I4 ^ I5))

    print (f"{P1}{p0}{result}")

calculateP0P1("0x11")



def addMessage():
    idToQuery = input("Enter the ID of ECU you wish to query :")
    if not calculateP0P1(idToQuery) == "Invalid ID":
        lin.bus.append("idToQuery")
    else:
        raise Exception ("Invalid ID")

inputDict = {
    "1" : ["Add Slave",addSlave],
    "2" : ["Remove Slave",RemoveSlave],
    "3" : ["Show Slaves",showSlaves],
    "4" : ["Message - Unconditional",addMessage],
    "5" : ["Message - Event Triggered", exit],
    "6" : ["Message - UDS", exit],
    "7" : ["Add ID to ECU ",addID],
    "8" : ["Add Entry to Schedule Table", exit],
    "99" : ["Exit", exit]
}

async def main():
    global a, lin 
    lin = linBus()
    asyncio.create_task(processMessages())
    while True : 
        clear_screen()
        PrintMenu()
        a = await asyncio.to_thread(input, "Enter your choice : ")
        if ValidateInput():
            inputDict[a][1]()
        else :
            print("Invalid Input, Try Again")
            time.sleep(0.8)

if __name__ == "__main__":
    asyncio.run(main())



