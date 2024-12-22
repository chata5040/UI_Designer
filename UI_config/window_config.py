import customtkinter as ctk

class WindowConfig:
    def __init__(self, window: ctk.CTk, 
                 title: str = 'Title', 
                 width: int = 600, 
                 height: int = 400, 
                 resizable: bool = True, 
                 appearance_mode: str = "dark", 
                 color_theme: str = "blue"):
        """
        WindowConfig クラスは、ウィンドウの設定を管理します。
        """
        self._window = window
        self._title = title
        self._width = width
        self._height = height
        self._resizable = resizable
        self._appearance_mode = appearance_mode
        self._color_theme = color_theme
        self.apply_to_window()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value
        self._window.title(value)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self._window.geometry(f'{self._width}x{self._height}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self._window.geometry(f'{self._width}x{self._height}')

    @property
    def resizable(self):
        return self._resizable

    @resizable.setter
    def resizable(self, value: bool):
        self._resizable = value
        self._window.resizable(value, value)

    @property
    def appearance_mode(self):
        return self._appearance_mode

    @appearance_mode.setter
    def appearance_mode(self, value: str):
        self._appearance_mode = value
        ctk.set_appearance_mode(value)

    @property
    def color_theme(self):
        return self._color_theme

    @color_theme.setter
    def color_theme(self, value: str):
        self._color_theme = value
        ctk.set_default_color_theme(value)

    def apply_to_window(self):
        self.title = self._title
        self.width = self._width
        self.height = self._height
        self.resizable = self._resizable
        self.appearance_mode = self._appearance_mode
        self.color_theme = self._color_theme
