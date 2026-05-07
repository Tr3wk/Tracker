from datetime import datetime
import json
from json import load, dump

def dodaj_wpis():
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

def odczyt_wpisow():
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

def usuniecie_wpisu():
    nazwa_usun = input("Wpis o jakiej nazwie usunąć")
    try:
        with open('PersonalTracker/Tracker.json', 'r') as plik:
            zawartosc = json.load(plik)
        zawartosc["wpisy"] = [wpis for wpis in zawartosc["wpisy"] if wpis["nazwa"] != nazwa_usun]
        with open('PersonalTracker/Tracker.json', 'w') as out_plik:
            json.dump(zawartosc, out_plik, indent=4)
    except FileNotFoundError:
        print("Brak wpisów, zacznij od dodania pierwszego wpisu")
