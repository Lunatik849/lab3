import random

number = random.randint(0, 10)
attempts = 3

print("Угадай число от 0 до 10. У тебя 3 попытки!")

for attempt in range(attempts):
    guess = int(input(f"Попытка {attempt + 1}: "))
    
    if guess == number:
        print("Поздравляю! Ты угадал!")
        break
    elif guess < number:
        print("Загаданное число больше!")
    else:
        print("Загаданное число меньше!")
else:
    print(f"Ты проиграл! Загаданное число было: {number}")