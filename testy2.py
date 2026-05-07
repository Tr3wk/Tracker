from rich.console import Console
from rich.table import Table
from datetime import datetime
import json
from json import load, dump
console = Console()
def odczyt_wpisow2():
    choice2 = input("1. Zobacz wszytskie,\n2. Zobacz po dacie")
    if choice2 == "1":
        try:
            tabela = Table(title='Wpisy', show_header=True, header_style='bold magenta')
            tabela.add_column("Nazwa", style="bold yellow")
            tabela.add_column('Opis', style="bold yellow")
            tabela.add_column('Czas', style="bold yellow")
            tabela.add_column('Data', style="dim")
            with open('PersonalTracker/Tracker.json', "r") as plik:
                zawartosc = load(plik)
                wpisy = zawartosc['wpisy']
                for wpis in wpisy:
                    nazwa = str(wpis['nazwa'])
                    opis = str(wpis['opis'])
                    czas = str(wpis['czas'])
                    data = str(wpis['data'])
                    tabela.add_row(nazwa, opis, czas, data)
                console.print(tabela)
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