from tkinter import *
from tkinter import ttk

# window = Tk()
# window.title("MHealth Care System")
# window.geometry('400x400')
# window.configure(background = "grey");
# a = Label(window,text = "First Name").grid(row = 0,column = 0)
# b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
# c = Label(window ,text = "Email Id").grid(row = 2,column = 0)
# d = Label(window ,text = "Contact Number").grid(row = 3,column = 0)
# a1 = Entry(window).grid(row = 0,column = 1)
# b1 = Entry(window).grid(row = 1,column = 1)
# c1 = Entry(window).grid(row = 2,column = 1)
# d1 = Entry(window).grid(row = 3,column = 1)
def add_entry():
   pass

def main_page():
   window = Tk()
   window.title("MHealth Care System")
   window.geometry('325x250')
   window.configure(background = "gray")
   main_frame = Frame(window)
   main_frame.pack()
   Label(main_frame, text="Welcome to MHealth System").grid(row=0, column=0, sticky=W)
   register_frame = Frame(window)       # Row of buttons
   register_frame.pack()
   register_frame = Button(register_frame, text="Register", command=register)
   register_frame.pack(side = BOTTOM)
   return window

def register():
    global fnamevar, lnamevar, phonevar, select

    frame1 = Frame(window)
    frame1.pack()

    Label(frame1, text="First Name").grid(row=0, column=0, sticky=W)
    fnamevar = StringVar()
    fname = Entry(frame1, textvariable=fnamevar)
    fname.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Last Name").grid(row=1, column=0, sticky=W)
    lnamevar = StringVar()
    lname = Entry(frame1, textvariable=lnamevar)
    lname.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Phone").grid(row=2, column=0, sticky=W)
    phonevar = StringVar()
    phone = Entry(frame1, textvariable=phonevar)
    phone.grid(row=2, column=1, sticky=W)

    frame2 = Frame(window)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2, text="submit", command=add_entry)
    # b2 = Button(frame2, text="Update", command=update_entry)
    # b3 = Button(frame2, text="Delete", command=delete_entry)
    # b4 = Button(frame2, text="Load  ", command=load_entry)
    #b5 = Button(frame2, text="Refresh", command=set_select)
    b1.pack(side=LEFT)
    # b2.pack(side=LEFT)
    # b3.pack(side=LEFT)
    # b4.pack(side=LEFT)
    # b5.pack(side=LEFT)

    # frame3 = Frame(win)       # select of names
    # frame3.pack()
    # scroll = Scrollbar(frame3, orient=VERTICAL)
    # select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    # scroll.config(command=select.yview)
    # scroll.pack(side=RIGHT, fill=Y)
    # select.pack(side=LEFT, fill=BOTH, expand=1)
    #return window

if __name__ == '__main__':
   window = main_page()
   window.mainloop()
