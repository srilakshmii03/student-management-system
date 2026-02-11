students={
     "101":"Rangaiah",
     "102":"Vijaya",
     "103":"Sri"
}
file=open("students.txt","w")
for roll,name in students.items():
    file.write(roll +","+ name + "\n")
file.close()
print("Students saved to file")
file=open("students.txt","r")
students={}
for line in file:
    roll,name=line.strip().split(",")
    students[roll]=name
file.close()
print(students)
