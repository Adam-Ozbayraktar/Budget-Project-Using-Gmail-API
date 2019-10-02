from datetime import datetime

t = datetime.now()
t_str = t.strftime("%d-%m-%Y")
#print(f"{t.day}-{t.month}-{t.year}")
print(f"The date is: {t_str}")
print(t.strftime("%d-%m-%Y"))
