def palindromes(text):
    """
    Функция обрабатывает введенный текст и ищет наименьший палиндром, например aa bb aba bab
    Логика построена на проверке текста кусочками, так как мы ищем самый маленький палиндром, если он находится
    между 1 и 3 символом то нет смысла проверять текст от 0 до n. Правильнее начать проверку от 3 до n
    :param text: На вход функция принимает введенный текст, это должен быть string
    :return: Функция возвращает либо самый короткий палиндром либо -1
    """
    a = 0  # Объявляем переменную a равную изначально 0, в нее в цикле запишем точку начала проверки текста
    palindrome = None  # Объявляем палиндром, изначально равный ничему

    for i in range(len(text)):  # Проходимся циклом длиной в длину введенного текста
        for j in range(a, i):  # Пройдемся циклом длиной от начала отсчета до символа из цикла выше
            chunk = text[j:i + 1]  # Кусок текста равен символам от j до i+1
            if chunk == chunk[::-1]:  # Если кусок текста палиндром
                if not palindrome:  # И это первый найденный палиндром
                    palindrome = chunk  # Тогда наш текущий палиндром будет равен куску текста chunk
                elif palindrome:  # Если мы уже нашли какой либо палиндром
                    if len(chunk) < len(palindrome):  # Если новый палиндром короче старого
                        palindrome = chunk  # Тогда меняем значение текущего палиндрома на chunk
                    elif len(chunk) == len(palindrome):  # Если новый палиндром и старый равны по длине
                        if chunk < palindrome:  # Сверяем палиндромы лексикографически, если новый короче
                            palindrome = chunk  # Меняем старый палиндром на новый chunk
            a = j  # Обновляем точку начала проверки текста

    if palindrome:  # Если нашли какой либо палиндром, возвращаем его
        return palindrome
    else:  # Если не нашли ни один палиндром, тогда возвращаем -1
        return "-1"


text = input()  # Получаем из ввода текст
print(palindromes(text=text))  # Выводим результат обработки текста на консоль
