import flet as ft

class CalculatorUI:
    def __init__(self):
        self.bg_color = "black"
        self.display_color = "white"
        
        # Textové pole pro výsledek
        self.display = ft.Text(value="0", size=40, color="white")

    def build_button(self, text, color="orange", text_color="white"):
        # Tady jsem změnil defaultní color na "orange"
        return ft.Container(
            content=ft.Text(text, size=20, color=text_color, weight="bold"),
            bgcolor=color,
            border_radius=10,
            alignment=ft.Alignment(0, 0), 
            expand=1,
            height=70,
            on_click=self.on_btn_click,
            data=text
        )

    def on_btn_click(self, e):
        print(f"Stisknuto: {e.control.data}")

    def get_view(self):
        return ft.Column(
            controls=[
                ft.Container(
                    content=self.display, 
                    padding=20, 
                    alignment=ft.Alignment(1, 0) 
                ),
                # Teď jsou všechna tlačítka oranžová automaticky
                ft.Row(controls=[
                    self.build_button("7"), self.build_button("8"), 
                    self.build_button("9"), self.build_button("/")
                ]),
                ft.Row(controls=[
                    self.build_button("4"), self.build_button("5"), 
                    self.build_button("6"), self.build_button("*")
                ]),
                ft.Row(controls=[
                    self.build_button("1"), self.build_button("2"), 
                    self.build_button("3"), self.build_button("-")
                ]),
                ft.Row(controls=[
                    # U "C" můžeme barvu přebít na červenou, pokud chceš
                    self.build_button("C", color="red"), 
                    self.build_button("0"), 
                    self.build_button("="), 
                    self.build_button("+")
                ]),
            ],
            width=350
        )