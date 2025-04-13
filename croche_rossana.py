import tkinter as tk
from tkinter import ttk
import math

def estimar_peso_fio(diametro_cm, diametro_referencia=36, peso_referencia_g=150):
    raio = diametro_cm / 2
    raio_ref = diametro_referencia / 2

    area = math.pi * raio ** 2
    area_ref = math.pi * raio_ref ** 2

    peso_estimado = (area / area_ref) * peso_referencia_g
    return round(peso_estimado, 2)

def calcular():
    try:
        diametro = float(entrada_diametro.get())
        peso = estimar_peso_fio(diametro)
        resultado_var.set(f"Peso estimado do fio: {peso} g")
    except ValueError:
        resultado_var.set("Por favor, insira um número válido.")

# Interface Gráfica
app = tk.Tk()
app.title("Calculadora de Fio para Sousplat")

frame = ttk.Frame(app, padding=20)
frame.grid()

# Entrada
ttk.Label(frame, text="Diâmetro do sousplat (cm):").grid(column=0, row=0, sticky="w")
entrada_diametro = ttk.Entry(frame, width=10)
entrada_diametro.grid(column=1, row=0)

# Botão
botao_calcular = ttk.Button(frame, text="Calcular", command=calcular)
botao_calcular.grid(column=0, row=1, columnspan=2, pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_label = ttk.Label(frame, textvariable=resultado_var, font=("Helvetica", 12, "bold"))
resultado_label.grid(column=0, row=2, columnspan=2, pady=10)

# Iniciar app
app.mainloop()