# if Statement = execute some code only if a condition is true
#                they allow for basic decision-making.
#                (if - elif - else)

age = int(input("Enter your age: "))
has_Ticket = True
initial_value = 10

if age < 0:
    print("You are not yet born literally")
elif age == 0:
    print("You are a just fresh born in Rwanda")
elif age >= 95:
    print("You are a dedicated living library")
elif age >= 65:
    print("You are senior citizen in Rwanda")
elif age >= 18:
    print("You are old enough to vote in Rwanda")
else:
    print("You are still young to vote in Rwanda")
