from tkinter import *


def button_clicked():
    mile = float(mile_input.get())
    km = round(mile * 1.60934, 4)
    km_output.config(text=f"{km}")

# window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

# Entry
mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

# "Miles" Label
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# "is equal to" label
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# km value Label
km_output = Label(text="0")
km_output.grid(column=1, row=1)

# "Km" Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# "Calculate" Button
calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)

window.mainloop()
