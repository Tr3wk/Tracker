from datetime import datetime
import json

while True:
    print("Witaj w Personal Tracker! co chcesz dzisiaj zrobić?")
    print("1. Dodać nowy wpis")
    print("2. Wyświetlić wszystkie wpisy")
    print("3. Wyjść")
    choice = input("Wybierz opcję: ")
    if choice == "1":
        nazwa = input("Nazwa twojej aktywności (jedno słowo): ")
        opis = input("Opis twojej aktywności: ")
        czas = input("Czas trawnia aktywności: ")
        data = datetime.now().strftime("%Y-%m-%d")
        with open("PersonalTracker/Tracker.txt", "a") as plik:
            plik.write(data)
            plik.write(f"\n{nazwa}")
            plik.write(f"\n{czas}")
            plik.write(f"\n{opis}")
            plik.write("\n---\n")
    elif choice == "2":
        try:
            with open('PersonalTracker/Tracker.txt', "r") as plik:
                print(plik.read())
        except FileNotFoundError:
            print("Brak wpisów, zacznij od dodania pierwszego wpisu")
    elif choice == "3":
        exit()
    else:
        print("Prosze wybrać opcje 1, 2 lub 3")
