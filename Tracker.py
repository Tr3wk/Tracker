import sqlite3
from datetime import datetime
import json
from json import load, dump
from rich.console import Console
from rich.table import Table
console = Console()

def inicjalizacja_bazy():
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wpisy(
        nazwa TEXT,
        opis TEXT,
        czas TEXT,
        data TEXT
                )               
                ''')
    baza.commit()
    baza.close()

def dodaj_wpis():
    nazwa = input("Nazwa twojej aktywności (jedno słowo): ")
    opis = input("Opis twojej aktywności: ")
    czas = input("Czas trawnia aktywności: ")
    data = datetime.now().strftime("%Y-%m-%d")
    dane = (nazwa, opis, czas, data)
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()
    cursor.execute("INSERT INTO wpisy (nazwa, opis, czas, data) VALUES (?, ?, ?, ?)", dane)
    baza.commit()
    baza.close()

def odczyt_wpisow():
    choice2 = input("1. Zobacz wszytskie,\n2. Zobacz po dacie ")
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()

    if choice2 == "1":
        try:
            tabela = Table(title='Wpisy', show_header=True, header_style='bold magenta')
            tabela.add_column("Nazwa", style="bold yellow")
            tabela.add_column('Opis', style="bold yellow")
            tabela.add_column('Czas', style="bold yellow")
            tabela.add_column('Data', style="dim")
            cursor.execute("SELECT nazwa, opis, czas, data FROM wpisy")
            wpisy = cursor.fetchall()
            for wpis in wpisy:
                nazwa = str(wpis[0])
                opis = str(wpis[1])
                czas = str(wpis[2])
                data = str(wpis[3])
                tabela.add_row(nazwa, opis, czas, data)

            console.print(tabela)
        except FileNotFoundError:
            print("Brak wpisów, zacznij od dodania pierwszego wpisu")
    elif choice2 == "2":
        data = input("z jakiego nia chcesz zoabczyć wpisy (format daty: RRRR-MM-DD)")
        tabela = Table(title='Wpisy', show_header=True, header_style='bold magenta')
        tabela.add_column("Nazwa", style="bold yellow")
        tabela.add_column('Opis', style="bold yellow")
        tabela.add_column('Czas', style="bold yellow")
        tabela.add_column('Data', style="dim")
        cursor.execute("SELECT nazwa, opis, czas, data FROM wpisy WHERE data = ?", (data,))
        wpisy = cursor.fetchall()
        for wpis in wpisy:
            nazwa = str(wpis[0])
            opis = str(wpis[1])
            czas = str(wpis[2])
            data = str(wpis[3])
            tabela.add_row(nazwa, opis, czas, data)

        console.print(tabela)

def usuniecie_wpisu():
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()
    nazwa_usun = input("Wpis o jakiej nazwie usunąć")
    cursor.execute("DELETE FROM wpisy WHERE nazwa = ?", (nazwa_usun,))
    baza.commit()
    baza.close()
