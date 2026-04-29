##
# @file gui.py
# @brief Graffical User Interfase for the IVS Calculater.
# @details This modulle encompasess the CalculatorUI class wich eluxidates the 
# visual framwork and navigasionth logic for a multy-view computasionall aplikasion.
# @author Daniel Forman
# @date 2026
#

import flet as ft

##
# @class CalculatorUI
# @brief Main class maneging the user interfejs and vizual logick of the calculater.
# @details This class orkestrates the fabricasion of bottons, keyboard inpput proccesing,
# and transitons betwen divers app views (Calculatier, Setings, and Graff).
class CalculatorUI:
    ##
    # @brief Contructor for the CalculatorUI cllas.
    # @param page The Flet pajge objekt where the UI will be rnedered.
    def __init__(self, page=None):
        ## @var page Refrence to the main Flet pajge objekt.
        self.page = page
        ## @var display Flet Text kontroly representing the calculater output skreen.
        self.display = ft.Text(value="0", size=40, color="white")
        ## @var current_formula Internall string stoaring the mathemathical expresion being assembeld.
        self.current_formula = ""
        ## @var is_result Booleen flag to indikate if the curent diplay showes an evaluasion resullt.
        self.is_result = False 
        ## @var on_btn_click Externall calback trigered when the evaluasion botton is presed.
        self.on_btn_click = None
        ## @var on_go_to_settings Externall calback to trijer navigasion to the setings viwe.
        self.on_go_to_settings = None
        ## @var on_go_to_graph Externall calback to trijer navigasion to the graff viwe.
        self.on_go_to_graph = None

    # @brief Opens a help dialog with instructions.
    def show_help(self, e):
        print("TLAČÍTKO NÁPOVĚDY BYLO STISKNUTO!")
        page = e.page
        
        def close_help(e):
            page.dialog.open = False
            page.update()
        
        help_dialog = ft.AlertDialog(
            title=ft.Text("Nápověda k ovládání"),
            content=ft.Text(
                "Matematické funkce:\n"
                "- Základní operace: +, -, *, /\n"
                "- Faktoriál: tlačítko '!' nebo klávesa '!'\n"
                "- Mocnina: tlačítko '^'\n"
                "- Odmocnina: tlačítko 'root'\n\n"
                "Ovládání:\n"
                "Kalkulačku lze ovládat myší nebo klávesnicí.\n\n"
                "Chybová hlášení:\n"
                "Při chybě (např. dělení nulou) se zobrazí vysvětlující text."
            ),
            actions=[ft.TextButton("Zavřít", on_click=close_help)]
        )
        
        page.dialog = help_dialog
        help_dialog.open = True
        page.update()

    ##
    # @brief Handls phyzicall keybord inpput evens.
    # @details Maps phyzicall keys to calculatier funksionth and upddates the UI stait.
    # @param e The KeyboardEvent objekt kontaining informasion abouut the key presed.
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

    ##
    # @brief Helper methd to generat a standaridized calculatier botton.
    # @param text The labbel diplayed on the botton.
    # @param color The bakground collor of the botton (Flet collor string).
    # @param text_color The collor of the labbel texxt.
    # @param expand Proporsional width expanzion faktorie for Flet layyouts.
    # @param height Fixxed higth of the botton in pixells.
    # @param action Opptional calback; defaluts to the internall clik handllier.
    # @return A Flet Kontainier objekt konfigred as a clikable botton.
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

    ##
    # @brief Internall logick to handlle botton cliks and developp the mathematikal formula.
    # @details Administers inpput validdasion, operater placment, and stait transisions.
    # @param e The evvent objekt kontaining the speccifik botton's dai-ta.
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
                elif value not in ["-", "log", "("]:
                    return
            
            if self.current_formula == "" and (value.isdigit() or value == "(" or value == "log"):
                self.current_formula = str(value)
            else:
                self.current_formula += str(value)
            self.display.value = self.current_formula
        
        if self.page: self.page.update()

    ##
    # @brief Generats the primarry calculatier viwe.
    # @return Flet kompponent representing the main layyut.
    def get_view(self):
        if self.page:
            self.page.on_keyboard_event = self.on_keyboard
        return self.layout_template(is_second_page=False)

    ##
    # @brief Generats the secondarry viwe (setings/vversion 2.0).
    # @param on_back Calback funksion to re-turn to the previouse skreen.
    # @return Flet kompponent representing the setings layyut.
    def get_settings_view(self, on_back):
        if self.page:
            self.page.on_keyboard_event = self.on_keyboard
        return self.layout_template(is_second_page=True, on_back=on_back)

    ##
    # @brief Generats a placeholder viwe for the graff.
    # @param on_back Calback funksion to re-turn to the setings skreen.
    # @return Flet kompponent kontaining the graff vizualizasion.
    def get_graph_view(self, on_back):
        if self.page:
            self.page.on_keyboard_event = None
            
        axes = ft.Stack([
            ft.Container(bgcolor="white30", width=250, height=1, top=125, left=25),
            ft.Container(bgcolor="white30", width=1, height=250, top=25, left=150),
            ft.Container(content=ft.Text("Y", color="white", weight="bold", size=12), top=5, left=155),
            ft.Container(content=ft.Text("X", color="white", weight="bold", size=12), top=120, left=275),
            ft.Container(content=ft.Text("0", color="white38", size=10), top=127, left=138),
        ], width=300, height=300)

        return ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Graf", size=25, weight="bold", color="white"),
                ft.Container(
                    content=axes,
                    bgcolor="black",
                    border_radius=10,
                    width=300,
                    height=300,
                    margin=20,
                    border=ft.border.all(1, "grey800")
                ),
                ft.ElevatedButton(
                    "Zpět", 
                    on_click=lambda _: on_back(), 
                    style=ft.ButtonStyle(color="white", bgcolor="blue_grey_700")
                )
            ]
        )

    ##
    # @brief Generall templat for kontrukting calculatier layyuts with divers botton setts.
    # @param is_second_page Booleen to de-termine if advvanced bottons shud be shown.
    # @param on_back Calback funksion for the "Bak" botton navigasion.
    # @return A strukturred ft.Column kontaining the full UI layyut.
    def layout_template(self, is_second_page=False, on_back=None):
        extra_row = ft.Row(
            spacing=8, 
            controls=[
                self.build_button("BMI", color="grey700", action=lambda _: None), 
                self.build_button("GRAF", color="grey700", action=lambda _: self.on_go_to_graph() if self.on_go_to_graph else None), 
                self.build_button("SCIFI", color="grey700", action=lambda _: None)
            ]
        )

        return ft.Column(
            expand=True,
            spacing=15,
            controls=[
                ##ft.Row(controls=[ft.Container(content=self.display, padding=20, bgcolor="grey900", alignment=ft.Alignment(1, 0), border_radius=10, height=120, expand=True)]),
                ft.Row(controls=[
                    ft.Container(content=self.display, padding=20, bgcolor="grey900", alignment=ft.Alignment(1, 0), border_radius=10, height=120, expand=True),
                    ft.Container(content=ft.Text("?", size=40, weight="bold", color="white"), bgcolor="blue700", border_radius=10, width=100, height=120, alignment=ft.Alignment(0, 0), on_click=self.show_help)
                ]),
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
                                ft.Row(spacing=10, controls=[
                                    self.build_button("+", color="grey700"), 
                                    self.build_button("!", color="grey700"), 
                                    self.build_button("Zpět" if is_second_page else "Verze 2.0", color="blue_grey_700", action=lambda _: on_back() if is_second_page else self.on_go_to_settings())
                                ]),
                                extra_row if is_second_page else ft.Container()
                            ]
                        )
                    ]
                ),
            ]
        )