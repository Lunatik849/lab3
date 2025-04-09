# 9.1
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Ошибка: введите число!")

# 9.2
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Файл не найден!")