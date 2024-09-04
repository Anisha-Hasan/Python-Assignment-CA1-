#Write a Python program to take a input from user in a list and print it.

def input_list():
    n = int(input("How many elements do you want in the list? "))
    

    user_list = []
    

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element)
    
    return user_list


user_list = input_list()


print("The list you entered is:", user_list)
