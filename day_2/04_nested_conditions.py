# Program showing nested if statements

age = 20
has_license = True

if age >= 18:
    print("You are old enough to drive.")
    
    # This inner check only happens if the outer check passed
    if has_license:
        print("You have a license. You can drive!")
    else:
        print("You do not have a license yet. You cannot drive.")

else:
    print("You are too young to drive.")
