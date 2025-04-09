# 7.1
def add(a, b):
    return a + b

# 7.2
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 7.3
def average(numbers):
    return sum(numbers) / len(numbers)