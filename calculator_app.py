import tkinter as tk

# Funkcija koja će se koristiti za ažuriranje unosa u kalkulatoru
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = str(eval(entry.get()))
            entry_var.set(value)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

# Glavna aplikacija
root = tk.Tk()
root.title("Kalkulator")

# Varijabla koja drži trenutno uneti tekst
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Definiši dugmad
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Dodaj dugmad u mrežu (grid)
row_val = 1
col_val = 0
for button in buttons:
    b = tk.Button(root, text=button, font="Arial 18", padx=20, pady=20)
    b.grid(row=row_val, column=col_val)
    b.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Pokreni glavnu petlju aplikacije
root.mainloop()
