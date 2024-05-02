#  Write a program to find the factorial of a given number n.
number = int(input("Choose a number? "))
if number < 0:
    print("Factorial not defined for negative numbers")
else:
    product=1
    for i in range(1,number+1):
        product= product * i
    print(f"factorial of {number} is {product}" )
