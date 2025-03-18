def invest(amount: float, rate: float, years: int):
    """Calculates and prints the investment growth over time."""
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")

def main():
    principal = float(input("Enter the initial amount: "))
    annual_rate = float(input("Enter the annual rate of return (as a decimal): "))
    num_years = int(input("Enter the number of years: "))
    
    invest(principal, annual_rate, num_years)

if __name__ == "__main__":
    main()