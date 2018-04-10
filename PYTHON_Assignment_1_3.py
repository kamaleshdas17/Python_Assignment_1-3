##Write a Python program to accept the user's first and last name and then getting them
##printed in the the reverse order with a space between first name and last name.

""" User Input from terminal """
first_name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")

print("Your name in reverse order:" + first_name[::-1] + " " + last_name[::-1])
