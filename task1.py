while True:
    num1 = input("Введите первое число: ")
    if num1 == '0':
        break
    try:
        num1 = float(num1)
        num2 = float(input("Введите второе число: "))
        operator = input("Введите оператор (+, -, *, /) или 0 для выхода: ")
        if operator == "+":
            result = num1 + num2
            print("Результат: ", result)
        elif operator == "-":
            result = num1 - num2
            print("Результат: ", result)
        elif operator == "*":
            result = num1 * num2
            print("Результат: ", result)
        elif operator == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль!")
            else:
                result = num1 / num2
                print("Результат: ", result)
        elif operator == "0":
            print("Программа завершена.")
            break
        else:
            print("Ошибка: неверный оператор!")
    except ValueError:
        print("Ошибка: введено некорректное значение числа.")
