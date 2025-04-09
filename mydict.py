# 6.1
student = {"name": "Иван", "age": 20, "course": 3}
print(student)

# 6.2
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print(merged)

# 6.3
key = input("Введите ключ: ")
print("Ключ есть" if key in student else "Ключа нет")