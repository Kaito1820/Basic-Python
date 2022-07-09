from tkinter import *

def display():
    if(x.get() == 1):
        print("You agree!")
    else:
        print("You don't agree")

window = Tk()

# x = IntVar()
# x = StringVar()
x = BooleanVar()
# logo = PhotoImage(file='logo.png')

check_button = Checkbutton(window,
                           text = 'Yes',
                           variable = x,
                        #    onvalue = 1,
                        #    offvalue = 0,
                           onvalue = True,
                           offvalue = False,
                           command = display,
                           font=("Arial",20),
                           fg='#00ff00',
                           bg = 'black',
                           activeforeground='#00ff00',
                           activebackground='black',
                        #    padx=25,
                        #    pad=10,
                        #    image=logo
                        #    commpound=LEFT,
                          )
check_button.pack()

window.mainloop()