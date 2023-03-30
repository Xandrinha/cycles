import random

number = random.randint(0, 100)
count = 0

while count < 10:
    guess = int(input('Угадайте число от 0 до 100: '))
    count += 1

    if guess == number:
        print(f"Поздравляем! Вы угадали число {number} за {count} попыток!")
        break

    if guess < number:
        print("Загаданное число больше, чем", guess)
    else:
        print("Загаданное число меньше, чем", guess)

    if count == 10 and guess != number:
        print(f"К сожалению, вы не угадали число за 10 попыток. Было загадано число {number}.")
