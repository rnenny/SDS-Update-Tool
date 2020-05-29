import time
import datetime
import calendar
import pyperclip
import re

def EpochTime():
    epochtime = time.time()
    print("Current Epoch time is: ", end='')
    print(int(epochtime))
    pyperclip.copy(int(epochtime))
    Menu()


def Time2Epoch():
    calenderDate = input("Enter Calender Date: ")
    try:
        calenderDate = calendar.timegm(time.strptime(calenderDate, '%d-%m-%Y %H:%M:%S'))
    except:
        calenderDate = calendar.timegm(time.strptime(calenderDate, '%Y-%m-%d'))
    finally:
        pass
    print(calenderDate)
    Menu()

def ConvertEpochTime():
    epochtime = input("Enter Epoch time to be converted: ")
    epochtime = int(epochtime)
    convertedepoch = datetime.datetime.utcfromtimestamp(epochtime).replace(tzinfo=datetime.timezone.utc)
    print(convertedepoch)
    pyperclip.copy(convertedepoch)
    Menu()

def CamelCase():
    text = input("Enter text to Camel Case: ")
    text = text.title()
    pyperclip.copy(text)
    print(text)
    Menu()

def DashStripper():
    s = ""

    phoneNumber = input("Enter number: ")
    phoneNumber = re.sub('[^A-Za-z0-9]+', '', phoneNumber)
    # phoneNumber = phoneNumber.replace("-", "")
    # phoneNumber = s.join(phoneNumber)
    # phoneNumber = phoneNumber.replace((".", "")) # will need to re-connent string to use this line
    # phoneNumber = s.join(phoneNumber)
    print(phoneNumber)
    pyperclip.copy(phoneNumber)
    Menu()

def Menu():
    print("\n[1] Get Current Epoch Time")
    print("[2] Convert Date to Epoch Time")
    print("[3] Strip Special Characters from Number")
    print("[4] Convert Epoch to Human Time")
    print("[5] Convert to Camel Case")
    choice = input("\nEnter Menu Choice: ")
    choice = int(choice)

    if (choice == 1):
        EpochTime()
    elif (choice == 2):
        Time2Epoch()
    elif (choice == 3):
        DashStripper()
    elif (choice == 4):
        ConvertEpochTime()
    elif (choice == 5):
        CamelCase()
    else:
        Menu()


Menu()
