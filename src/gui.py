import flet as ft

class CalculatorUI:
    def __init__(self, page=None):
        self.page = page
        self.display = ft.Text(value="0", size=40, color="white")
        self.current_formula = ""
        self.is_result = False 
        self.on_btn_click = None
        self.on_go_to_settings = None

    def on_keyboard(self, e: ft.KeyboardEvent):
        class FakeEvent:
            def __init__(self, data):
                self.control = type('obj', (object,), {'data': data})
        key = e.key
        if key in "0123456789+-*/^().,!":
            self.internal_handle_click(FakeEvent(key.replace(",", ".")))
        elif key == "Enter":
            self.internal_handle_click(FakeEvent("="))
        elif key == "Escape":
            self.internal_handle_click(FakeEvent("C"))
        elif key == "Backspace":
            if not self.is_result and self.current_formula:
                self.current_formula = self.current_formula[:-1]
                self.display.value = self.current_formula if self.current_formula else "0"
                if self.page: self.page.update()

    def build_button(self, text, color="grey800", text_color="white", expand=1, height=70, action=None):
        return ft.Container(
            content=ft.Text(text, size=16, color=text_color, weight="bold"),
            bgcolor=color,
            border_radius=10,
            alignment=ft.Alignment(0, 0), 
            expand=expand,
            height=height,
            on_click=action if action else self.internal_handle_click,
            data=text
        )

    def internal_handle_click(self, e):
        value = e.control.data
        operators = ["+", "-", "*", "/", "^", "root", "log", "!", "(", ")"]

        if self.display.value == "Error":
            self.current_formula = ""
            self.display.value = "0"
            self.is_result = False
            if value in operators:
                if self.page: self.page.update()
                return

        if self.is_result:
            if value.isdigit() or value == "(":
                self.current_formula = ""
            elif value in operators:
                self.current_formula = self.display.value
            self.is_result = False

        if value == "C":
            self.current_formula = ""
            self.display.value = "0"
            self.is_result = False
        
        elif value == "=":
            if self.on_btn_click:
                self.on_btn_click(self.current_formula)
                self.is_result = True
            return

        else:
            strict_operators = ["+", "-", "*", "/", "^", "root", "log", "!"]
            if value in strict_operators:
                if self.current_formula:
                    if self.current_formula.endswith(tuple(strict_operators)):
                        self.current_formula = self.current_formula[:-1]
                elif value not in ["-", "log"]:
                    return
            
            if self.current_formula == "" and (value.isdigit() or value == "(" or value == "log"):
                self.current_formula = str(value)
            else:
                self.current_formula += str(value)
            self.display.value = self.current_formula
        
        if self.page: self.page.update()

    def get_view(self):
        if self.page:
            self.page.on_keyboard_event = self.on_keyboard
        
        return ft.Column(
            expand=True,
            spacing=15,
            controls=[
                ft.Row(controls=[ft.Container(content=self.display, padding=20, bgcolor="grey900", alignment=ft.Alignment(1, 0), border_radius=10, height=120, expand=True)]),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Column(
                            expand=3,
                            spacing=10,
                            controls=[
                                ft.Row(spacing=10, controls=[self.build_button("7"), self.build_button("8"), self.build_button("9")]),
                                ft.Row(spacing=10, controls=[self.build_button("4"), self.build_button("5"), self.build_button("6")]),
                                ft.Row(spacing=10, controls=[self.build_button("1"), self.build_button("2"), self.build_button("3")]),
                                ft.Row(spacing=10, controls=[self.build_button("0"), self.build_button("=", color="orange"), self.build_button("C", color="red")]),
                            ]
                        ),
                        ft.Column(
                            expand=3,
                            spacing=10,
                            controls=[
                                ft.Row(spacing=10, controls=[self.build_button("/", color="grey700"), self.build_button("root", color="grey700"), self.build_button("(", color="grey700")]),
                                ft.Row(spacing=10, controls=[self.build_button("*", color="grey700"), self.build_button("^", color="grey700"), self.build_button(")", color="grey700")]),
                                ft.Row(spacing=10, controls=[self.build_button("-", color="grey700"), self.build_button("log", color="grey700"), self.build_button(".", color="grey700")]),
                                ft.Row(spacing=10, controls=[self.build_button("+", color="grey700"), self.build_button("!", color="grey700"), self.build_button("Verze 2.0", color="blue_grey_700", action=lambda _: self.on_go_to_settings())]),
                            ]
                        )
                    ]
                ),
            ]
        )

    def get_settings_view(self, on_back):
        if self.page:
            self.page.on_keyboard_event = None
        return ft.Column(
            expand=True, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER, 
            alignment=ft.MainAxisAlignment.CENTER, 
            controls=[
                ft.Text("Projekt IVS", size=30, weight="bold", color="white"), 
                ft.Text("verze 2.0", size=16, color="grey"), 
                ft.Divider(height=20, color="transparent"), 
                ft.ElevatedButton("Zpět ke kalkulačce", on_click=lambda _: on_back())
            ]
        )