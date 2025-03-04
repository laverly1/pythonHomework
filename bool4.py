a, b, c = map(float, input("Enter three numbers: ").split())
print("All numbers are different" if len({a, b, c}) == 3 else "Some numbers are the same")
