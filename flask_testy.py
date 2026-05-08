from flask import Flask
from flask import render_template
import sqlite3
from datetime import datetime
import json
from json import load, dump
from rich.console import Console
from rich.table import Table
console = Console()
app = Flask(__name__)

@app.route('/')
def index():
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()
    cursor.execute("SELECT nazwa, opis, czas, data FROM wpisy")
    wpisy = cursor.fetchall()
    baza.close()
    return render_template('index.html', wpisy = wpisy )

if __name__ == '__main__':
    app.run(debug=True)
