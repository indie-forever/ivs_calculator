import flet as ft
from gui import CalculatorUI  
from logic import CalculatorController

def main(page: ft.Page):
    ctrl = CalculatorController()
    ui = CalculatorUI()
    
    page.title = "Moje Kalkulačka"
    page.theme_mode = ft.ThemeMode.DARK 
    page.padding = 10
    
    page.window_width = 400
    page.window_height = 750
    page.window_resizable = False

    def handle_click(e):
        ctrl.handle_button(e.control.data) 
        ui.display.value = ctrl.get_display_text()   
        page.update()

    def show_calc():
        page.clean()
        page.add(ui.get_view())

    def show_settings():
        page.clean()
        page.add(ui.get_settings_view(on_back=show_calc))

    ui.on_btn_click = handle_click 
    ui.on_go_to_settings = show_settings

    show_calc()

if __name__ == "__main__":
    ft.app(target=main)
