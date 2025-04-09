# 8.1
with open("test.txt", "w") as f:
    f.write("Hello, File!")

# 8.2
with open("test.txt", "r") as f:
    print(f.read())

# 8.3
with open("test.txt", "a") as f:
    f.write("\nНовая строка")