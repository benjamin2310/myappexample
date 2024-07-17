print("Ampah")
user = "BenjaminKwameAmpah"
print(user, sep= "-" , end='\n')
print(f'{user}')

# Variables

studentData = 555
StudentName = "Angela"
studentGradePoint = 3.155
studentAge = 25

print(type(studentData), studentData)
print(type(StudentName), StudentName)
print(type(studentGradePoint), studentGradePoint)
# print(type(studentData))

print(studentData.__ceil__())
print(studentGradePoint.__round__())

print(float(studentData))
print(int(studentGradePoint))

print(len(StudentName))

# Chapter 2 - Flow Control
test = (studentData or studentGradePoint) and StudentName
print(test)

if StudentName == "Angela":
    print(f'Hello {StudentName} you are welcome.')
elif StudentName == "Hamza":
    print("I am new here")
else:
    print("check your name")