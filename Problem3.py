# energy = 1000
# sport = 100
# home_action = 50
# homework = 180
# listening = 200
# task1
# # while energy > 0:
#
# print(f'У Вас есть {energy} единиц здоровья')
#
# start_the_action = input('Выберите Ваше действие: ')
# if start_the_action == '1':
#     print('У Вас осталось', (energy - sport), 'единиц здоровья')
#
#
# # print(f'У Вас осталось {energy} единиц здоровья')
#
# if energy <= 0:
#     print('Вы проиграли. У Вас 0 жизней')

energy = 1000
spent_energy = 0
restored_energy = 0

while energy > 0:
    print("Выберите активность:")
    print("1 - спорт (100 единиц)")
    print("2 - домашняя активность (60 единиц)")
    print("3 - уроки (180 единиц)")
    print("4 - слушать нытье (200 единиц)")
    print("5 - прослушивание музыки (60 единиц)")
    print("6 - прием пищи (150 единиц)")
    print("7 - сон (500 единиц)")
    choice = int(input("Введите номер активности: "))

    if choice == 1:
        if energy >= 100:
            energy -= 100
            spent_energy += 100
        else:
            print("Недостаточно энергии для этой активности")
    elif choice == 2:
        if energy >= 60:
            energy -= 60
            spent_energy += 60
        else:
            print("Недостаточно энергии для этой активности")
    elif choice == 3:
        if energy >= 180:
            energy -= 180
            spent_energy += 180
        else:
            print("Недостаточно энергии для этой активности")
    elif choice == 4:
        if energy >= 200:
            energy -= 200
            spent_energy += 200
        else:
            print("Недостаточно энергии для этой активности")
    elif choice == 5:
        energy += 60
        restored_energy += 60
    elif choice == 6:
        energy += 150
        restored_energy += 150
    elif choice == 7:
        energy += 500
        restored_energy += 500
    else:
        print("Выбрана некорректная активность")

print("Общая потраченная энергия: ", spent_energy)
print("Общая восстановленная энергия: ", restored_energy)
