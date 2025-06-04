from datetime import datetime, timedelta


def wypozycz_ksiazke(studenci, ksiazki, student_id, ksiazka_id):
    student = next((s for s in studenci if s['id'] == student_id), None)
    ksiazka = next((k for k in ksiazki if k['id'] == ksiazka_id), None)
    
    if student is None:
        print("Nie znaleziono studenta.")
        return
    if ksiazka is None:
        print("Nie znaleziono książki.")
        return
    
    if len(student['wypozyczone']) >= 5:
        print("Ten student nie może wypożyczyć więcej niż 5 książek.")
        return
    
    if ksiazka['ilosc'] <= 0:
        print("Brak dostępnych egzemplarzy tej książki.")
        return

    ksiazka['ilosc'] -= 1
    student['wypozyczone'].append({
        'id': ksiazka['id'],
        'tytul': ksiazka['tytul'],
        'data_wypozyczenia': datetime.now()
    })
    print(f"Wypożyczono książkę '{ksiazka['tytul']}' studentowi {student['imie']} {student['nazwisko']}")



def raport_przypomnien(studenci, dni=14):
    print(f"\n--- Raport przypomnień o zwrotach (książki wypożyczone dłużej niż {dni} dni) ---")
    teraz = datetime.now()
    znaleziono = False
    for student in studenci:
        przeterminowane = []
        for ks in student['wypozyczone']:
            if (teraz - ks['data_wypozyczenia']).days > dni:
                przeterminowane.append(ks)
        if przeterminowane:
            znaleziono = True
            print(f"\nStudent: {student['imie']} {student['nazwisko']} (ID: {student['id']})")
            for ks in przeterminowane:
                dni_ = (teraz - ks['data_wypozyczenia']).days
                print(f" - {ks['tytul']}, wypożyczona {dni_} dni temu")
    if not znaleziono:
        print("Brak przeterminowanych wypożyczeń.")
