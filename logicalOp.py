# Logical operators evaluate multiple conditions (and, or, not)
# and = TRUE if both conditions are true
# or  = TRUE if at least one condition is true
# not = Inverts the condition (True becomes False, False becomes True)

# --- EXAMPLE 1: OR ---
temp = 25
is_raining = True

# Triggers if any condition is met
if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is CANCELLED.")
else:
    print("The outdoor event is STILL RUNNING.")

# --- EXAMPLE 2: AND & NOT ---
temp = 25
is_sunny = True

# Triggers only if both are true
if temp > 28 and is_sunny:
    print("It is hot and sunny outside.")

# Triggers only if both are true
elif temp <= 0 and is_sunny:
    print("It is freezing but sunny outside.")

# Changed lower bound to 0 to catch temperatures between 0 and 28
elif 0 <= temp <= 28 and not is_sunny:
    print("It is cool and cloudy outside.")
