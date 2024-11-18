from tkinter import *

def button_clicked():
    miles = float(input.get())
    km = miles * 1.609
    mile_to_km.config(text=km)

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300, 300)

window.config(padx=100, pady=100)

#Label
my_label = Label(text="is equal to ", font=("Helvetica", 13, "normal"))
my_label.grid(column=0, row=3)
my_label.config(padx=5, pady=5)

km_label = Label(text="Km", font=("Helvetica", 13, "normal"))
km_label.grid(column=4, row=3)
km_label.config(padx=5, pady=5)

mile_label = Label(text="Miles", font=("Helvetica", 13, "normal"))
mile_label.grid(column=3, row=2)


mile_to_km = Label(text="0", font=("Helvetica", 13, "normal"))
mile_to_km.grid(column=1, row=3)

#Button

button = Button(text="Calculate", command=button_clicked, width=10, height=1)
button.grid(column=1, row=4)



#Entry

input = Entry(width=10)
input.get()
print(input.get())
input.grid(column= 1, row=2)








window.mainloop()