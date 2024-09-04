#print reverse of a number

def reverse_number(n):
    reversed_num = int(str(n)[::-1])
    return reversed_num
number = int(input("Enter a number: "))
print("Reversed number:", reverse_number(number))
