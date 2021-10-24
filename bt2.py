a = float(input("Press a: "))

isInteger = int(a) == a
print(f"{a} is an integer") if isInteger else print(f"{a} is not an integer")