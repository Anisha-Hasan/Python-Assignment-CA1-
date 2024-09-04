#Write a Python program to perform Linear search.

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

def input_numbers():
    n = int(input("How many numbers do you want to input? "))
    numbers_list = []
    
    for i in range(n):
        number = float(input(f"Enter number {i+1}: "))
        numbers_list.append(number)
    
    return numbers_list


numbers_list = input_numbers()

target_number = float(input("Enter the number to search for: "))

index = linear_search(numbers_list, target_number)

if index != -1:
    print(f"Number {target_number} found at index {index}.")
else:
    print(f"Number {target_number} not found in the list.")
