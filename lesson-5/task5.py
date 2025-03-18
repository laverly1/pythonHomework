def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a positive integer: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
