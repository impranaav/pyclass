# Write a python program that classifies a person's age into categories: child, teenager, or adult

age= int(input("Whats your age?"))
if age<0:
    print("Choose a positive number")

elif age < 13 :
    print("You are a Child")

elif age<20:
    print("You are a Teenager")

else:
    print("You are an Adult")