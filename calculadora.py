import tkinter as tk

def clicar(tecla):
    entrada.insert(tk.END, tecla)

def calcular():
    expression = entrada.get().replace('x', '*')
    entrada.delete(0, tk.END)
    try:
        resultado = eval(expression)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.insert(tk.END, "Erro")

def limpar():
    entrada.delete(0, 'end')

def limparUm():
    entrada.delete(len(entrada.get())-1, 'end')

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=20, font=('Arial', 18, 'bold'), bd=5, justify='right')
entrada.grid(row=0, column=0, columnspan=4, pady=10)

botoes = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', 'x'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

for i, linha in enumerate(botoes):
    for j, texto in enumerate(linha):
        if texto == '=':
            btn = tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 16), command=calcular)
        else:
            btn = tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 16), command=lambda t=texto: clicar(t))
        btn.grid(row=i+1, column=j, padx=5, pady=5)

btn_limpar = tk.Button(janela, text='C', width=12, height=2, font=('Arial', 16), command=limpar)
btn_limpar.grid(row=11, column=0, columnspan=2, padx=5, pady=5)

btn_limparUm = tk.Button(janela, text='<', width=12, height=2, font=('Arial', 16), command=limparUm)
btn_limparUm.grid(row=11, column=2, columnspan=2, padx=5, pady=5)


janela.mainloop()
