from platform import freedesktop_os_release
from unicodedata import name

from numpy import average


student1 = {"age":20,
"name": "Fred" ,
"phone_number": "5555555555"}

student2 = {"age":22,
"name": "Jenny" ,
"phone_number": "5555555555"}

#print("the name of the student is " + student2[name])

student_list = [student1,
                student2]

print(student_list)

print(len(student_list))
i = 0
while i < len(student_list):
    print(student_list[i])
    i=+1

for i in student_list:
    print(i)


#compute average age of all students in list
total_age = 0
for student in student_list:
    total_age += student["age"]

average_age = total_age / len(student_list)
print(average_age)


student_names = ["Jed", "Jen", "Sandy"]
#### Print out names of all the students
for student_name in student_names:
    print(student_name)
    
#### print first student
print(student_names[0])

#### print second student
print(student_names[1])


i = len(student_names)
while (i >= 0 ):
    print(student_names[i])
    i-= 1

    