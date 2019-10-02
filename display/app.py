from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3
import webbrowser
from display.get_totals import get_monthly_totals
from pathlib import Path
db_file = Path("src/new.db")
DATABASE = db_file

app = Flask(__name__)

app.config.from_object(__name__)

def connection_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/transactions')
def transactions():
    g.db = connection_db()
    cur = g.db.execute('SELECT * FROM Bank_Transactions')
    Bank_Transactions = [dict(date=row[0], name=row[1], card=row[2], amount=row[3], amount_left=row[4]) for row in cur.fetchall()]
    g.db.close()
    return render_template('transactions.html', Bank_Transactions=Bank_Transactions)

@app.route('/weekly-comparisons')
def weekly_comparisons():
    months, general_intervals = get_monthly_totals()
    return render_template('weekly_comparisons.html', months=months, general_intervals=general_intervals)

@app.route('/grouped-comparison')
def grouped_comparison():
    months, general_intervals = get_monthly_totals()
    """
    print(render_template('grouped_comparison.html', months=months, totals=totals))
    text_file = open("output.html", "w")
    text_file.write(render_template('grouped_comparison.html', months=months, totals=totals))
    text_file.close()
    """
    return render_template('grouped_comparison.html', months=months)


@app.route('/main')
def main():
    return render_template('main.html')

def start_app():
    app.run()

def open_browser():
    url = "http://localhost:5000/main"
    webbrowser.open(url)

if __name__ == '__main__':
    app.run(debug=True)
