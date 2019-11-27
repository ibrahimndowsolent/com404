# gui.py

from tkinter import *

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Songmaker")
        self.configure(padx=10, pady=10)
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        #self.__add_tickets_entry()
        self.__add_addd_entry()
        #self.__add_add_button()
        
    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        # layout
        self.heading_label.grid(row=0, column=0)
        # style
        self.heading_label.configure(   font="Arial 24", 
                                        text="Songmaker")
        
    def __add_instruction_label(self):
        # create
        self.instruction_label = Label()
        # layout
        self.instruction_label.grid(row=1, column=0, sticky=W)
        # style
        self.instruction_label.configure(text="Lyrics to add:")
        
        
# main.py


my_gui = Gui()
my_gui.mainloop()