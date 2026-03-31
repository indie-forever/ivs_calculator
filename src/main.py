import flet as ft
from gui import CalculatorUI  
from logic import CalculatorController

def main(page: ft.Page):
    page.title = "IVS Calculator"

    ctrl = CalculatorController()
    
    ui = CalculatorUI()
    
    def handle_click(e):
        ctrl.handle_button(e.control.data) 
        ui.display.value = ctrl.get_display_text()   
        page.update()

    ui.on_btn_click = handle_click 
    page.add(ui.get_view())

if __name__ == "__main__":
    ft.app(target=main)