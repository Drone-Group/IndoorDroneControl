#       As it turns out, there is a way to automate Mission Planner directly from the 
#           python script.  That being the case, ArduPilot uploaded documentation of 
#           of how this works and what information can be accessed.
#
#   https://ardupilot.org/planner/docs/using-python-scripts-in-mission-planner.html
#
import sys

sys.path.append(r"c:\Python27\Lib\site-packages")   # Very important that we
sys.path.append(r"c:\Python27\Lib")                     # use Python 2.7

import serial
import os
import threading

#           Most, if not all, of this code will change because we have a small drone

#           [ Script ] references ArduP's 'MegaScript'
#               It's written in c#
#
for cc in range(1, 9):
    Script.SendRC(cc, 1500, False)
    Script.SendRC(3, Script.GetParam('RC3_MIN'), True)

Script.Sleep(5000)

#           [ cs ] refers to accessing the value of a variable at the current state
#
while cs.lat == 0:
    print 'Activating GPS'
    Script.Sleep(1000)

print 'GPS is up'

# ------------- This code is ideally meant to run on RG's PC -------------

Script.SendRC(3, 1000, False)
Script.SendRC(4, 2000, True)
cs.messages.Clear()
Script.WaitFor('ARMING MOTORS', 30000)
Script.SendRC(4, 1500, True)
print 'Motors Armed!'
Script.SendRC(3, 1700, True)

while cs.alt < 50:
    Script.Sleep(50)

Script.SendRC(5, 2000, True)    # Acro
Script.SendRC(1, 2000, False)   # Roll
Script.SendRC(3, 1370, True)    # Throttle

while cs.roll > -45:            # Top half 0 - 180
    Script.Sleep(5)
while cs.roll < -45:            # Bottom (-180) - (-45)
    Script.Sleep(5)

Script.SendRC(5, 1500, False)   # Stabilize
Script.SendRC(1, 1500, True)    # Level it out
Script.Sleep(2000)              # Literally giving it time to stabilize
Script.SendRC(3, 1300, True)    # Throttle back to land

while cs.alt > 0.1:             # Decend but dont fly into the ground
    Script.Sleep(300)

Script.SendRC(3, 1000, False)
Script.SendRC(4, 1000, True)
Script.WaitFor('DISARMING MOTORS', 30000)
Script.SendRC(4, 1500, True)

print 'Roll\'d'
