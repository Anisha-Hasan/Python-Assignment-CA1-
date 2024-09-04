#to check a number is prime or not

def isprime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 and n%3==0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
n=int(input("Enter a number:"))
if isprime(n):
    print("The number is prime")
else:
    print("The number is not prime")