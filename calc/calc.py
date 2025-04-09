while True:
    expr = input("Введите выражение (например 2 + 2): ")
    if expr.lower() == 'выход':
        break
    try:
        a, op, b = expr.split()
        a, b = float(a), float(b)
        if op == '+':
            print(a + b)
        elif op == '-':
            print(a - b)
        elif op == '*':
            print(a * b)
        elif op == '/':
            print(a / b)
        else:
            print("Неизвестная операция")
    except:
        print("Ошибка ввода!")