import time
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
    calenderDate = input("Enter Calender Date")
    calendar.timegm(time.strptime('2000-01-01 12:34:00', '%Y-%m-%d %H:%M:%S'))

def DashStripper():
    s = ""

    phoneNumber = input("Enter phone number: ")
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
    print("[3] Strip dashes from Phone Number")
    choice = input("\n")
    choice = int(choice)

    if (choice == 1):
        EpochTime()
    elif (choice == 2):
        Time2Epoch()
    elif (choice == 3):
        DashStripper()
    else:
        Menu()

Menu()
