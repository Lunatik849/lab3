import random
import datetime
import math

# 10.1
print(random.randint(1, 100))

# 10.2
print(datetime.datetime.now())

# 10.3
num = float(input("Введите число: "))
print(f"С math: {math.sqrt(num)}")
print(f"Без math: {num**0.5}")