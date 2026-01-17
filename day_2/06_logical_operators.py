# Program illustrating Logical Operators (and, or, not) in conditionals

age = 65
day = "Tuesday"

# Determine ticket price
# Senior citizens (65+) OR children (under 12) get a discount
# AND if it's Tuesday, everyone gets a discount

if (age >= 65 or age < 12) or day == "Tuesday":
    print("You get a discount ticket Price: $10")
else:
    print("Standard ticket Price: $15")

# 'not' operator example
is_member = False
if not is_member:
    print("Consider joining our membership for more benefits!")
