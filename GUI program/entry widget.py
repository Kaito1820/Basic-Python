from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " + username)
    # entry.config(state=DISABLED)

def delete():
    entry.delete(0,END) #entry.delete(index begin, index end)


def backspace():
    entry.delete(len(entry.get())-1,END)

window = Tk()

entry = Entry(window,
              font=('Arial', 50),
              fg="#00ff00",
              bg='black',
              show='*' #use for password
             )
# entry.insert(0,"Write something")
entry.pack(side = LEFT)

submit_button = Button(window,text='submit', command = submit)
submit_button.pack(side = RIGHT)


delete_button = Button(window, text='delete',command=delete)
delete_button.pack(side = RIGHT)

backspace_button = Button(window, text='backspace',command=backspace)
backspace_button.pack(side = RIGHT)


window.mainloop()