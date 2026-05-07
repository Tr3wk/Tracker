from json import load, dump
from datetime import datetime


with open('PersonalTracker/Tracker.json', "r") as plik:
    zawartosc = load(plik)
    print(zawartosc)
    for wpisy in zawartosc.get("wpisy", []):
        print(wpisy)

nazwa = input("Nazwa twojej aktywności (jedno słowo): ")
opis = input("Opis twojej aktywności: ")
czas = input("Czas trawnia aktywności: ")
data = datetime.now().strftime("%Y-%m-%d")
zawartosc["wpisy"].append({
    "nazwa": nazwa,
    "opis": opis,
    "czas": czas,
    "data": data
})
with open('PersonalTracker/Tracker.json', "a") as out_plik:
    dump(zawartosc, out_plik, indent=4 )