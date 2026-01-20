'''
Task: Ask the user to input two numbers and print which one is smaller.

Write your pseudocode here
START
   INPUT number1
   INPUT number2
   IF number1 < number2 THEN
       OUTPUT "The smallest number is", number1
   ELSE
       OUTPUT "The smallest number is", number2
   ENDIF
END

translate your pseudocode to python code.
'''
# Find the smallest of two numbers

# Input two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Compare the numbers
if number1 < number2:
    print("The smallest number is", number1)
else:
    print("The smallest number is", number2)
