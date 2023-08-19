
# w_h = [x for x in input("Please enter the work hourse:").split()]
# def planet(id):
# operator overloading
import tkinter as tk
from datetime import datetime, timedelta


def calculate_days_remaining():
    try:
        birthday_str = birthday_entry.get()
        birthday_date = datetime.strptime(birthday_str, '%Y-%m-%d')

        today = datetime.today()
        next_birthday = birthday_date.replace(year=today.year)

        if today > next_birthday:
            next_birthday = next_birthday.replace(year=today.year + 1)

        days_remaining = (next_birthday - today).days
        result_label.config(
            text=f"Jours restants jusqu'à Magal Touba: {days_remaining} jours🐄🐔🐏")
    except ValueError:
        result_label.config(
            text="Format de date invalide. Veuillez utiliser AAAA-MM-JJ format.")


# Create the main window
root = tk.Tk()
root.title("Magal Timer")

# Create and place widgets
instructions_label = tk.Label(
    root, text="Entrez la date de Magal Touba sous la forme(AAAA-MM-JJ):")
instructions_label.pack(pady=30)

birthday_entry = tk.Entry(root)
birthday_entry.pack(pady=25)

calculate_button = tk.Button(
    root, text="Calculate", command=calculate_days_remaining)
calculate_button.pack(pady=30)

result_label = tk.Label(root, text="Magal Touba Sunu Yite!!!")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()

# print(dir(str))

# print(dir(int))
