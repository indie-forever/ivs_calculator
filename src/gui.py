import flet as ft

class CalculatorUI:
    def __init__(self):
        self.bg_color = "black"
        self.display_color = "white"
        self.display = ft.Text(value="0", size=40, color="white")
        self.on_btn_click = None
        self.on_go_to_settings = None

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
                ft.Row(spacing=10, controls=[self.build_button("7"), self.build_button("8"), self.build_button("9"), self.build_button("/"), self.build_button("^")]),
                ft.Row(spacing=10, controls=[self.build_button("4"), self.build_button("5"), self.build_button("6"), self.build_button("*"), self.build_button("√")]),
                ft.Row(spacing=10, controls=[self.build_button("1"), self.build_button("2"), self.build_button("3"), self.build_button("-"), self.build_button("(")]),
                ft.Row(spacing=10, controls=[self.build_button("C", color="red"), self.build_button("0"), self.build_button("="), self.build_button("+"), self.build_button(")")]),
                
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            "Nastavení / Info", 
                            on_click=lambda _: self.on_go_to_settings() if self.on_go_to_settings else None,
                            expand=True,
                            style=ft.ButtonStyle(color="white", bgcolor="blue_grey_700")
                        )
                    ]
                )
            ]
        )

    def get_settings_view(self, on_back):
        return ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Text("Nová Stránka", size=30, weight="bold"),
                ft.Text("Zde může být info o projektu IVS", size=16),
                ft.ElevatedButton("Zpět ke kalkulačce", on_click=lambda _: on_back())
            ]
        )
