from tkinter import *
# from PIL import Image
# from PIL import ImageTk

window = Tk() # instantiate an instance of a window, like begin

window.geometry("420x420") # resize the window
window.title("Kaito GUI program")

# icon = PhotoImage(file='logo.png')
# window.iconphoto(True, icon)
window.config(background="#40DFEF")

# photo = PhotoImage(file='D:\\Python\\First GUI program\\logo.png')
# photo = ImageTk.PhotoImage(Image.open("logo.jpg"))

label = Label(window, text = "Hello word",
                      font=('Arial,20,Bold'), 
                      fg='pink', 
                      bg='black',
                      relief=RAISED, #vien xung quanh label, RAISED, SUNKEN  là boder style
                      bd=10, #do day cua vien
                      padx=100, #khoang trong giua vien va chu trong label theo truc X
                      pady=20, # giong o tren nhung truc Y
                    #   image=photo
                    compound='bottom' #photo se xuat hien duoi chu trong label
            )
label.pack()
# label.place(x = 210, y = 210)



window.mainloop() #place window on computer screen, listen for the events, like end



