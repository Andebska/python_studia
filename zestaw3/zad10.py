"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

"""
Sposób I:
roman_dictionary = {}
roman_dictionary['I'] = 1
roman_dictionary['V'] = 5
roman_dictionary['X'] = 10
itd.
"""
#MMMCMXCIX

def roman2int(roman_number):
    # sposób II:
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for char in roman_number:
        if char not in roman_dictionary:
            print(f"Znak {char} nie istnieje w systemie rzymskim! ")
            return None


    result = 0
    prev_value = 0
    for char in reversed(roman_number):
        value = roman_dictionary[char]
        if value < prev_value:
            result -= value
        else:
            result += value

        prev_value = value

    return result


romanian_num = input("Podaj liczbę rzymską: ")
arabic_num = roman2int(romanian_num)
if arabic_num is not None:
    print(f"Liczba rzymska: {romanian_num} w postaci arabskiej: {arabic_num}")
