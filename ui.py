from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from database import init_db

def display_entries():
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entries")
    entries = cursor.fetchall()

    custom_theme = Theme({
        "info": "dim cyan",
        "warning": "bold yellow",
        "error": "bold red"
    })
    console = Console(theme=custom_theme)
    table = Table(title="Reading Tracker")

    table.add_column("ID", justify="right")
    table.add_column("Type", justify="right")
    table.add_column("Title", justify="left")
    table.add_column("Link", justify="left")
    table.add_column("Tags", justify="right")
    table.add_column("Added Date", justify="right")

    for entry in entries:
        table.add_row(str(entry[0]), entry[1], entry[2], entry[3], entry[4], entry[5])
    
    console.print(table)

if "__name__"=="__main__":
   display_entries() 
