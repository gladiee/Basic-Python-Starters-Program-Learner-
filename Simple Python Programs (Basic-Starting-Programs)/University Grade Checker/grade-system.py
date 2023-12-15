print("SM UNIVERSITY Exam Result Window!")
print()
print("Grade Checker!")
print()

St_name = input("Name of The Student! : ")

print()
print("Now Enter Each Subject Mark in Below Section!")
print()

eng1 = int(input("English - 1 Mark: "))
eng2 = int(input("English - 2 Mark: "))
mal1 = int(input("Malayalam - 1  Mark: "))
mal2 = int(input("Malayalam - 2  Mark: "))
math1 = int(input("Maths - 1 Mark: "))
math2 = int(input("Maths - 2 Mark: "))
physics = int(input("Physics  Mark: "))
chem = int(input("Chemistry  Mark: "))
cs = int(input("Computer  Mark: "))
prac = int(input("Praticals  Mark: "))

tmark = (eng1, eng2, mal1,  mal2, math1, math2, physics, chem, cs, prac)
mark = sum(tmark)

print("Total Mark Obtained by ", St_name, "is :", mark, "Out of 1000")
print()

tm = float(mark)
m = tm/10

if m >= float(95.0):

    print(St_name,"Accquired Topper Position With :", m,"%")

elif float(90.0) <= m <= float(94.9):

    print(St_name,"Accquired First Class With :", m,"%")

elif float(85.0) <= m <= float(89.9):

    print(St_name,"Accquired Second Class With :", m,"%")

elif float(75.0) <= m <= float(84.9):

    print(St_name,"Accquired Distinction With :", m,"%")

elif float(60.0) <= m <= float(74.9):

    print(St_name,"Accquired First Grade With :", m,"%")

elif float(50.0) <= m <= float(59.9):

    print(St_name,"Accquired Second Grade With :", m,"%")

elif float(40.0) <= m <= float(49.9):

    print(St_name,"Accquired Third Grade With :", m,"%")

elif float(39.9) <= m <= float(0.0):

    print(St_name,"Failed In Exam :", m,"%")
    print("Try in Next Exam | U can Apply at https://google.com")

print()

