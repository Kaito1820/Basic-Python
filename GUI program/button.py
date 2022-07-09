from tkinter import *
# button = you click it, then it does stuff
count = 0

def click():
    # print("You clicked the button!")
    global count
    count += 1
    print(count)

window = Tk() 

button = Button(window,
                text='click me!',
                command=click,
                font=('Comic Sans', 30),
                fg="#00FF00",
                bg="black",
                activeforeground='#00FF00',
                activebackground='black',
                state = ACTIVE, #trang thai cua nut ACTIVE or DISABLE
                # image = photo,
                # compound = 'top'
                )
button.pack()
window.mainloop()