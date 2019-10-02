import sqlite3
import datetime
import calendar
from pathlib import Path
def calculate_total(Bank_Transactions):

    total = 0
    for i in Bank_Transactions:
        curr = str(i['amount'])
        if "-" in curr:
            curr = float(curr[1:])
            total += curr

    return total

def get_tag_total(tag, Bank_Transactions):

    total = 0
    for transaction in Bank_Transactions:
        if transaction['tag']==tag:
            curr = str(transaction['amount'])
            curr = float(curr[1:])
            total += curr

    return(f"{total:.2f}")

def get_first_and_last(c):
    # Get the first row from database
    c.execute("SELECT date FROM Bank_Transactions LIMIT 1")

    most_recent_date = datetime.datetime.strptime(c.fetchone()[0], '%Y-%m-%d')
    most_recent_date = most_recent_date.date()


    # Get the last row from the database (this works if table is already ordered)
    c.execute("SELECT date FROM Bank_Transactions ORDER BY date ASC LIMIT 1")

    least_recent_date = datetime.datetime.strptime(c.fetchone()[0], '%Y-%m-%d')
    least_recent_date = least_recent_date.date()

    return most_recent_date, least_recent_date

def get_date_intervals(c):

    most_recent_date, least_recent_date = get_first_and_last(c)

    month_end = calendar.monthrange(most_recent_date.year, most_recent_date.month)[1]

    stop_date = most_recent_date.replace(day=month_end)
    stop_date = stop_date + datetime.timedelta(days=1)

    least_recent_date = least_recent_date.replace(day = 1)
    curr = least_recent_date

    intervals = []

    while True:

        last = curr
        curr = curr + datetime.timedelta(days=7)
        check = curr + datetime.timedelta(days=7)
        if check.month != last.month:
            diff = calendar.monthrange(curr.year, curr.month)[1] - int(last.day)
            curr = last + datetime.timedelta(days=diff+1)

        if curr >= stop_date:
            last = last + datetime.timedelta(days=1)
            intervals.append([last,curr])
            break
        else:
            last = last + datetime.timedelta(days=1)
            intervals.append([last,curr])

    return intervals

def get_monthly_totals():

    db_file = Path("src/new.db")
    with sqlite3.connect(db_file) as connection:
        c = connection.cursor()
        intervals = get_date_intervals(c)

        weeks = []
        for date_interval in intervals:
            date_1 = date_interval[0]
            date_2 = date_interval[1]

            c.execute("SELECT * FROM Bank_Transactions WHERE \
                        card = 'DEBIT CARD PURCHASE FROM' AND \
                        date(date) BETWEEN ? AND ?", (date_1, date_2))

            Bank_Transactions = [dict(date=row[0],amount=row[3], tag=row[5])
                                    for row in c.fetchall()]

            week = dict(month=date_1.strftime('%B'),
                        year=date_1.strftime('%Y'), dates=f"{date_1} to {date_2}",
                        takeaways=get_tag_total("Takeaways", Bank_Transactions),
                        groceries=get_tag_total("Groceries", Bank_Transactions),
                        health_shops=get_tag_total("Health Shops", Bank_Transactions),
                        petrol=get_tag_total("Petrol", Bank_Transactions),
                        animal_related=get_tag_total("Animal Related", Bank_Transactions),
                        other=get_tag_total("Other", Bank_Transactions),
                        uncategorized=get_tag_total("Uncategorized", Bank_Transactions),total=f"{(calculate_total(Bank_Transactions)):.2f}")
            weeks.append(week)

    months = []
    week_1, week_2, week_3, week_4 = ([] for i in range(4))

    total = 0
    while len(weeks) != 0:

        month = dict(month=f"{weeks[0]['month']} {weeks[0]['year']}")

        total += float(weeks[0]['total'])
        month['week_1']=weeks.pop(0)

        total += float(weeks[0]['total'])
        month['week_2']=weeks.pop(0)

        total += float(weeks[0]['total'])
        month['week_3']=weeks.pop(0)

        total += float(weeks[0]['total'])
        month['week_4']=weeks.pop(0)

        month['month_total']=f"{total:.2f}"

        months.append(month)
        total = 0

    general_intervals = [[intervals[i][j].day for j in range(2)] for i in range(4)]

    return months, general_intervals

def main():
    get_monthly_totals()

if __name__ == "__main__":
    main()
