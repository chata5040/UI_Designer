import customtkinter as ctk
from dataclasses import dataclass
from typing import List

@dataclass
class GridConfig:
    index: int
    weight: int = 1  # デフォルト値を設定

    def __post_init__(self):
        if self.index < 0:
            raise ValueError("Index must be non-negative")
        if self.weight < 0:
            raise ValueError("Weight must be non-negative")

@dataclass
class WidgetLayout:
    widget: ctk.CTkBaseClass
    row: int
    column: int
    rowspan: int = 1
    columnspan: int = 1
    sticky: str = 'nsew'
    
    def __post_init__(self):
        if self.row < 0:
            raise ValueError("Row must be non-negative")
        if self.column < 0:
            raise ValueError("Column must be non-negative")
        if self.rowspan < 0:
            raise ValueError("Rowspan must be non-negative")
        if self.columnspan < 0:
            raise ValueError("Columnspan must be non-negative")
        if self.sticky not in ['n', 's', 'e', 'w', 'ns', 'ew', 'ne', 'nw', 'se', 'sw', 'nsew']:
            raise ValueError("Sticky must be one of ['n', 's', 'e', 'w', 'ns', 'ew', 'ne', 'nw', 'se', 'sw', 'nsew']")

    def grid(self):
        self.widget.grid(row=self.row, column=self.column, rowspan=self.rowspan, columnspan=self.columnspan, sticky=self.sticky)
        
class GridManager:
    def __init__(self, master: ctk.CTkBaseClass, 
                 column_configs: List[GridConfig] = [], 
                 row_configs: List[GridConfig] = [],
                 widget_layouts: List[WidgetLayout] = None):
        
        self.master = master
        self.column_configs = column_configs
        self.row_configs = row_configs
        
        if widget_layouts is None:
            raise ValueError("widget_layouts must be a list of WidgetLayout objects")
        self.widget_layouts = widget_layouts 
        
        self.configure_grid()
        self.layout_widgets() 
    
    def configure_grid(self):
        for config in self.column_configs:
            self.master.columnconfigure(config.index, weight=config.weight)
        for config in self.row_configs:
            self.master.rowconfigure(config.index, weight=config.weight)
    
    def layout_widgets(self):
        for layout in self.widget_layouts:
            layout.grid()