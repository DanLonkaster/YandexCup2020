win_numbers = input()  # Получаем из ввода выигрышные номера в формате 1 2 3 4 5 6
win_numbers = win_numbers.split()  # Создаем список из номеров, сплитуя их через пробел,получаем [1,2,3,4,5,6]
players = input()  # Получаем из ввода количество игроков

for player in range(int(players)):  # Перебираем всех игроков от первого до последнего
    counter = 0  # Устанавливаем переменную счетчика на 0
    ticket = input()  # Получаем из ввода билет в формате 1 2 3 4 5 6
    ticket = ticket.split()  # Создаем список из номеров этого билета, получаем [1,2,3,4,5,6]
    for number in ticket:  # Перебираем цифры из билета
        if number in win_numbers:  # Если цифра есть в выигрышных цифрах тогда счетчик увеличиваем на единицу
            counter += 1
    if counter >= 3:  # Если по результатам перебора в билете есть как минимум 3 выигрышных цифры - выводим Lucky
        print("Lucky")
    else:  # Если меньше трех выигрышных цифр - выводим Unlucky
        print("Unlucky")
