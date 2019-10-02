import csv
import sqlite3
from glob import glob
import os
from src.add_tags import add_tags
import sys
files_added = 0
files_already_added = 0

def export_to_database(path):
    """Reads the csv files and adds the files to a database.
    Also checks if files have already been added.
    """

    global files_added
    global files_already_added
    possible_csv_files = glob(os.path.join(path, "*.csv"))
    possible_csv_processed_files = glob(os.path.join(path, "*_processed.csv"))
    for file in possible_csv_files:

        if file not in possible_csv_processed_files:
            files_added += 1
            export(file)

        else:
            files_already_added += 1
        sys.stdout.write(f"\rFiles added to database: {files_added} --- " \
                f"Files that are already in database: {files_already_added}")
    print()
    sort_database()

def export(file):
    """Exports the csv file to a database"""
    with sqlite3.connect(r"C:\Users\Study\Documents\Budget_project\src\new.db")\
        as connection:

        c = connection.cursor()
        # Get the count of the tables with the name
        c.execute("SELECT count(name) FROM sqlite_master WHERE \
                type='table' AND name='Bank_Transactions'")

        # If the count is one, then the table exists
        if c.fetchone()[0] == 1:
            pass

        else:
            c.execute("CREATE TABLE Bank_Transactions(date DATE, \
                        name TEXT, card TEXT, amount INT, \
                        amount_left FLOAT, tag TEXT)")


        input_file = open(file, 'r')
        reader = csv.reader(input_file)

        c.executemany("INSERT INTO Bank_Transactions(date, name, card, \
                    amount, amount_left) values(?, ?, ?, ?, ?)", \
                    reader)

        input_file.close()
        new_name = file[:-4] + "_processed.csv"
        os.rename(file, new_name)

    add_tags()

def sort_database():
    """Sorts the database by date in decending order"""
    with sqlite3.connect(r"C:\Users\Study\Documents\Budget_project\src\new.db")\
        as connection:
        c = connection.cursor()
        c.execute("CREATE TABLE Bank_Transactions_curr(date DATE, \
                name TEXT, card TEXT, amount INT, amount_left FLOAT, \
                tag TEXT)")

        c.execute("INSERT INTO Bank_Transactions_curr(date, name, card,\
                    amount, amount_left, tag) SELECT * FROM Bank_Transactions \
                    ORDER BY date DESC")

        c.execute("DROP TABLE Bank_Transactions")

        c.execute("ALTER TABLE Bank_Transactions_curr  \
                    RENAME TO Bank_Transactions")

        c.execute("DELETE FROM Bank_Transactions WHERE rowid NOT IN \
                    (SELECT min(rowid) FROM Bank_Transactions GROUP BY \
                    date,name,card,amount)")


def main():
    path = r"C:\Users\Study\Documents\budget_project\cache\csv"
    export_to_database(path)

if __name__ == "__main__":
    main()
