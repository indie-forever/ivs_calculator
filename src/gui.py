##
# @file gui.py
# @brief Graphical User Interface for the IVS Calculator.
# @details This module contains the CalculatorUI class, which defines the 
# visual structure and interaction logic for a multi-view mathematical application.
# @author Daniel Forman
# @date 2026
#

import flet as ft

##
# @class CalculatorUI
# @brief Main class managing the user interface and visual logic.
# @details Orchestrates button construction, keyboard input processing, 
# and view transitions (Calculator, Settings, and Graph).
class CalculatorUI:
    ##
    # @brief Constructor for the CalculatorUI class.
    # @param page Reference to the Flet Page object for UI rendering.
    def __init__(self, page=None):
        ## @var page Reference to the primary Flet page object.
        self.page = page
        ## @var display Flet Text control representing the calculator's display screen.
        self.display = ft.Text(value="0", size=40, color="white")
        ## @var current_formula Internal string storing the mathematical expression being built.
        self.current_formula = ""
        ## @var is_result Boolean flag indicating if the displayed value is a result of a calculation.
        self.is_result = False 
        ## @var on_btn_click External callback triggered when the equals button is pressed.
        self.on_btn_click = None
        ## @var on_go_to_settings External callback for navigating to the settings/advanced view.
        self.on_go_to_settings = None
        ## @var on_go_to_graph External callback for navigating to the graph visualization.
        self.on_go_to_graph = None

    ##
    # @brief Displays a help dialog with control instructions.
    # @details Triggers a modal AlertDialog showing available functions and control tips.
    # @param e The event object from the help button click.
    def show_help(self, e):
        # Ensure we have the correct page reference for the overlay
        page = self.page if self.page else e.page
        
        def close_help(e):
            help_dialog.open = False
            page.update()
        
        ## @brief Popup dialog containing usage tips.
        help_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Nápověda k ovládání"),
            content=ft.Text(
                "Matematické funkce:\n"
                "- Základní operace: +, -, *, /\n"
                "- Faktoriál: tlačítko '!' nebo klávesa '!'\n"
                "- Mocnina: tlačítko '^'\n"
                "- Odmocnina: tlačítko 'root'\n\n"
                "Ovládání:\n"
                "Kalkulačku lze ovládat myší nebo klávesnicí.\n\n"
            ),
            actions=[ft.TextButton("Jasně, chápu", on_click=close_help)],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.overlay.append(help_dialog)
        help_dialog.open = True
        page.update()

    ##
    # @brief Processes physical keyboard inputs.
    # @details Maps keys to calculator actions and updates the current formula.
    # @param e The KeyboardEvent object from Flet.
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
                # Logic to delete multi-character operators properly
                if self.current_formula.endswith("root"):
                    self.current_formula = self.current_formula[:-4]
                elif self.current_formula.endswith("log"):
                    self.current_formula = self.current_formula[:-3]
                else:
                    self.current_formula = self.current_formula[:-1]
                
                self.display.value = self.current_formula if self.current_formula else "0"
                if self.page: self.page.update()

    ##
    # @brief Helper method to create a standardized UI button.
    # @param text Label displayed on the button.
    # @param color Background color of the container.
    # @param text_color Color of the label text.
    # @param expand Proportional expansion factor for the layout.
    # @param height Fixed pixel height of the button.
    # @param action Optional specific callback function; defaults to internal_handle_click.
    # @return A Flet Container object configured as a clickable button.
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
    # @brief Processes internal button clicks and builds the mathematical expression.
    # @details Handles operator replacement logic, multi-char deletion, and display updates.
    # @param e The event object containing the button's data.
    def internal_handle_click(self, e):
        value = e.control.data
        operators = ["+", "-", "*", "/", "^", "root", "log", "!", "(", ")"]
        
        # Reset display if error occurred previously
        if self.display.value == "Error":
            self.current_formula = ""
            self.display.value = "0"
            self.is_result = False
            if value in operators:
                if self.page: self.page.update()
                return
        
        # Start new formula if a digit is pressed after a result
        if self.is_result:
            if value.isdigit() or value == "(":
                self.current_formula = ""
            elif value in operators:
                self.current_formula = self.display.value
            self.is_result = False
        
        # Clear logic
        if value == "C":
            self.current_formula = ""
            self.display.value = "0"
            self.is_result = False
        
        # Trigger external calculation
        elif value == "=":
            if self.on_btn_click:
                self.on_btn_click(self.current_formula)
                self.is_result = True
            return
        
        # Expression building logic
        else:
            strict_operators = ["+", "-", "*", "/", "^", "root", "log", "!"]
            if value in strict_operators:
                if self.current_formula:
                    # Logic to replace existing operators and prevent "roolog" errors
                    if self.current_formula.endswith("root"):
                        self.current_formula = self.current_formula[:-4]
                    elif self.current_formula.endswith("log"):
                        self.current_formula = self.current_formula[:-3]
                    elif self.current_formula.endswith(tuple(["+", "-", "*", "/", "^", "!"])):
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
    # @brief Returns the default calculator view.
    # @return A Flet Column representing the main UI view.
    def get_view(self):
        if self.page:
            self.page.on_keyboard_event = self.on_keyboard
        return self.layout_template(is_second_page=False)

    ##
    # @brief Returns the advanced/settings view.
    # @param on_back Callback for the navigation return button.
    # @return A Flet Column representing the settings UI view.
    def get_settings_view(self, on_back):
        if self.page:
            self.page.on_keyboard_event = self.on_keyboard
        return self.layout_template(is_second_page=True, on_back=on_back)

    ##
    # @brief Returns the graph visualization view.
    # @param on_back Callback for the navigation return button.
    # @return A Flet Column containing the graphical coordinate system.
    def get_graph_view(self, on_back):
        if self.page:
            self.page.on_keyboard_event = None
            
        ## @brief Drawing axes for graph visualization.
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
    # @brief Standard layout template used across views.
    # @param is_second_page If True, renders advanced row (BMI, GRAPH, etc).
    # @param on_back Callback for navigation buttons.
    # @return A fully assembled Flet Column layout.
    def layout_template(self, is_second_page=False, on_back=None):
        ## @brief Advanced functionality row.
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
                # Top layout section including display and help button
                ft.Row(controls=[
                    ft.Container(
                        content=self.display, padding=20, bgcolor="grey900", 
                        alignment=ft.Alignment(1, 0), border_radius=10, height=120, expand=True
                    ),
                    ft.Container(
                        content=ft.Text("?", size=40, weight="bold", color="white"), 
                        bgcolor="blue700", border_radius=10, width=100, height=120, 
                        alignment=ft.Alignment(0, 0), 
                        on_click=self.show_help
                    )
                ]),
                # Main keypad layout
                ft.Row(
                    spacing=10,
                    controls=[
                        # Number pad column
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
                        # Operator column
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