# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remove), unordered
#         No duplicates, best for membership testing

#LIST
print("\nLIST")
print("==========================================")

fruits = ["apple", "orange", "banana", "coconut"]

print(fruits) #Print out whole List
fruits[0] = "Lemon" #Updating the element
fruits.remove("banana") #Removing specific element
fruits.append("cherry") #Appending or add element
fruits.insert(1, "banana") #Inserting the element at specific i
fruits.pop(2) #removing the element at specific element
fruits.clear() #Cleaning all of elements

#Print out list using the loop
for fruit in fruits:
    print(fruit, end=" ")

#TUPLE !Immutable
print("\nTUPLE")
print("==========================================")
fruits = ("apple", "orange", "banana", "coconut")
for fruit in fruits:
    print(fruit, end=" ")


#SET !Unordered
print("\nSET")
print("==========================================")
fruits = {"apple", "orange", "banana", "coconut"}

fruits.add("mango")
fruits.add("mango")
fruits.add("mango")
fruits.remove("coconut")
fruits.pop()
print(fruits)
fruits.clear()


for fruit in fruits:
    print(fruit, end=" ")

#Search for specific element in set
if "banana" in fruits:
    print("banana found")
else:
    print("banana not found")