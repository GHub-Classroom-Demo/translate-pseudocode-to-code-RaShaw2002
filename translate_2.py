'''
The pseudocode below shows a method of comparison to obtain the largest number.
START
   INPUT number1
   INPUT number2
   INPUT number3

   IF number1 > number2 AND number1 > number3 THEN
       largest = number1
   ELSE IF number2 > number3 THEN
       largest = number2
   ELSE
       largest = number3
   ENDIF

   OUTPUT "The largest number is ", largest
END

When you run the program below, you will face logic error, hence:
Your task is to replace variable 'x' with apropriate variable names by referring to the pseudocode
'''


# Find the largest of three numbers

# Input three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Compare numbers to find the largest
if number1 > number2 and number1 > number3:
    largest = number1
elif number2 > number3:
    largest = number2
else:
    largest = number3

# Output the largest number
print("The largest number is", largest1)

