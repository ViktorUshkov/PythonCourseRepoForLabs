# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_count = dict()
    words = text.lower().split()
    text_in_one_line = ''.join(words)
    for sym in text_in_one_line:
        if sym.isalpha():
            if sym in letters_count:
                letters_count[sym] += 1
            else:
                letters_count[sym] = 1
    return letters_count


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count):
    letters_freq = dict()
    count_of_all_letters = sum(letters_count.values())
    for let, count in letters_count.items():
        letters_freq[let] = count/count_of_all_letters

    return letters_freq


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
count_of_letters = count_letters(main_str)
freq_of_letters = calculate_frequency(count_of_letters)
for letter, freq in freq_of_letters.items():
    print(f'{letter}: {freq:.2f}')

