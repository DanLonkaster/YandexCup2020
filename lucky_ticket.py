"""
Лотерейный билет
Ограничение времени	1 секунда
Ограничение памяти	512Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Решение, проходящее все тесты, будет оценено в 1 балл.

На различных мероприятиях команда стажировок регулярно разыгрывает призы в лотерею.
Организаторы выбирают 10 случайных различных чисел от 1 до 32.
Каждому участнику выдается лотерейный билет, на котором записаны 6 различных чисел от 1 до 32.
Билет считается выигрышным, если в нем есть не менее 3 выбранных организаторами числа.
Помогите Юле, напишите программу, которая будет сообщать, какие билеты выигрышные.

Формат ввода
В первой строке входных данных записаны 10 различных целых чисел ai (1≤ai≤32) — выбранные организаторами числа.
Во второй строке записано одно целое число n (1≤n≤1000) — количество лотерейных билетов, выданных на мероприятии.
В каждой из n последующих строк записаны 6 различных целых чисел bj (1≤bj≤32) — числа, записанные на очередном лотерейном билета.

Формат вывода
Выведите n строк. Для каждого лотерейного билета в порядке следования во входных данных выведите
строку Lucky, если билет выигрышный, иначе выведите Unlucky.
"""
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
