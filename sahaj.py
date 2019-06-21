try:
    age = int(input("enter your age = "))
    if age < 18:
        total = 18 - age
        print(f"You are not allowed to vote come back after {total} years!")
    elif age >= 18:
        print(f"you are allowed to vote please wait in the queue!")
    else:
        pass
except ZeroDivisionError:
    print("age cannot be zero")
except ValueError:
    print("age is not valid!")
else:
    print("age valided!")


def myFunc():
    print('this is my function which i set up in branch master2')
