def main():
    # exercise1()
     exercise2()
#
# EXERCISE1
# Create a function that has a loop that quits with ```q```.
# If the user doesn't enter ```q```, ask them to input another string.
#
# def exercise1():
#     while True:
#         code = input("Enter the letter of your first name.")
#         if code.upper() == "Q":
#             break
#
# if __name__ == '__main__':
#     main()

# EXERCISE2
# Write 2 functions: ```exercise2()``` and ```exercise2_helper(num1, num2, num3. operation)```
# The function ```exercise2_helper(num1, num2, num3)``` should expect 3 numbers, and an operation to perform as a String as parameters.
# The function should support 3 operations:
# * ```SUM``` - Return the sum of the 3 numbers
# * ```PROD``` - Return the product of the 3 numbers
# * ```AVG``` - Return the average of the 3 numbers
# The operation and the returned value should then be printed out back in the main ```exercise2()``` function.
# Return ```INVALID OPERATION``` if an operation passed in that isn't supported. HINT: Use ```switch/case```

def exercise2():
    print(exercise2_helper(3,24,99, "SUM"))
    print(exercise2_helper(3,24,99,"Product"))
    print(exercise2_helper(3,24,99,"Average"))

def exercise2_helper(num1, num2, num3, op):
    if op == "SUM":
            return(num1 + num2 + num3)
    elif op == "Product":
                return(num1*num2*num3)
    elif op == "Average":
                return(num1 + num2 + num3 // 3)
    else:
                print("Invalid Function")

    print(exercise2_helper(num1,num2, num3,op))

if __name__ == '__main__':
    main()


