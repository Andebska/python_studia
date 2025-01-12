from Polynomial import *

def display_menu():
    print("\nMenu:")
    print("1. Dodaj wielomian")
    print("2. Odejmij wielomian")
    print("3. Pomnóż wielomian")
    print("4. Oblicz wartość wielomianu dla x")
    print("5. Wyświetl wielomian")
    print("6. Porównaj wielomiany")
    print("7. Odczytaj współczynnik przy potędze x")
    print("0. Wyjdź")

def input_polynomial(prompt="Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):"):
    coeffs = input(prompt).strip().split()
    try:
        return Polynomial([int(c) if c.isdigit() else float(c) for c in coeffs])
    except ValueError:
        print("Błąd: Współczynniki muszą być liczbami.")
        return input_polynomial(prompt)

def main():
    print("Interaktywny program obsługi wielomianów")

    while True:
        display_menu()
        choice = input("Wybierz opcję: ")

        if choice == "0":
            print("Do zobaczenia!")
            break

        elif choice == "1":
            print("Dodawanie wielomianów")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p1 = input_polynomial("Podaj pierwszy wielomian: ")
            p2 = input_polynomial("Podaj drugi wielomian: ")
            result = p1 + p2
            print(f"Wynik: {result}")

        elif choice == "2":
            print("Odejmowanie wielomianów")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p1 = input_polynomial("Podaj pierwszy wielomian: ")
            p2 = input_polynomial("Podaj drugi wielomian: ")
            result = p1 - p2
            print(f"Wynik: {result}")

        elif choice == "3":
            print("Mnożenie wielomianów")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p1 = input_polynomial("Podaj pierwszy wielomian: ")
            p2 = input_polynomial("Podaj drugi wielomian: ")
            result = p1 * p2
            print(f"Wynik: {result}")

        elif choice == "4":
            print("Obliczanie wartości wielomianu")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p = input_polynomial()
            try:
                x = float(input("Podaj wartość x: "))
                result = p(x)
                print(f"Wartość wielomianu dla x={x}: {result}")
            except ValueError:
                print("Błąd: x musi być liczbą.")

        elif choice == "5":
            print("Wyświetlanie wielomianu")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p = input_polynomial()
            print(f"Wielomian: {p}")

        elif choice == "6":
            print("Porównywanie wielomianów")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p1 = input_polynomial("Podaj pierwszy wielomian: ")
            p2 = input_polynomial("Podaj drugi wielomian: ")
            if p1 == p2:
                print("Wielomiany są równe.")
            else:
                print("Wielomiany są różne.")

        elif choice == "7":
            print("Odczytywanie współczynnika przy potędze x")
            print("Podaj współczynniki wielomianu oddzielone spacjami (od najniższego stopnia):")
            p = input_polynomial()
            try:
                index = int(input("Podaj potęgę x: "))
                coeff = p[index]
                print(f"Współczynnik przy x^{index}: {coeff}")
            except ValueError:
                print("Błąd: Potęga musi być liczbą całkowitą.")
            except IndexError:
                print("Błąd: Potęga nie może być ujemna.")

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main()