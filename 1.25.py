#to check a number is armstrong or not

def is_armstrong(n):

    digits = str(n)
    num_digits = len(digits)
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    return sum_of_powers == n

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
