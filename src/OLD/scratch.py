c.execute("CREATE TABLE Bank_Transactions(date DATE, \
            name TEXT, card TEXT, amount INT, \
            amount_left FLOAT)")

c.executemany("INSERT INTO Bank_Transactions(date, name, card, \
            amount, amount_left) values(?, ?, ?, ?, ?)" \
            bank_trans)

c.execute("CREATE TABLE Bank_Transactions_curr(date DATE, \
        name TEXT, card TEXT, amount INT, amount_left FLOAT)")

c.execute("INSERT INTO Bank_Transactions_curr(date, name, card,\
            amount, amount_left) SELECT * FROM Bank_Transactions \
            ORDER BY date DSC")

c.execute("DROP TABLE Bank_Transactions")
c.execute("ALTER TABLE Bank_Transactions_curr  \
            RENAME TO Bank_Transactions")
