from datetime import datetime

while True:
    print("Witaj w Personal Tracker! co chcesz dzisiaj zrobić?")
    print("1. Dodać nowy wpis")
    print("2. Wyświetlić wszystkie wpisy")
    print("3. Wyjść")
    choice = input("Wybierz opcję: ")
    if choice == "1":
        Nazwa = input("Nazwa twojej aktywności (jedno słowo): ")
        Opis = input("Opis twojej aktywności: ")
        Czas = input("Czas trawnia aktywności: ")
        data = datetime.now().strftime("%Y-%m-%d")
        with open(f"{data}-{Nazwa}.txt", "a") as plik:
            plik.write(data)
            plik.write(f"\n{Nazwa}")
            plik.write(f"\n{Czas}")
            plik.write(f"\n{Opis}")

