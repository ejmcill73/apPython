# 1. What is the difference between 
# a parameter and an argument in a python function
# A parameter is the variable listed inside the parentheses.An arguement is the value that are sent to the function when it is called 

# 2. In your own words, describe what 
# a conditional statement (if/else) is 
# A conditional statement is something that allows you to make decisons based on if a specific condition is met or not



# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )
 temperature = 25
if temperature > 30:
 Print ("its hot outside.") 
 else 
 print("Its not too hot.")

# 3. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 
def check_fridge (food_in_fridge) :
 if: food_in_fridge :
  print("Time to cook.")
 else:
  print("Time to shop.")
  check_fridge (True)
  check_fridge(False)


# 4. Create a function that checks the inventory of cereal for a store. 
# your function should parameter should accept an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".
def check_cereal_invetory(quanity):
 if quanity > 10:
  print("Invetory full.")
  else print("We need to order more cereal")
check_cereal_invetory (15)
check_cereal_invetory(5)