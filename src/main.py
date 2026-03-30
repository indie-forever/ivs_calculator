import flet as ft
from gui import CalculatorUI  

def main(page: ft.Page):
    page.title = "Moje Kalkulačka"
    
    # 1. Vytvoříme instanci tvého UI
    ui = CalculatorUI()
    
    # 2. SEM VLOŽÍME TU FUNKCI (jako vnitřní funkci)
    def handle_click(e):
        napsano_na_tlacitku = e.control.data 
        
        if ui.display.value == "0":
            ui.display.value = napsano_na_tlacitku
        else:
            ui.display.value += napsano_na_tlacitku
        
        page.update()

    # 3. PROPOJENÍ: Musíme říct tvým tlačítkům, aby tuto funkci volala.
    # V gui.py jsme si připravili on_btn_click, tak mu ji teď předáme.
    ui.on_btn_click = handle_click 

    # 4. Přidáme celé UI na stránku
    page.add(ui.get_view())

ft.app(target=main)