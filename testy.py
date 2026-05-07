from rich.console import Console
from rich.table import Table

# Inicjalizacja konsoli
console = Console()

# 1. Tworzenie obiektu tabeli
table = Table(title="Lista Studentów", show_header=True, header_style="bold magenta")

# 2. Dodawanie kolumn (styl, justowanie)
table.add_column("ID", style="dim", width=4, justify="center")
table.add_column("Imię i Nazwisko", style="cyan")
table.add_column("Kierunek", justify="right", style="green")
table.add_column("Średnia", justify="right", style="bold yellow")

# 3. Dodawanie wierszy (dane)
table.add_row("001", "Jan Kowalski", "Informatyka", "4.5")
table.add_row("002", "Anna Nowak", "Grafika", "4.8")
table.add_row("003", "Piotr Wiśniewski", "Ekonomia", "3.9")
table.add_row("004", "Maria Dąbrowska", "Informatyka", "5.0")

# 4. Wyświetlenie tabeli w konsoli
console.print(table)
