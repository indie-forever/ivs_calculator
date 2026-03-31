import flet as ft

class CalculatorUI:
    def __init__(self):
        self.bg_color = "black"
        self.display_color = "white"
        self.display = ft.Text(value="0", size=40, color="white")
        self.on_btn_click = None

    def build_button(self, text, color="orange", text_color="white"):
        return ft.Container(
            content=ft.Text(text, size=20, color=text_color, weight="bold"),
            bgcolor=color,
            border_radius=10,
            alignment=ft.Alignment(0, 0), 
            expand=1,
            height=90,
            on_click=lambda e: self.on_btn_click(e) if self.on_btn_click else None,
            data=text
        )

    def get_view(self):
        return ft.Column(
            expand=True,
            spacing=10,
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(
                            content=self.display, 
                            padding=20, 
                            bgcolor="grey900",
                            alignment=ft.Alignment(1, 0),
                            border_radius=10,
                            height=150,
                            expand=True
                        )
                    ]
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        self.build_button("7"), self.build_button("8"), 
                        self.build_button("9"), self.build_button("/"),
                        self.build_button("^")
                    ]
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        self.build_button("4"), self.build_button("5"), 
                        self.build_button("6"), self.build_button("*"),
                        self.build_button("√")
                    ]
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        self.build_button("1"), self.build_button("2"), 
                        self.build_button("3"), self.build_button("-"),
                        self.build_button("(")
                    ]
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        self.build_button("C", color="red"), 
                        self.build_button("0"), self.build_button("="), 
                        self.build_button("+"), self.build_button(")")
                    ]
                ),
            ]
        )