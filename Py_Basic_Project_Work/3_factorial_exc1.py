import math as m
    # num = int(input("Enter a number"))
    # sum = 0

    # for i in range(len(str(num))):
    #     text = str(num)
    #     x = m.factorial(int(text[0]))
    #     num = int(text[1:]) if text[1:] else 0
    #     sum = sum + x
    #     print(x,num,sum)

# factorial (silnia) of 145 = 1! + 4! + 5! = 1 + 24 + 120 = 145
# create a function to calculate factorial
n=int(input("Enter a number"))  
def factorial(n):   
    if n == 0 or n == 1:  
        return 1  
    else:  
        return n * factorial(n - 1)
    
def print_factorial(n):
    result = factorial(n)
    print("The factorial of", n, "is", result)

print_factorial(n)
    
    

