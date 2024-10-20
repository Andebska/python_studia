
def ex_10(line):
        return len(line.split())


def ex_11(word):
        return '_'.join(word)


def ex_12(line):
        words = line.split()    #tworzy liste
        first_letters = ''
        last_letters = ''

        for word in words:
            word = word.rstrip(",.")         #usuwa przecinki i kropki z konca slow
            first_letters += word[0]
            last_letters += word[-1]

        return "Z pierwszych liter: ", first_letters, "  Z ostatnich liter: ", last_letters


def ex_13(line):
        words = line.split()
        sum = 0

        for word in words:
            only_letters = ''
            for char in word:
                    if char.isalpha():           #sprawdza czy znak jest litera
                            only_letters += char
            sum += len(only_letters)

        return sum


def ex_14(line):
        words_before = line.split()
        words_after = []

        for word in words_before:
            word = word.rstrip(",.")         #usuwa przecinki i kropki z konca slow
            words_after.append(word)

        max_length = max(len(word) for word in words_after)
        longest_words = []
        for word in words_after:
                if(len(word) == max_length):
                        longest_words.append(word)

        return longest_words, max_length


def ex_15(L):
        return ''.join(str(num) for num in L)


def ex_16(line):
        return line.replace("GvR", "Guido van Rossum")


def ex_17(line):
        words_before = line.split()
        words_after = []

        for word in words_before:
                word = word.rstrip(",.")  # usuwa przecinki i kropki z konca slow
                word = word.lower()       # zmienia na male litery
                words_after.append(word)

        alphabetically_sorted = sorted(words_after)
        length_sorted = sorted(words_after, key=len)

        return alphabetically_sorted, length_sorted


def ex_18(number):
        return str(number).count('0')


def ex_19(L):
        word_L = ''
        for num in L:
            str_num = str(num).zfill(3)     #zamienia na string i uzupelnia zerami
            word_L += str_num

        return word_L



#---------------------- main -----------------------


line = ("Lorem ipsum dolor sit amet,\n consectetur adipiscing elit.\n "
        "Nunc suscipit porta est,\n sed ultricies dui posuere condimentum.")

word = "Lorem"

L = [1, 37, 80, 5, 9, 18, 63, 29, 151]

line_gvr = "GvR"

large_number = 130531090160870


print("Zadanie 10: \n", ex_10(line))
print("\nZadanie 11: \n", ex_11(word))
print("\nZadanie 12: \n", ex_12(line))
print("\nZadanie 13: \n", ex_13(line))
print("\nZadanie 14: \n", ex_14(line))
print("\nZadanie 15: \n", ex_15(L))
print("\nZadanie 16: \n", ex_16(line_gvr))
print("\nZadanie 17: \n", ex_17(line))
print("\nZadanie 18: \n", ex_18(large_number))
print("\nZadanie 19: \n", ex_19(L))


