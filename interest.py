#write a python program to calculate the simple interest for a given principal amount, rate of interest, and time period (in years).
# note: ensure that the user inputs are properly validated (eg: negative values)
principal = int(input("Please write the Principal Amount? "))
time = int(input("Please write the time period in Years "))
rate = int(input("Rate of interest per Year "))
interest=(principal*time*rate) / 100
print (f"Simple Interest is {interest}")
