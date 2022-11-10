from cgitb import text
import math as mt
from datetime import datetime

tire_width = int(input("What is the width of the tire in mm? "))
aspect_ratio = int(input("What is the aspect ratio of the tire? "))
diameter = int(input("What is the diameter of the tire? "))

volume = mt.pi * tire_width**2 * aspect_ratio*(tire_width*aspect_ratio+ 2540 * diameter)/10000000000

print(f"the approximate volume is {volume:.2f} liters.")

date = datetime.now

f = open("volumes.txt", "w")
text = (str(date), str(tire_width), str(aspect_ratio), str(diameter), str(volume))
f.writelines(text)
f.close()
