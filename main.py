import customtkinter as ctk
from UI_config.window_config import WindowConfig
from UI_config.grid_layout import GridConfig, WidgetLayout, GridManager
from main_window_widgets.menu_bar import MenuBar
from main_window_widgets.widget_adder_frame import WidgetAdderFrame

class UIDesigner(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.create_widgets()
        self.layout_widgets()

    def configure_window(self):
        self.window_config = WindowConfig(
            window=self,
            title='UI Designer',
            width=1500,
            height=800,
            resizable=False,
            appearance_mode="dark",
            color_theme="blue"
        )

    def create_widgets(self):
        self._menu = MenuBar(master=self)
        self._widget_adder_frame = WidgetAdderFrame(master=self, select_button_command=self.add_widget)

    def layout_widgets(self):
        self.window_grid_manager = GridManager(
            master=self,
            column_configs=[GridConfig(index=0, weight=0), GridConfig(index=1, weight=1)],
            row_configs=[GridConfig(index=0, weight=0), GridConfig(index=1, weight=1)],
            widget_layouts=[
                WidgetLayout(widget=self._menu.menu_bar, row=0, column=0, columnspan=2, sticky='nsew'),
                WidgetLayout(widget=self._widget_adder_frame, row=1, column=0, sticky='nsew')
            ]
        )

    def add_widget(self, widget_class):
        # ここにウィジェットを追加するロジックを実装します
        print(f"Adding widget: {widget_class}")

if __name__ == '__main__':
    app = UIDesigner()
    app.mainloop()