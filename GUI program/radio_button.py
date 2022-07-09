from tkinter import *

# radio button = similar to checkbox, but you can only select one from a group

food = ['bread', 'oppla', 'egg']

window = Tk()
x = IntVar()
for i in range(len(food)):
    radio_button = Radiobutton(window, 
                               text = food[i], #adds text to radio button
                               variable=x, #group radiobutton together if they share the same variable
                               value=i, # assigns each radiobutton a different value
                               padx = 25, #adds padding on x-axis
                               font=('Impact', 20)
                              ) 
    radio_button.pack(anchor = W)

window.mainloop()