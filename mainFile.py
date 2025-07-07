from Master import linBus, messages
import time
import os

def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")

global inputDict,a

inputDict = {
    "1" : "Add Slave",
    "2" : "Remove Slave",
    "3" : "Message - Unconditional",
    "4" : "Message - Event Triggered",
    "5" : "Message - UDS",
    "6" : "Add ID to ECU ",
    "99" : "Exit",
}

def PrintMenu():
    print("============================================")
    for i in inputDict:
        print(f"{i} - {inputDict[i]}")
    print("============================================")

def ValidateInput():
    global a
    if a in inputDict.keys():
        return True
    else:
        return False

def main():
    global a
    while True : 
        clear_screen()
        PrintMenu()
        a = input("Enter your choice : ")
        if ValidateInput():
            pass # Do the tasks here
        else :
            print("Invalid Input, Try Again")
            time.sleep(1.2)

if __name__ == "__main__":
    main()

