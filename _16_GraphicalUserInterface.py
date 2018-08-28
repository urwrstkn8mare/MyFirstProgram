# Work In Progress
# This is just to mess around with differents GUI's I find on the internet


from tkinter import *
from _15_BinaryConverterAndStuff import *


def dec2bin_gui():
    def calculate():
        global master
        calculated = dec2bin(e1.get())
        result = str(e1.get()) + ' -> ' + str(calculated)
        Label(master, text=result).grid(row=0)
        e1.grid_forget()
        b.grid_forget()
        l.grid_forget()
        b2 = Button(master, text='Quit', command=master.quit)
        b2.grid(row=1, column=0, sticky=W, pady=4)
        return

    master = Tk()
    master.title('dec2bin')
    master.geometry("300x70")
    master.pack_propagate()
    l = Label(master, text="Decimal")
    l.grid(row=0)
    e1 = Entry(master)
    e1.grid(row=0, column=1)
    b = Button(master, text='Calculate', command=calculate)
    b.grid(row=1, column=0, pady=4)
    mainloop()
    return

    
def run():
    dec2bin_gui()


if __name__ == '__main__':
    run()


