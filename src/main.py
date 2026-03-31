import flet as ft
from gui import CalculatorUI  


def main(page: ft.Page):
    page.title = "Moje Kalkulačka"

    page.theme_mode = ft.ThemeMode.DARK 

    page.padding = 5
    
    page.window_width = 390   # Ubrali jsme cca 70 pixelů
    page.window_height = 450  # Ubrali jsme cca 30 pixelů
    
    page.window_resizable = False
    
    ui = CalculatorUI()
    
    def handle_click(e):
        napsano_na_tlacitku = e.control.data 
        
        if ui.display.value == "0":
            ui.display.value = napsano_na_tlacitku
        else:
            ui.display.value += napsano_na_tlacitku
        
        page.update()

    ui.on_btn_click = handle_click 

    page.add(ui.get_view())

ft.app(target=main)