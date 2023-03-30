target_sum = int(input("Сколько хотите накопить? "))
current_sum = 0

while current_sum < target_sum:
    value = int(input("Взнос: "))
    current_sum += value

print('Поздравляю! Вы накопили', current_sum, 'сомов!')
