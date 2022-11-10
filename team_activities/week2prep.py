import math
items = int(input("enter the number of items"))
itemsperbox = int(input("enter the number of items per box"))

numberofboxes = math.ceil(items / itemsperbox)

print(f"for {items} items, packing {itemsperbox} per box, you will need {numberofboxes} boxes.")