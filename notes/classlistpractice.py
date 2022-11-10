list = []

def addfunc(list, appendage):
    list.append(appendage)

def addmiddlefunc(list, indexspot, appendage):
    list.insert(indexspot, appendage)

def removefunc(list, indexspot):
    del list[indexspot]

addfunc(list, "red")
addfunc(list, "purple")
addmiddlefunc(list, 1, "blue")

print(list)

removefunc(list,2)
print(list)