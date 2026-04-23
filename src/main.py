import flet as ft
from gui import CalculatorUI
from logic import CalculatorController

def main(page: ft.Page):
    # Inicializace logiky a UI
    ctrl = CalculatorController()
    ui = CalculatorUI(page)
    
    # Nastavení okna
    page.title = "IVS Kalkulačka"
    page.theme_mode = ft.ThemeMode.DARK 
    page.padding = 10
    page.window_width = 400
    page.window_height = 750
    page.window_resizable = False

    def handle_click(formula):
        ctrl.expression = formula 
        ctrl.handle_button("=") # Vyvoláme výpočet
        ui.display.value = ctrl.get_display_text()
        ui.current_formula = ui.display.value 
        page.update()

    def show_calc():
        page.clean()
        ui.display.value = ctrl.get_display_text()
        page.add(ui.get_view())

    def show_settings():
        page.clean()
        page.add(ui.get_settings_view(on_back=show_calc))

    ui.on_btn_click = handle_click 
    ui.on_go_to_settings = show_settings

    show_calc()

if __name__ == "__main__":
    ft.app(target=main)