from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(width=300, height=300)

input = Entry(width=10)
input.grid(column=1, row=0)

label1 = Label(text="is equal to")
label1.grid(column=0, row=1)
label1.config(padx=10, pady=10)

label2 = Label(text="Km")
label2.grid(column=2, row=1)
label2.config(padx=10, pady=10)

label3 = Label(text="0")
label3.grid(column=1, row=1)
label3.config(padx=10, pady=10)

def output():
    miles = float(input.get())
    kms = miles*1.609
    label3.config(text=f"{kms}")


button = Button(text="calculate", command = output)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

label = Label(text="Miles")
label.grid(column=2, row=0)
label.config(padx=10, pady=10)

window.mainloop()