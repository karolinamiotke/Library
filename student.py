studenci = [
    {"id": 1, "imie": "Anna", "nazwisko": "Kowalska", "wypozyczone": []},
    {"id": 2, "imie": "Piotr", "nazwisko": "Nowak", "wypozyczone": []},
    {"id": 3, "imie": "Kamil", "nazwisko": "Wiśniewski", "wypozyczone": []},
    {"id": 4, "imie": "Magda", "nazwisko": "Wójcik", "wypozyczone": []},
    {"id": 5, "imie": "Tomasz", "nazwisko": "Kowalczyk", "wypozyczone": []},
    {"id": 6, "imie": "Ewa", "nazwisko": "Kamińska", "wypozyczone": []},
    {"id": 7, "imie": "Karol", "nazwisko": "Lewandowski", "wypozyczone": []},
    {"id": 8, "imie": "Zuzanna", "nazwisko": "Zielińska", "wypozyczone": []},
    {"id": 9, "imie": "Mateusz", "nazwisko": "Szymański", "wypozyczone": []},
    {"id": 10, "imie": "Aleksandra", "nazwisko": "Dąbrowska", "wypozyczone": []},
    {"id": 11, "imie": "Jakub", "nazwisko": "Woźniak", "wypozyczone": []},
    {"id": 12, "imie": "Natalia", "nazwisko": "Mazur", "wypozyczone": []},
    {"id": 13, "imie": "Paweł", "nazwisko": "Krawczyk", "wypozyczone": []},
    {"id": 14, "imie": "Julia", "nazwisko": "Kaczmarek", "wypozyczone": []},
    {"id": 15, "imie": "Michał", "nazwisko": "Piotrowski", "wypozyczone": []},
]

def wyswietl_studentow():
    print("\n--- Lista studentów ---")
    if not studenci:
        print("Brak studentów.")
    for s in studenci:
        print(f"ID: {s['id']}, Imię: {s['imie']}, Nazwisko: {s['nazwisko']}")

def dodaj_studenta():
    if len(studenci) >= 15:
        print("Nie można dodać więcej niż 15 studentów.")
        return

    print("\n--- Dodawanie studenta ---")
    imie = input("Imię: ")
    nazwisko = input("Nazwisko: ")
    nowe_id = max([s['id'] for s in studenci], default=0) + 1
    studenci.append({"id": nowe_id, "imie": imie, "nazwisko": nazwisko, "wypozyczone": []})
    print("Student został dodany.")
    