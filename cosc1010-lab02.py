# Garrick McDonald
# UWYO COSC 1010
# 19 September 2024
# Lab 02 
# Lab Section: 12
# Sources, people worked with, help given to: Logan Cabanaw

hello_message = "Hello, COSC1010"
uw = "cowboy joe"
uwyo = "University of Wyoming"
year = "1886"
x=5
y=10
first_name = "Garrick"
last_name = "McDonald"
space = " "

## Section ONE

# Complete the following print statement to print out "Hello, COSC1010"
print("Hello, COSC1010")

# Assign the string above to a variable named hello_message and print that variable
print(hello_message)

# Assign the string "cowboy joe" to a variable, and print that variable with title casing
print(uw.title())

# Complete the following f-string print message 
    # You will need to create your own variables and insert them  
    # the final message should read `The University of Wyoming was founded in 1886`
print(f"The {uwyo} was founded in {year}")

# Now let's do some math with variables 
    # Create two variables x and y and assign them the values 5 and 10 respectively 
    # Complete the following print statements using your variables
    #All math must be done within the braces in the f-strings
print(f"x + y = {x+y}")
print(f"x - y = {x-y}")
print(f"x * y = {x*y}")
print(f"x / y = {x/y}")

# String concatenation 
    # Finally we will take a look at string concatenation
    # String concatenation combines two strings together
    # It is done using the + operator
    # Create three variables:
        # first_name, which is your first name 
        # last_name, which is your last name
        # space, which is a space character 
    # Use string concatenation to print out your full name 
print(first_name + space + last_name)
