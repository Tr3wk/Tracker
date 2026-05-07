from Tracker import *
from testy2 import *
        
while True:

    print("Witaj w Personal Tracker! co chcesz dzisiaj zrobić?")
    print("1. Dodać nowy wpis")
    print("2. Wyświetlić wszystkie wpisy")
    print("3. Usuń wpis")
    print("4. Wyjść")
    choice = input("Wybierz opcję: ")
    if choice == "1":
        dodaj_wpis()
        
    elif choice == "2":
        odczyt_wpisow()
    elif choice == "3":
        usuniecie_wpisu()

    elif choice == "4":
        exit()
    else:
        print("Prosze wybrać opcje 1, 2, 3 lub 4")
