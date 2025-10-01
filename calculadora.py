import tkinter as tk
from tkinter import ttk, messagebox
import math

# === Funciones de Operaciones Básicas ===

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero."
    return a / b

# === Funciones de Operaciones Avanzadas ===

def potencia(base, exponente):
    return base ** exponente

def porcentaje(numero, percent):
    return (numero * percent) / 100

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: Raíz de número negativo."
    return math.sqrt(numero)

def convertir_temp(valor, unidad_origen, unidad_destino):
    u_o = unidad_origen.upper()
    u_d = unidad_destino.upper()

    if u_o == 'C' and u_d == 'F':
        return (valor * 9/5) + 32
    elif u_o == 'F' and u_d == 'C':
        return (valor - 32) * 5/9
    else:
        return "Error: Unidades no válidas o iguales (solo C/F)."

# === CLASE PRINCIPAL DE LA APLICACIÓN (GUI) ===

class CalculadoraApp:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Inteligente")
        master.geometry("400x550") 
        master.resizable(False, False) 

        self.current_expression = tk.StringVar()
        self.current_expression.set("0")

        display_frame = tk.Frame(master, bd=4, relief="ridge", bg="lightgray")
        display_frame.pack(fill="x", padx=10, pady=10)

        self.display_label = tk.Label(
            display_frame,
            textvariable=self.current_expression,
            font=("Arial", 24, "bold"),
            anchor="e",
            bg="lightgray",
            fg="black",
            padx=10,
            pady=10
        )
        self.display_label.pack(expand=True, fill="both")

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(pady=5, padx=10, expand=True, fill="both")

        self.tab_basicas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_basicas, text='Básicas')
        self.crear_interfaz_basicas(self.tab_basicas)

        self.tab_avanzadas = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_avanzadas, text='Avanzadas')
        self.crear_interfaz_avanzadas(self.tab_avanzadas)
        
        self.operator = ""
        self.first_num = None
        self.waiting_for_second_num = False

    def click_button(self, value):
        current_text = self.current_expression.get()

        if value == "C":
            self.current_expression.set("0")
            self.first_num = None
            self.operator = ""
            self.waiting_for_second_num = False
            return
        
        if self.waiting_for_second_num and value.replace('.', '', 1).isdigit():
            self.current_expression.set(value)
            self.waiting_for_second_num = False
        elif current_text == "0" and value != ".":
            self.current_expression.set(value)
        else:
            if value == "." and "." in current_text:
                return
            self.current_expression.set(current_text + str(value))

    def set_operator(self, op):
        if self.first_num is None:
            try:
                self.first_num = float(self.current_expression.get())
            except ValueError:
                messagebox.showerror("Error", "Entrada inválida. Limpie y reintente.")
                self.current_expression.set("0")
                return
        else:
            if not self.waiting_for_second_num:
                self.calculate_basic()
                self.first_num = float(self.current_expression.get())
            
        self.operator = op
        self.waiting_for_second_num = True

    def calculate_basic(self):
        if self.first_num is None or self.operator == "":
            return

        try:
            second_num = float(self.current_expression.get())
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida para el segundo número.")
            self.current_expression.set("0")
            self.first_num = None
            self.operator = ""
            self.waiting_for_second_num = False
            return

        result = "Error"
        if self.operator == "+":
            result = suma(self.first_num, second_num)
        elif self.operator == "-":
            result = resta(self.first_num, second_num)
        elif self.operator == "*":
            result = multiplicacion(self.first_num, second_num)
        elif self.operator == "/":
            result = division(self.first_num, second_num)
        
        if isinstance(result, str):
            self.current_expression.set(result)
        else:
            self.current_expression.set(str(result))
        
        self.first_num = None
        self.operator = ""
        self.waiting_for_second_num = False

    def crear_interfaz_basicas(self, parent_frame):
        buttons_frame = tk.Frame(parent_frame)
        buttons_frame.pack(pady=10)

        button_config = {
            'font': ('Arial', 18), 'width': 5, 'height': 2, 'bg': '#f0f0f0', 'activebackground': '#e0e0e0'
        }
        operator_config = {
            'font': ('Arial', 18, 'bold'), 'width': 5, 'height': 2, 'bg': '#e6e6e6', 'activebackground': '#d9d9d9'
        }
        
        buttons_list = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '.', '='
        ]
        
        row_val = 0
        col_val = 0
        
        for button_text in buttons_list:
            
            if button_text.isdigit() or button_text == '.':
                command = lambda val=button_text: self.click_button(val)
                style = button_config
            elif button_text == '=':
                command = self.calculate_basic
                style = {'font': ('Arial', 18, 'bold'), 'width': 5, 'height': 2, 'bg': '#a0e0a0', 'activebackground': '#90d090'}
            elif button_text == 'C':
                command = lambda: self.click_button("C")
                style = {'font': ('Arial', 18, 'bold'), 'width': 5, 'height': 2, 'bg': '#ff9999', 'activebackground': '#ff8080'}
            else:
                command = lambda op=button_text: self.set_operator(op)
                style = operator_config
            
            btn = tk.Button(buttons_frame, text=button_text, **style, command=command)
            
            if button_text == '0':
                 btn.grid(row=3, column=1, padx=5, pady=5)
            elif button_text == 'C':
                btn.grid(row=3, column=0, padx=5, pady=5)
            elif button_text == '.':
                btn.grid(row=3, column=2, padx=5, pady=5)
            elif button_text == '=':
                btn.grid(row=3, column=3, padx=5, pady=5)
            else:
                btn.grid(row=row_val, column=col_val % 4, padx=5, pady=5)
            
            col_val += 1
            if col_val % 4 == 0:
                row_val += 1
                col_val = 0

    def crear_interfaz_avanzadas(self, parent_frame):
        input_frame = tk.Frame(parent_frame, padx=5, pady=5)
        input_frame.pack(fill="x", expand=True)

        label_font = ('Arial', 11)
        entry_font = ('Arial', 11)
        button_font = ('Arial', 9)

        # 1. Potencia (Base ^ Exp)
        row_count = 0
        tk.Label(input_frame, text="Potencia:", font=label_font).grid(row=row_count, column=0, sticky="w", pady=5)
        
        self.power_base_entry = tk.Entry(input_frame, width=6, font=entry_font)
        self.power_base_entry.grid(row=row_count, column=1, padx=1, pady=5)
        
        tk.Label(input_frame, text="^", font=label_font).grid(row=row_count, column=2, padx=1, pady=5)
        
        self.power_exp_entry = tk.Entry(input_frame, width=6, font=entry_font)
        self.power_exp_entry.grid(row=row_count, column=3, padx=1, pady=5)
        
        tk.Button(input_frame, text="Calc.", command=self.calcular_potencia, font=button_font, width=5).grid(row=row_count, column=4, padx=5, pady=5)
        
        # 2. Porcentaje (Num % de Cantidad)
        row_count += 1
        tk.Label(input_frame, text="Porcentaje:", font=label_font).grid(row=row_count, column=0, sticky="w", pady=5)
        
        self.percent_num_entry = tk.Entry(input_frame, width=6, font=entry_font)
        self.percent_num_entry.grid(row=row_count, column=1, padx=1, pady=5)
        
        tk.Label(input_frame, text="%", font=label_font).grid(row=row_count, column=2, padx=1, pady=5)
        
        self.percent_total_entry = tk.Entry(input_frame, width=6, font=entry_font)
        self.percent_total_entry.grid(row=row_count, column=3, padx=1, pady=5)
        
        tk.Button(input_frame, text="Calc.", command=self.calcular_porcentaje, font=button_font, width=5).grid(row=row_count, column=4, padx=5, pady=5)
        
        # 3. Raíz Cuadrada (√Num)
        row_count += 1
        tk.Label(input_frame, text="Raíz Cuadrada:", font=label_font).grid(row=row_count, column=0, sticky="w", pady=5)
        
        self.sqrt_num_entry = tk.Entry(input_frame, width=20, font=entry_font)
        self.sqrt_num_entry.grid(row=row_count, column=1, padx=5, pady=5, columnspan=3, sticky="ew") 
        
        tk.Button(input_frame, text="Calc.", command=self.calcular_raiz_cuadrada, font=button_font, width=5).grid(row=row_count, column=4, padx=5, pady=5)
        
        # 4. Conversión de Temperatura (Valor C/F a F/C)
        row_count += 1
        tk.Label(input_frame, text="Conversión Temp:", font=label_font).grid(row=row_count, column=0, sticky="w", pady=5)
        
        self.temp_val_entry = tk.Entry(input_frame, width=6, font=entry_font)
        self.temp_val_entry.grid(row=row_count, column=1, padx=1, pady=5)
        
        self.temp_from_unit = ttk.Combobox(input_frame, values=["C", "F"], width=2, font=('Arial', 10))
        self.temp_from_unit.set("C")
        self.temp_from_unit.grid(row=row_count, column=2, sticky="w")
        
        tk.Label(input_frame, text="a", font=label_font).grid(row=row_count, column=3, sticky="w")
        
        self.temp_to_unit = ttk.Combobox(input_frame, values=["C", "F"], width=2, font=('Arial', 10))
        self.temp_to_unit.set("F")
        self.temp_to_unit.grid(row=row_count, column=3, sticky="w")
        
        tk.Button(input_frame, text="Conv.", command=self.calcular_conversion_temp, font=button_font, width=5).grid(row=row_count, column=4, padx=5, pady=5)

    def calcular_potencia(self):
        try:
            base = float(self.power_base_entry.get())
            exp = float(self.power_exp_entry.get())
            result = potencia(base, exp)
            self.current_expression.set(str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida para potencia. Ingrese números.")
            self.current_expression.set("Error")

    def calcular_porcentaje(self):
        try:
            num = float(self.percent_num_entry.get())
            total = float(self.percent_total_entry.get())
            result = porcentaje(num, total)
            self.current_expression.set(str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida para porcentaje. Ingrese números.")
            self.current_expression.set("Error")

    def calcular_raiz_cuadrada(self):
        try:
            num = float(self.sqrt_num_entry.get())
            result = raiz_cuadrada(num)
            self.current_expression.set(str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida para raíz cuadrada. Ingrese un número.")
            self.current_expression.set("Error")

    def calcular_conversion_temp(self):
        try:
            value = float(self.temp_val_entry.get())
            from_unit = self.temp_from_unit.get()
            to_unit = self.temp_to_unit.get()
            result = convertir_temp(value, from_unit, to_unit)
            self.current_expression.set(str(result))
        except ValueError:
            messagebox.showerror("Error", "Entrada inválida para conversión. Ingrese un número.")
            self.current_expression.set("Error")

# === PUNTO DE INICIO DE LA APLICACIÓN ===

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()