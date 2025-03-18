def find_factors(n: int):
    """Prints the factors of the given positive integer n."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")

def main():
    number = int(input("Enter a positive integer: "))
    find_factors(number)

if __name__ == "__main__":
    main()