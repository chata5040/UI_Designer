import customtkinter as ctk

from CTkMenuBar import *

class MenuBar():
    def __init__(self, master):
        self.master = master
        
        self.menu_bar = CTkMenuBar(master=self.master)
        self._file_button = self.menu_bar.add_cascade("File")
        self._file_dropdown = CustomDropdownMenu(widget=self._file_button)
        self._file_dropdown.add_option(option="Save as")
        
        self.menu_bar.pack_forget()

