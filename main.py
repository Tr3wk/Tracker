from datetime import datetime
import json
from json import load, dump

        
while True:

    print("Witaj w Personal Tracker! co chcesz dzisiaj zrobić?")
    print("1. Dodać nowy wpis")
    print("2. Wyświetlić wszystkie wpisy")
    print("3. Usuń wpis")
    print("4. Wyjść")
    choice = input("Wybierz opcję: ")
    if choice == "1":
        nazwa = input("Nazwa twojej aktywności (jedno słowo): ")
        opis = input("Opis twojej aktywności: ")
        czas = input("Czas trawnia aktywności: ")
        data = datetime.now().strftime("%Y-%m-%d")
        try:
            with open("PersonalTracker/Tracker.json", "r") as plik:
                zawartosc = load(plik)
        except FileNotFoundError:
            zawartosc = {"wpisy":[]}
                
        zawartosc["wpisy"].append({
            "nazwa": nazwa,
            "opis": opis,
            "czas": czas,
            "data": data
            })
        
        with open('PersonalTracker/Tracker.json', "w") as out_plik:
            dump(zawartosc, out_plik, indent=4 )
        
    elif choice == "2":
        choice2 = input("1. Zobacz wszytskie,\n2. Zobacz po dacie")
        if choice2 == "1":
            try:
                with open('PersonalTracker/Tracker.json', "r") as plik:
                    zawartosc = load(plik)
                    for wpisy in zawartosc.get('wpisy', []):
                        print(wpisy)
            except FileNotFoundError:
                print("Brak wpisów, zacznij od dodania pierwszego wpisu")
        elif choice2 == "2":
            data = input("z jakiego nia chcesz zoabczyć wpisy (format daty: RRRR-MM-DD)")
            try:
                with open('PersonalTracker/Tracker.json', "r") as plik:
                    zawartosc = load(plik)
                    for wpis in zawartosc['wpisy']:
                        if wpis['data']== data:
                            print(wpis)

            except FileNotFoundError:
                print("Brak wpisów, zacznij od dodania pierwszego wpisu")
    elif choice == "3":
        nazwa_usun = input("Wpis o jakiej nazwie usunąć")
        
    elif choice == "4":
        exit()
    else:
        print("Prosze wybrać opcje 1, 2, 3 lub 4")
