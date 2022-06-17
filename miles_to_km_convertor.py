from tkinter import *


def miles_to_km_conversion():
    miles = float(miles_input.get())
    km = miles * 1.609344
    label_conversion.config(text=km)


#TODO 1: Create Window
window = Tk()
window.title("Mile to km convertor")
window.minsize(width=300, height=200)
window.config(padx=25, pady=25)

#TODO 2: Create button
button = Button(text="Calculate", command=miles_to_km_conversion)
button.grid(column=2, row=4)


#TODO 3: Create entries for miles to be converted
miles_input = Entry(width=10)
miles_input.grid(column=2, row=2)

#TODO 4: Create label for the km
label_km = Label(text="Km")
label_km.grid(column=4, row=3)
label_km.config(padx=10, pady=10)

#TODO 5: Create label for miles
label_miles = Label(text="Miles")
label_miles.grid(column=4, row=2)

#TODO 6: Create label for "is equal to"
label_equal = Label(text="is equal to")
label_equal.grid(column=1, row=3)

#TODO 7: Create empty label to show conversion
label_conversion = Label(text=" ")
label_conversion.grid(column=2, row=3)







window.mainloop()
