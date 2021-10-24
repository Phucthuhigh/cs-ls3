a = input("Press a: ")

try:
    a = int(a)
    print(f"'{a}' is a digit")
except:
    print(f"'{a}' is not a digit")