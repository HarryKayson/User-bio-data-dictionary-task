#Task
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

#initialize an empty dictionary to store the person's info
user_info={}

#Asking the user to input and store it in the dictionary
user_info["name"]=input("Enter your name: ")
user_info["age"]=input("Enter your age: ")
user_info["color"]=input("Enter your favorite color: ")

#Print the dictionary to the console
print("/nHere is the information you provided: ")
print(user_info)