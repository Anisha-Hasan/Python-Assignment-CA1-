#Write a Python program to find the average of n numbers using list

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def input_numbers():
    n = int(input("How many numbers do you want to input? "))
    numbers_list = []
    
    for i in range(n):
        number = float(input(f"Enter number {i+1}: "))
        numbers_list.append(number)
    
    return numbers_list


numbers_list = input_numbers()


average = calculate_average(numbers_list)

print("The average of the numbers is:", average)
