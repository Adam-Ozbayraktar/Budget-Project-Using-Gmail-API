import os
import csv
import sqlite3

def export(file):
    with sqlite3.connect(r"C:\Users\Study\Documents\Budget_project\src\new.db") as connection:
        c = connection.cursor()

        c.execute("CREATE TABLE temp(garbage TEXT, date DATE, \
                    garbage_2 TEXT,amount INT,card TEXT, name TEXT, \
                    garbage_3 TEXT, garbage_4 TEXT)")

        input_file = open(file, 'r')
        reader = csv.reader(input_file)

        c.executemany("INSERT INTO temp(garbage, date, \
                        garbage_2, amount, card, name, garbage_3, garbage_4)\
                        values(?,?,?,?,?,?,?,?)", reader)

        input_file.close()



        c.execute("UPDATE temp SET date = substr(date, 1, 4) || '-' || substr(date, 5,2) || '-' || substr(date, 7,2)")

        c.execute("DELETE FROM temp WHERE date >= '2019-07-22'")

        c.execute("INSERT INTO Bank_Transactions(date, name, card, amount) SELECT date, name, card, amount FROM temp")

        c.execute("DROP TABLE temp")
def main():
    csv_file = r"C:\Users\Study\Documents\Budget_project\cache\combined.csv"
    #txt_file = os.path.join(file_path, "SBSA_Statement_25-08-2019_0_unecrypted.txt")
    export(csv_file)

if __name__ == "__main__":
    main()
