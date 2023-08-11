import tkinter as tk


def adicionar_numero(numero):
  entrada_texto.insert(tk.END, numero)


def realizar_calculo():
  try:
    expressao = entrada_texto.get()
    resultado = eval(expressao)
    entrada_texto.delete(0, tk.END)
    entrada_texto.insert(tk.END, resultado)
  except Exception as e:
    entrada_texto.delete(0, tk.END)
    entrada_texto.insert(tk.END, "Erro")


def limpar():
  entrada_texto.delete(0, tk.END)


# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Entrada de texto
entrada_texto = tk.Entry(janela, font=("Arial", 20))
entrada_texto.grid(row=0, column=0, columnspan=4)

# Organização da disposição dos botões
botoes = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('4', 2, 0),
          ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('1', 3, 0), ('2', 3, 1),
          ('3', 3, 2), ('-', 3, 3), ('0', 4, 0), ('.', 4, 1), ('=', 4, 2),
          ('+', 4, 3), ('C', 5, 0)]

# Criação dos botões
for (simbolo, linha, coluna) in botoes:
  botao = tk.Button(janela, text=simbolo, font=("Arial", 20))
  botao.grid(row=linha, column=coluna)
  if simbolo != '=' and simbolo != 'C':
    botao.configure(command=lambda simbolo=simbolo: adicionar_numero(simbolo))
  elif simbolo == '=':
    botao.configure(command=realizar_calculo)
  else:
    botao.configure(command=limpar)

# Iniciar a interface
janela.mainloop()
