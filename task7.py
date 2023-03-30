num = input("Введите натуральное число: ")
x = 0

for i in num:
    if int(i) > x:
        x = int(i)

print(f"Наибольшая цифра в числе {num} равна {x}")
