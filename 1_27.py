#Write a Python program to implement multiplication table.

def multiplication_table(n, upto=10):
    for i in range(1, upto + 1):
        print(f"{n} x {i} = {n * i}")


number = int(input("Enter a number: "))

upto = int(input("Enter the range (default is 10): ") or 10)


print(f"Multiplication table of {number}:")
multiplication_table(number, upto)
