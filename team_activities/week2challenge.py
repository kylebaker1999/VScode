import math
from pickle import FALSE, TRUE
import random
from datetime import datetime

# def even():
#    num =  math.ceil(17**9 / 3) - 6    #ceil rounds up to nearest int
#    return num % 2 ==0

# print(even())


##################WHILE LOOP WITH RANDOM NUMBERS SELECTED   
# randomintlist = []
# while len(randomintlist) < 10:
#     randomintlist.append(random.randint(0,1000))
# randomintlist.sort()
# print(randomintlist)

##########################

now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "odd minute"
print(display_message)



