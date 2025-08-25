def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):  # check only till sqrt(num)
        if num % i == 0:
            return False
    return True

def next_prime(start):
    """Return the very next prime number after 'start'."""
    num = start + 1
    while True:
        if is_prime(num):
            return num
        num += 1

# Example usage
n = int(input("Enter a number: "))
ref = next_prime(n)
print("The next prime number is:", ref)
