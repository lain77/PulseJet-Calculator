import tkinter as tk

# ---------------------------
# JANELA PRINCIPAL
# ---------------------------
janela = tk.Tk()
janela.title("Pulsejet Calculator")
janela.geometry("950x650")
janela.configure(bg="#121212")

# ---------------------------
# CORES E FONTES
# ---------------------------
fundo_cor = "#121212"
texto_cor = "#EAEAEA"
cor_botao = "#3E3E3E"
cor_hover = "#6AA9F7"
cor_entrada = "#1F1F1F"
cor_frame = "#1C1C1C"
cor_resultado = "#7FDBCA"

fonte_titulo = ("Segoe UI", 28, "bold")
fonte_texto = ("Segoe UI", 12)
fonte_botao = ("Segoe UI", 12, "bold")
fonte_resultado = ("Consolas", 12)

# ---------------------------
# FUNÇÃO DE VALIDAÇÃO
# ---------------------------
def apenas_numeros(texto):
    if texto == "":
        return True
    return texto.replace('.', '', 1).isdigit()  # permite ponto decimal

vcmd = (janela.register(apenas_numeros), "%P")

# ---------------------------
# FUNÇÃO DE CÁLCULO
# ---------------------------
def calcular():
    try:
        r = float(entrada.get())  # raio em mm
        EPA = 3.141592 * (r ** 2)  # área do escape mm²
        VFA = EPA * 0.4922  # área de válvulas mm²
        comprimento = 0.152 * EPA + 470  # mm
        empuxo = (EPA / 100) * 0.295  # conversão p/ cm² → kgf
        freq = 300 / (2 * (comprimento / 1000))  # Hz (velocidade som ~300m/s)

        resultado_area.config(
            text=f"Exhaust pipe area: {EPA:.2f} mm²\nValve flow area: {VFA:.2f} mm²")
        resultado_dimensao.config(
            text=f"Comprimento estimado: {comprimento:.1f} mm ({comprimento/1000:.3f} m)")
        resultado_empuxo.config(text=f"Empuxo estimado: {empuxo:.2f} kgf")
        resultado_freq.config(text=f"Frequência estimada: {freq:.1f} Hz")

    except ValueError:
        resultado_area.config(text="Erro: digite um número válido!")
        resultado_dimensao.config(text="")
        resultado_empuxo.config(text="")
        resultado_freq.config(text="")

# ---------------------------
# LAYOUT
# ---------------------------
container = tk.Frame(janela, bg=fundo_cor)
container.pack(expand=True, fill="both")

# Título
titulo = tk.Label(container, text="Pulsejet Calculator", fg=texto_cor, bg=fundo_cor, font=fonte_titulo)
titulo.pack(pady=25)

# Frame de entrada
entrada_frame = tk.Frame(container, bg=cor_frame, highlightbackground="#3A3A3A", highlightthickness=1)
entrada_frame.pack(pady=15, ipadx=10, ipady=10)

tk.Label(
    entrada_frame,
    text="Digite o raio do escape (mm):",
    fg=texto_cor,
    bg=cor_frame,
    font=fonte_texto
).pack(side="left", padx=8)

entrada = tk.Entry(entrada_frame, width=20, font=fonte_texto, relief="flat",
                   bg=cor_entrada, fg=texto_cor, insertbackground=texto_cor,
                   validate="key", validatecommand=vcmd)
entrada.pack(side="left", ipady=8, padx=10)

# Botão
def on_enter(e):
    botao_calc.config(bg=cor_hover)

def on_leave(e):
    botao_calc.config(bg=cor_botao)

botao_calc = tk.Button(container, text="Calcular", width=20, height=2,
                       bg=cor_botao, fg="white", font=fonte_botao, bd=0, relief="flat",
                       command=calcular, activebackground=cor_hover, cursor="hand2")
botao_calc.pack(pady=15)
botao_calc.bind("<Enter>", on_enter)
botao_calc.bind("<Leave>", on_leave)

# Frame de resultados
resultados_frame = tk.Frame(container, bg=cor_frame, highlightbackground="#3A3A3A", highlightthickness=1)
resultados_frame.pack(padx=40, pady=10, fill="x", ipadx=10, ipady=15)

resultado_area = tk.Label(resultados_frame, text="Aguardando cálculo...",
                          fg=cor_resultado, bg=cor_frame, font=fonte_resultado, justify="left")
resultado_area.pack(anchor="w", padx=20, pady=5)

resultado_dimensao = tk.Label(resultados_frame, text="", fg=cor_resultado,
                              bg=cor_frame, font=fonte_resultado, justify="left")
resultado_dimensao.pack(anchor="w", padx=20, pady=5)

resultado_empuxo = tk.Label(resultados_frame, text="", fg=cor_resultado,
                            bg=cor_frame, font=fonte_resultado, justify="left")
resultado_empuxo.pack(anchor="w", padx=20, pady=5)

resultado_freq = tk.Label(resultados_frame, text="", fg=cor_resultado,
                          bg=cor_frame, font=fonte_resultado, justify="left")
resultado_freq.pack(anchor="w", padx=20, pady=5)

# Rodapé
footer = tk.Label(janela, text="© 2025 Pulsejet Tools  |  by Victor Samuel",
                  fg="#666", bg=fundo_cor, font=("Segoe UI", 9))
footer.pack(side="bottom", pady=10)

janela.mainloop()
