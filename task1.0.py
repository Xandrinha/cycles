while True:
    try:
        num1 = float(input("Введите первое число: "))
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
                print("Ошибка: деление на ноль запрещено!")
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
