import sqlite3
from rich.table import Table
from rich.console import Console
console = Console()


def odczyt_wpisow2():
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

 