import sqlite3

def add_tags():
    """Adds tags to each transaction in database so that it can be catagorised.
    """
    with sqlite3.connect(r"C:\Users\Study\Documents\Budget_project\src\new.db")\
        as connection:

        c = connection.cursor()

        c.execute("""UPDATE Bank_Transactions SET tag = "Takeaways" WHERE
                    name LIKE '%mcd%'
                    OR name LIKE '%nandos%'
                    OR name LIKE '%mugg%'
                    OR name LIKE '%mochachos%'
                    OR name LIKE '%seattle%'
                    OR name LIKE '%rocco%'
                    OR name LIKE '%wimpy%'
                    OR name LIKE '%cafe%'
                    OR name LIKE '%pizza%'
                    OR name LIKE '%restaurant%'
                    OR name LIKE '%popeyes%'
                    OR name LIKE '%yume%'
                    OR name LIKE '%col cacchio%'
                    OR name LIKE '%banjaara%'
                    OR name like '%kitchen%'
                    OR name like '%papachinos%'
                    OR name like '%kfc%'
                    OR name like '%debonairs%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Groceries" WHERE
                    name LIKE '%woolworths%'
                    OR name like '%meat%'
                    OR name like '%spar%'
                    OR name like '%pnp%'
                    OR name like '%checkers%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Health Shops" WHERE
                    name LIKE '%clicks%'
                    OR name like '%dis-chem%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Petrol" WHERE
                    name LIKE '%cltx%'
                    OR name like '%sasol%'
                    OR name like '%total%'
                    OR name like '%shell%'
                    OR name like '%caltex%'
                    OR name like '%bp%'
                    OR name like '%engen%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Animal Related" WHERE
                    name LIKE '%pet%'
                    OR name like '%jungle%'
                    OR name like '%animal%'
                    OR name like '%vet%'
                    OR name like '%reptilians%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Other" WHERE
                    name LIKE '%ster kinekor%'
                    OR name like '%plastic%'
                    OR name like '%builders%'
                    OR name like '%makro%'
                    OR name like '%lifestyle%'
                    OR name like '%garden%'
                    OR name like '%BERLINER%'
                    """)

        c.execute("""UPDATE Bank_Transactions SET tag = "Uncategorized" WHERE
                    tag IS NULL AND card == "DEBIT CARD PURCHASE FROM"
                    """)

def main():
    add_tags()

if __name__ == "__main__":
    main()
