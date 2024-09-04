#Write a Python program to print Fibonacci series of n term

def fibonacci_series(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))

print("Fibonacci series up to", n, "terms:")
fibonacci_series(n)
