# 1. Describe what a computer program is and what does it do.
 
#A computer program is a sequence or set of instructions in a programming language for a computer to execute. It is one component of software
 

# 2. Describe what complexitity and abstraction are, then provide an example
# of complexity in the real world and how we apply abstraction to that thing (you example must be original and cannot be an example
# used in our lecture slides ie car, grocery store, etc.). 
  
# complexity is when code is too hard undestand for a developer. An abstraction is when you dont explain everything except the relevent data.
# Examples: an example of abstraction is that that many people dont know how exactly a computer is built but they can still use it perfectly fine 
#Example2: an example of complexity is if a toaster had all the parts and components that is inside of it and a tutorial on how its built when you buy it 

# 3. What is Syntax in Python and why is it important to write proper syntax?

# a syntax is a set of rules that will dertimine how a program will be written  its important to write a proper syntax because you want your program to run correctly

# 4. What is a function, and why do we wrap our code inside of functions?

# a function is a block of code which will run when it is called, we wrap our code in functions to modify the behavior of the code

# 5. Name and describe the three (3) naming conventions for variables in python? Then provide three (3) name rules for Python
# variables. 

# 6. What will be the output of the print functons when this code is ran, explain why
name = 'Bill'
student = name
name = 'Walter'
student= 'Richard'

print(name)
print(student)
# The outcome would be that it will print Walter and Richard

# 7. Describe the difference between each of the following assignment operators:
# =  assign 
# == is equal to 
# != is not equal to 
 
# 8. What type of data can be stored in a python list?

#Integer and float 
# 9. Create a function that will take in a word provided by a user and then output that word back to the user but in reverse. 

txt= "Hello World" [::-1]
print(txt)


# 10. Create three (3) seperate functions that will do addition, subtraction, and multiplication respectively. 
# each of these functions should take two (2) arguments. When the user passes these arguments into the function, they will be
# calculated together and return the output in your terminal. 

# 11. What is the difference between a function argument and a function parameter. 

# the difference is that a parameter is  the varible listed in the parenthesis in the function definition an argument is the value sent to the function when called 

# 12. You have been hired by a software company and your first assignment is to develop a password authenticator program. 
# the goal of your program is to check a user's password and make sure it meets the company's password requirements. 
# the company has provided you with the following requirements for the passcode program:
# a. the passcode must NOT contain any numbers
# b. the passcode must NOT contain any capital letters
# c. the passcode can NOT be any longer than five (5) characters
# d. the passcode can NOT shorter the three (3) characters
# e. the user should be able to enter their password and if it meets the requirements, should print a message saying that 
# their password was created successfully, and if it was not, should send back a message with one of the following issues. 

# 13. When you run your code and see typeError in your terminal, what does that typically mean and how would you try to solve
# the issue?

#typeError happens when you us different data types in a function 

# 14. When you run your code and see indentError in your terminal, what does that typically mean and how would you try to solve 
# the issue? 

# This typically means there is an issue with your indenting and that you should modify and tweak it using the "enter" and "backspace" keys 

# 15. Create a while loop that check a user's password. If they enter the password correct, they will get a message saying 
# that the password was entered successfully. If they enter the password incorrectly, it will tell the user to try again. 
# The user should only have three (3) attempts to get the password correct. If they enter the password incorrect on the fourth 
# attempt, a message should appear telling them that have been locked out and need to talk to the administrator. 

# 16. Which item is at index 5
giftShopping=['xbox','sneakers','necklace','clothing','laptop','gift card']

#laptop

# 17. Create a for loop that will print ONLY the even numbers within the range of the variable provided below.
# HINT: You will need to use the range() function. 
upToNumber = 30


i= upToNumber = 30 
while i < 30 
print(i)

# 18. Create a function that uses a conditional statement that checks if a person qualifies for a raise on their salary. 
# The user should be able to enter their name, their salary (how much money they make in an entire year), and how long they have
# worked at the company. If the user has been working at the company longer than four (4) years, they will get a 15% raise. 
# Your program should be able to calculate what their salary is with the 15% increase. If the user qualifies, your program
# should return the a message congratulating the user by name, and telling them what their new salary is with the 15%
# increase (this must be the actual number). If they do not qualify inform the user that unfortunately they do not qualify. 

# 19. Create a function that checks which value is greater than the other. Your function should take two (2) integer parameters. 
# and should evaluate which number is larger. Your function should then print the largest number. 
x= max(5,10)
print(x)

# 20. Create a while loop function that will add gift items to a list. Your function should ask the user to enter an item name. 
# The item name should then be added to a list variable called gift_bag. Your gift bag should have a limit of six (6) items. 
# Once your gift bag hits its limit of six (6) items your program should print a message saying 
# that the gift bag is full and print the list of items in the gift bag.   
 
