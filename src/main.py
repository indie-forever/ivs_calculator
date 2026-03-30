import flet as ft
from gui import CalculatorUI

def main(page: ft.Page):
    page.title = "IVS Kalkulačka"
    page.window_width = 320
    page.window_height = 500
    
    calc = CalculatorUI()
    page.add(calc.get_view())

ft.app(target=main)