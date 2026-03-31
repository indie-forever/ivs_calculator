import flet as ft
from gui import CalculatorUI  
from logic import CalculatorController


def main(page: ft.Page):

    ctrl = CalculatorController()
    page.title = "Moje Kalkulačka"

    page.theme_mode = ft.ThemeMode.DARK 

    page.padding = 5
    
    page.window_width = 390   # Ubrali jsme cca 70 pixelů
    page.window_height = 450  # Ubrali jsme cca 30 pixelů
    
    page.window_resizable = False
    
    ui = CalculatorUI()
    
    def handle_click(e):
        ctrl.handle_button(e.control.data) 
        ui.display.value = ctrl.get_display_text()   
        page.update()

    ui.on_btn_click = handle_click 
    page.add(ui.get_view())

if __name__ == "__main__":
    ft.app(target=main)