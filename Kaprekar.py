#program to find Kaprekar Number
#Defination: A number whose square, when split into two parts, 
# and the parts added together, result in the original number. 
# For example, 45 is a Kaprekar number because 45² = 2025 and 20 + 25 = 45.

num = int(input("Enter a number: "))
x = num

sqr = num ** 2
y = sqr
a = 0

while sqr != 0:
    a += (sqr % 100)
    sqr //= 100

if a == x:
    print(f"{x} is a Kaprekar Number.")
else:
    print(f"{x} is not a Kaprekar Number.")

