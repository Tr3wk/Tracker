from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()

    if request.method == 'POST':
        data = datetime.now().strftime("%Y-%m-%d")
        nazwa = request.form['nazwa']
        opis = request.form['opis']
        czas = request.form['czas']
        dane = (nazwa, opis, czas, data)
        cursor.execute("INSERT INTO wpisy (nazwa, opis, czas, data) VALUES (?, ?, ?, ?)", dane)
        baza.commit()
        return redirect(url_for('index'))
        

    cursor.execute("SELECT nazwa, opis, czas, data FROM wpisy")
    wpisy = cursor.fetchall()
    baza.close()
    

    return render_template('index.html', wpisy = wpisy )

@app.route('/usun', methods=['POST'])
def usun():
    baza = sqlite3.connect('PersonalTracker/tracker.db')
    cursor = baza.cursor()
    nazwa_usun = request.form['nazwa_usun']
    cursor.execute("DELETE FROM wpisy WHERE nazwa = ?", (nazwa_usun,))
    baza.commit()
    baza.close()


    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)
