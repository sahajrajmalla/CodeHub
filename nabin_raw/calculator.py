from math import pi


def add(x, y):
    return x + y


def pie(x, y):
    return pi


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def muntiply(x, y):
    return x * y


print("select operatent")
print("1.add")
print("2.sub")
print("3.div")
print("4.munt")
print("5.pie")
choice = input("Enter your choice: ")
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter Second number: "))
if choice == "1":
    print(numb1, "+", numb2, "=", add(numb1, numb2))
elif choice == "2":
    print(numb1, "-", numb2, "=", subtract(numb1, numb2))
elif choice == "3":
    print(numb1, "/", numb2, "=", divide(numb1, numb2))
elif choice == "4":
    print(numb1, "*", numb2, "=", muntiply(numb1, numb2))
elif choice == "5":
    print(pie(pi))
else:
    print("Syntax Error")
