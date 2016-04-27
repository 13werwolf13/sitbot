import os
import constants


def startp():

    response1 = os.system("ping -c 1 " + constants.hostname1)
    response2 = os.system("ping -c 1 " + constants.hostname2)
    response3 = os.system("ping -c 1 " + constants.hostname3)
    response4 = os.system("ping -c 1 " + constants.hostname4)

    if response1 ==0:
        globals()["text1"] = 'srv1 is up'
    else:
        globals()["text1"] = 'srv1 is down'

    if response2 ==0:
        globals()["text2"] = 'srv2 up'
    else:
        globals()["text2"] = 'srv2 is down'

    if response3 ==0:
        globals()["text3"] = 'srv3 is up'
    else:
        globals()["text3"] = 'srv3 is down'

    if response4 ==0:
        globals()["text4"] = 'srv4 is up'
    else:
        globals()["text4"] = 'srv4 is down'
