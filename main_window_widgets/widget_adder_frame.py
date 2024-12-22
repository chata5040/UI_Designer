from functools import partial
from abc import ABC, abstractmethod
import customtkinter as ctk

class WidgetLibrary:
    def __init__(self):
        self._widget_classes = {
            "Button": ctk.CTkButton,
            "Frame": ctk.CTkFrame,
            "Entry": ctk.CTkEntry,
            "Label": ctk.CTkLabel,
            "Slider": ctk.CTkSlider,
            "Textbox": ctk.CTkTextbox,
            "RadioButton": ctk.CTkRadioButton,
            "Switch": ctk.CTkSwitch,
            "CheckBox": ctk.CTkCheckBox,
            "ComboBox": ctk.CTkComboBox,
            "OptionMenu": ctk.CTkOptionMenu,
        }
        self._widget_list = list(self._widget_classes.keys())
    
    @property
    def widget_classes(self):
        return self._widget_classes
    
    @property
    def widget_list(self):
        return self._widget_list

class WidgetAdderFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, select_button_command=None):
        super().__init__(master, corner_radius=0)
        
        if not callable(select_button_command):
            raise ValueError("select_button_command must be a callable function")
        
        self.select_button_command = select_button_command
        self._widget_library = WidgetLibrary()
        self._widget_classes = self._widget_library.widget_classes
        self._widget_list = self._widget_library.widget_list
        self._create_widget_add_buttons()

    def _create_widget_add_buttons(self):
        self._buttons = []
        for widget_name, widget_class in self._widget_classes.items():
            button = ctk.CTkButton(self, text=widget_name, border_width=0,
                                   fg_color="#660066", hover_color="#440044",
                                   command=partial(self._select_button, widget_name, widget_class))
            button.grid(padx=5, pady=5, sticky="ew")
            self._buttons.append(button)

    def _select_button(self, widget_name, widget_class):
        for button in self._buttons:
            button.configure(border_width=2 if button.cget("text") == widget_name else 0)
        
        self.select_button_command(widget_class)
