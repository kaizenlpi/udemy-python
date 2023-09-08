password = input("Enter a password:")
if len(password) > 7 :
   print("Great password there!")
else:
    if len(password) < 7:
     print("Your password is weak")