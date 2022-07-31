import time
import os
import keyboard
from colored import fg  ,bg

s ='''   __     __
  |  \   /  |
  ||| \_/ |||
  |||||||||||
  |||||||||||
  |||||||||||
__|||||||||||__
\ \--.|||.--/ /
 \ \__\_/__/ /
  \ CMDEASE /
   ---------'''
print(s)

color = fg ('light_yellow')

print(color + "EasyCMD.py") \

color = fg('aquamarine_1b')

input(color + "To buy, Press (Return)  on your keyboard: ")

print(color + "(A) Date & Time")
time.sleep(0.1)
print(color + "(B) Flush DNS")
time.sleep(0.1)
print(color + "(C) Open Explorer")
time.sleep(0.1)
print(color + "(D) Display Volume C: Serial Number ")
time.sleep(0.1)
print(color + "Type Exit to leave")
time.sleep(0.1)
color = fg('spring_green_3a')



d1a =  input(color + "Choice: ")

if d1a == "A":
  os.system('cmd /k "color a & date & color b% time"')
  print("You cant change the time by default to do so (Run as Administrator)")
  input()
if d1a == "B":
   os.system('cmd /k ipconfig /flushdns')
   input()
if d1a == "C":
    os.system('cmd /k explorer')
    input()
if d1a == "D":
    os.system('cmd /k "title & Vol C:"') 
    input()
    input()
if d1a == "Exit":
    exit()


    
