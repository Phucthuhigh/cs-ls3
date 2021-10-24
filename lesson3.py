# a = int(input("Press a: "))
# b = int(input("Press b: "))
# c = int(input("Press c: "))

# maximum = max(a,b,c)
# print(maximum)

# weight = float(input("Press ur weight: "))
# height = float(input("Press ur height: "))

# BMI = weight / (height ** 2)

# print(BMI)
# if BMI < 18.5:
#     print("under weight")
# elif 18.5 <= BMI <= 24.9:
#     print("normal")
# elif 25 <= BMI <= 29.9:
#     print("over weight")
# else:
#     print("obese")

# a = float(input("Press side a: "))
# b = float(input("Press side b: "))
# c = float(input("Press side c: "))

# if a + b > c and b + c > a and a + c > b:
#     print("This is a rectangle")
#     if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
#         if (a == b or b == c or a == c):
#             print("This is a balance right rectangle")
#         else:
#             print("This is a right rectangle")
#     elif a == b == c:
#         print("This is an even triangle")
#     elif a == b or a == c or b == c:
#         print("This is a balance rectangle")
#     elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
#         print("This is a prison triangle")
#     else:
#         print("This is a sharp triangle")
# else:
#     print("This is not a rectangle")

# year = int(input("Year: "))
# condition = [3, 6, 9, 11, 14, 17]

# if year % 4 == 0 or year % 400 == 0 or year % 100 == 0 or year % 19 in condition:
#     print("Leap year")
# else:
#     print("Year")

# practice = 0.3 * float(input("practice: "))
# homework = 0.3 * float(input("homework: "))
# theory = 0.4 * float(input("theory: "))

# total = practice + homework + theory

# s = ' => '
# if total >= 5:
#     s = str(round(total,2)) + s + "Passed"
# else:
#     s = str(round(total,2)) + s + "Failed"

# print(s)

# average_score = float(input("Press Average Score: "))

# if (average_score <= 10):
#     if 9 <= average_score <= 10:
#         print("Xuat sac 😉")
#     elif 8 <= average_score <= 9:
#         print("Gioi 😍")
#     elif 7 <= average_score <= 8:
#         print("Kha 🤤")
#     elif 6 <= average_score <= 7:
#         print("Trung binh kha 🥲")
#     elif 5 <= average_score <= 6:
#         print("Trung binh 😥")
#     elif 4 <= average_score <= 5:
#         print("Yeu 😭")
#     else:
#         print("Kem 😭🤧")
# else:
#     print("Khong co diem nay ban oi 🥺")

# a = float(input("Press a: "))

# isInteger = int(a) == a
# print(f"{a} is an integer") if isInteger else print(f"{a} is not an integer")

# a = input("Press a: ")

# try:
#     a = int(a)
#     print(f"'{a}' is a digit")
# except:
#     print(f"'{a}' is not a digit")

# a = int(input("Press a: "))
# print(f"{a} is even") if a % 2 == 0 else print(f"{a} is odd")

# try:
#     n = int(input("Press n: "))
#     condition = [3,5]
#     a = []

#     for i in condition:
#         if n % i == 0:
#             a.append(i)

#     s = ""

#     if len(a) == 0:
#         s = f"{n} is not divisible by"
#         for i in range(len(condition)):
#             s += f" {condition[i]} "
#             if i != len(condition) - 1:
#                 s += "or"
#     elif len(a) == 1:
#         s = f"{n} is divisible by {a[0]}"
#     else:
#         s = f"{n} is divisible by"
#         for i in range(len(a)):
#             s += f" {a[i]} "
#             if i != len(a) - 1:
#                 s += "and"

#     print(s)
# except:
#     print("error input")

# a = float(input("Input length 1: "))
# b = float(input("Input length 2: "))
# c = float(input("Input length 3: "))

# if a + b > c and b + c > a and a + c > b:
#     print("The 3 line segments can form a triangle.")
# else:
#     print("The 3 line segments cannot form a triangle.")

# import turtle

# a = float(input("Input length 1: "))
# b = float(input("Input length 2: "))
# c = float(input("Input length 3: "))

# if a + b > c and b + c > a and a + c > b:
#     if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
#         print("The 3 line segments can form a right triangle.")
#     elif a == b == c:
#         turtle.Screen()
#         print("The 3 line segments can form an equilateral triangle.")
#         pen = turtle.Turtle()
#         for i in range(3):
#             pen.forward(a)
#             pen.left(180-60)
#         turtle.done()
#     else:
#         print("The 3 line segments can form a triangle.")
# else:
#     print("The 3 line segments cannot form a triangle.")