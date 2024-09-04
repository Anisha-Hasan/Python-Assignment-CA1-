#Write a Python program to find the largest element in the list.

def find_largest(numbers):
    if not numbers:
        return None  
    return max(numbers)


def input_numbers():
    n = int(input("How many numbers do you want to input? "))
    numbers_list = []
    
    for i in range(n):
        number = float(input(f"Enter number {i+1}: "))
        numbers_list.append(number)
    
    return numbers_list


numbers_list = input_numbers()


largest_number = find_largest(numbers_list)

if largest_number is not None:
    print("The largest number in the list is:", largest_number)
else:
    print("The list is empty, no largest number to find.")
