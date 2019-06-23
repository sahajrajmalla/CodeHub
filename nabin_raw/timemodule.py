import random
import string
r1 = random.random()
print(r1)
r2 = random.randint(1, 3)
print(r2)
r3 = random.choice([1, 2, 3, 10])
print(r3)
r4 = "".join(random.choices(string.digits, k=4))
print(r4)
number = [1, 2, 3, 4, 5]
r5 = random.shuffle(number)
print(number)
