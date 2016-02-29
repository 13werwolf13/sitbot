import os
import constants

def startp():

    alert1 = 0
    alert2 = 0
    alert3 = 0
    alert4 = 0
    response1 = os.system("ping -c 1 " + constants.hostname1)
    response2 = os.system("ping -c 1 " + constants.hostname2)
    response3 = os.system("ping -c 1 " + constants.hostname3)
    response4 = os.system("ping -c 1 " + constants.hostname4)

    if response1 ==0:
        globals()["text1"] = 'srv1 10.0.1.10 is up'
    else:
        globals()["text1"] = 'srv1 10.0.1.10 is down'
        alert1 = 1
    if response2 ==0:
        globals()["text2"] = 'srv2 10.0.1.11 is up'
    else:
        globals()["text2"] = 'srv2 10.0.1.11 is down'
    if response3 ==0:
        globals()["text3"] = 'storage 10.0.1.12 is up'
    else:
        globals()["text3"] = 'storage 10.0.1.12 is down'
        alert3 = 1
    if response4 ==0:
        globals()["text4"] = 'mail 10.0.1.16 is up'
    else:
        globals()["text4"] = 'mail 10.0.1.16 is down'
        alert4 = 1

