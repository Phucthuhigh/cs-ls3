try:
    n = int(input("Press n: "))
    condition = [3,5,2,1,6]
    a = []

    for i in condition:
        if n % i == 0:
            a.append(i)

    s = ""

    if len(a) == 0:
        s = f"{n} is not divisible by"
        for i in range(len(condition)):
            s += f" {condition[i]} "
            if i != len(condition) - 1:
                s += "or"
    else:
        s = f"{n} is divisible by"
        for i in range(len(a)):
            s += f" {a[i]} "
            if i != len(a) - 1:
                s += "and"

    print(s)
except:
    print("error input")