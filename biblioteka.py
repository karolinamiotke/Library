ksiazki = [
    {"id": 1, "tytul": "Lalka", "autor": "Bolesław Prus", "rok": 1890, "strony": 700, "ilosc": 3},
    {"id": 2, "tytul": "Pan Tadeusz", "autor": "Adam Mickiewicz", "rok": 1834, "strony": 340, "ilosc": 2},
    {"id": 3, "tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok": 1866, "strony": 500, "ilosc": 4},
    {"id": 4, "tytul": "Dziady", "autor": "Adam Mickiewicz", "rok": 1822, "strony": 400, "ilosc": 2},
    {"id": 5, "tytul": "Chłopi", "autor": "Władysław Reymont", "rok": 1904, "strony": 450, "ilosc": 3},
    {"id": 6, "tytul": "Krzyżacy", "autor": "Henryk Sienkiewicz", "rok": 1900, "strony": 520, "ilosc": 5},
    {"id": 7, "tytul": "Potop", "autor": "Henryk Sienkiewicz", "rok": 1886, "strony": 700, "ilosc": 4},
    {"id": 8, "tytul": "Ogniem i mieczem", "autor": "Henryk Sienkiewicz", "rok": 1884, "strony": 600, "ilosc": 3},
    {"id": 9, "tytul": "Quo Vadis", "autor": "Henryk Sienkiewicz", "rok": 1896, "strony": 560, "ilosc": 2},
    {"id": 10, "tytul": "W pustyni i w puszczy", "autor": "Henryk Sienkiewicz", "rok": 1911, "strony": 300, "ilosc": 5},
    {"id": 11, "tytul": "Kamienie na szaniec", "autor": "Aleksander Kamiński", "rok": 1943, "strony": 200, "ilosc": 3},
    {"id": 12, "tytul": "Ferdydurke", "autor": "Witold Gombrowicz", "rok": 1937, "strony": 280, "ilosc": 3},
    {"id": 13, "tytul": "Solaris", "autor": "Stanisław Lem", "rok": 1961, "strony": 300, "ilosc": 4},
    {"id": 14, "tytul": "Bajki robotów", "autor": "Stanisław Lem", "rok": 1964, "strony": 260, "ilosc": 2},
    {"id": 15, "tytul": "1984", "autor": "George Orwell", "rok": 1949, "strony": 328, "ilosc": 4},
    {"id": 16, "tytul": "Rok 1984", "autor": "George Orwell", "rok": 1949, "strony": 330, "ilosc": 3},
    {"id": 17, "tytul": "Folwark zwierzęcy", "autor": "George Orwell", "rok": 1945, "strony": 150, "ilosc": 4},
    {"id": 18, "tytul": "Mały Książę", "autor": "Antoine de Saint-Exupéry", "rok": 1943, "strony": 120, "ilosc": 5},
    {"id": 19, "tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok": 1997, "strony": 320, "ilosc": 5},
    {"id": 20, "tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok": 1937, "strony": 310, "ilosc": 3},
    {"id": 21, "tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok": 1954, "strony": 1000, "ilosc": 2},
    {"id": 22, "tytul": "Gra o tron", "autor": "George R.R. Martin", "rok": 1996, "strony": 850, "ilosc": 2},
    {"id": 23, "tytul": "Dziewczyna z pociągu", "autor": "Paula Hawkins", "rok": 2015, "strony": 320, "ilosc": 3},
    {"id": 24, "tytul": "Zaginiona dziewczyna", "autor": "Gillian Flynn", "rok": 2012, "strony": 400, "ilosc": 2},
    {"id": 25, "tytul": "Inferno", "autor": "Dan Brown", "rok": 2013, "strony": 450, "ilosc": 3},
]

def wyswietl_ksiazki():
    print("\n--- Lista książek ---")
    for ksiazka in ksiazki:
        print(f"ID: {ksiazka['id']}, Tytuł: {ksiazka['tytul']}, Autor: {ksiazka['autor']}, Rok: {ksiazka['rok']}, Strony: {ksiazka['strony']}, Ilość: {ksiazka['ilosc']}")

def dodaj_ksiazke():
    print("\n--- Dodawanie książki ---")
    tytul = input("Tytuł: ")
    autor = input("Autor: ")
    rok = int(input("Rok wydania: "))
    strony = int(input("Liczba stron: "))
    ilosc = int(input("Ilość egzemplarzy: "))
    nowe_id = max(k["id"] for k in ksiazki) + 1 if ksiazki else 1
    ksiazki.append({"id": nowe_id, "tytul": tytul, "autor": autor, "rok": rok, "strony": strony, "ilosc": ilosc})
    print("Książka została dodana.")

def edytuj_ksiazke():
    print("\n--- Edycja książki ---")
    try:
        id_ksiazki = int(input("Podaj ID książki do edycji: "))
        for ksiazka in ksiazki:
            if ksiazka["id"] == id_ksiazki:
                ksiazka["tytul"] = input(f"Nowy tytuł ({ksiazka['tytul']}): ") or ksiazka['tytul']
                ksiazka["autor"] = input(f"Nowy autor ({ksiazka['autor']}): ") or ksiazka['autor']
                ksiazka["rok"] = int(input(f"Nowy rok ({ksiazka['rok']}): ") or ksiazka['rok'])
                ksiazka["strony"] = int(input(f"Nowa liczba stron ({ksiazka['strony']}): ") or ksiazka['strony'])
                ksiazka["ilosc"] = int(input(f"Nowa ilość ({ksiazka['ilosc']}): ") or ksiazka['ilosc'])
                print("Książka została zaktualizowana.")
                return
        print("Nie znaleziono książki o podanym ID.")
    except ValueError:
        print("Błąd: ID musi być liczbą.")

def usun_ksiazke():
    print("\n--- Usuwanie książki ---")
    try:
        id_ksiazki = int(input("Podaj ID książki do usunięcia: "))
        for ksiazka in ksiazki:
            if ksiazka["id"] == id_ksiazki:
                ksiazki.remove(ksiazka)
                print("Książka została usunięta.")
                return
        print("Nie znaleziono książki o podanym ID.")
    except ValueError:
        print("Błąd: ID musi być liczbą.")