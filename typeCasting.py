# TypeCasting  = the process of converting a variable form on data type to another.
#                   str(), int(), float(), bool()
#Relevant most in user input handling

name = "Alicade"
age = 25
gpa = 3.2
is_student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

age = float(age)
print(type(age))
age = str(age)
print(type(age))


name = bool(name)
print(name) #True because it is non-empty string
name =""
name = bool(name)
print(name) #False because it is empty string