password = input("Enter a password:")
if len(password) > 7:
    print("Great Password")
elif len(password) == 7:                         # NOTE: use elif which is: else/if combined to save lines of code. 
      print("Password is OK, but not too strong")
else:
     print("Your password is too weak")

# Explanation

# The code prompts the user to enter a new password using the input() function. The entered password is stored in the password variable.

# The if statement is used to check the length of the password using the len() function. If the length of the password is greater than 7, the condition len(password) > 7 evaluates to True, and the program executes the code block under the if statement.

# In this case, it prints "Great password there" to indicate that the entered password is considered strong.

# If the length of the password is equal to 7, meaning the condition len(password) == 7 evaluates to True, the program executes the code block under the elif statement.

# In this case, it prints "Password is OK, but not too strong" to indicate that the entered password meets the minimum length requirement but could be stronger.

# If the length of the password is less than 7, meaning the conditions len(password) > 7 and len(password) == 7 both evaluate to False, the program executes the code block under the else statement.

# In this case, it prints "Your password is weak" to indicate that the entered password is considered weak.

# By running this code, it prompts the user to enter a password and then checks its length. Depending on the length, it provides different feedback to the user about the strength of the password.