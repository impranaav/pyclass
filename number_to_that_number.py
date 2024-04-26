# Write a program that asks the user for a number n, then calculates and prints the sum of all numbers from 1 to n.
number = int(input("Enter a number:" ))
sum=0
for i in range(1, number+1):
    sum=sum+i
print(sum)
