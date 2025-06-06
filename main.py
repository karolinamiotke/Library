import biblioteka
import student
import wypozyczenia

def main_menu():
    while True:
        print("\n=== SYSTEM BIBLIOTECZNY ===")
        print("1. Lista książek")
        print("2. Dodaj książkę")
        print("3. Edytuj książkę")
        print("4. Usuń książkę")
        print("5. Lista studentów")
        print("6. Dodaj studenta")
        print("7. Wypożycz książkę")
        print("8. Zwróć książkę")
        print("9. Raport przypomnień")
        print("0. Wyjście")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            biblioteka.wyswietl_ksiazki()
        elif wybor == "2":
            biblioteka.dodaj_ksiazke()
        elif wybor == "3":
            biblioteka.edytuj_ksiazke()
        elif wybor == "4":
            biblioteka.usun_ksiazke()
        elif wybor == "5":
            student.wyswietl_studentow()
        elif wybor == "6":
            student.dodaj_studenta()
        elif wybor == "7":
            try:
                student_id = int(input("Podaj ID studenta: "))
                ksiazka_id = int(input("Podaj ID książki: "))
                wypozyczenia.wypozycz_ksiazke(student.studenci, biblioteka.ksiazki, student_id, ksiazka_id)
            except ValueError:
                print("Nieprawidłowe dane wejściowe. Podaj liczby całkowite.")
        elif wybor == "8":
            try:
                student_id = int(input("Podaj ID studenta: "))
                ksiazka_id = int(input("Podaj ID książki do zwrotu: "))
                wypozyczenia.zwroc_ksiazke(student.studenci, biblioteka.ksiazki, student_id, ksiazka_id)
            except ValueError:
                print("Nieprawidłowe dane wejściowe. Podaj liczby całkowite.")

        elif wybor == "9":
            wypozyczenia.raport_przypomnien(student.studenci)
        elif wybor == "0":
            print("Do widzenia!")
            break
        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")

if __name__ == "__main__":
    main_menu()
