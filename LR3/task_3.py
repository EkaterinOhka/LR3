# TODO  Напишите функцию count_letters
def count_letters(text):
    counted_letters = {}
    for letter_in_text in text.lower():  # просматриваем символы текста, приведя все к нижнему регистру
        if letter_in_text.isalpha():  # проверяем символы на то, являются ли они буквой
            count = 0
            for compare_letter in text.lower():  # повторно просматриваем текст
                if compare_letter == letter_in_text:  # сравниваем повторно полученные буквы с изначальной
                    count += 1
                    counted_letters[letter_in_text] = count  # заполняем словарь буквами и их количеством
    return counted_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(counted_letters):
    letter_frequency = {}
    sum_of_letters = 0
    for letter_sum in counted_letters:  # находим сумму букв в тексте, суммируя значения полученного словаря
        sum_of_letters += counted_letters[letter_sum]

    for letter_in_dict in counted_letters:  # считаем частоту повторения каждой буквы
        for _ in range(1, len(counted_letters)):
            letter_frequency[letter_in_dict] = counted_letters[letter_in_dict] / sum_of_letters
    return letter_frequency

# создаем тестовый текст для проверки
# test_str = """
# """


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
"""
вывод для проверки работы программы
for letter in calculate_frequency(count_letters(test_str)):
    print(f"{letter}: {calculate_frequency(count_letters(test_str))[letter]:.2f}")
"""
# построчный вывод
for letter in calculate_frequency(count_letters(main_str)):
    print(f"{letter}: {calculate_frequency(count_letters(main_str))[letter]:.2f}")
