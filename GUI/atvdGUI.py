import tkinter as tk
from tkinter import ttk

# WIDGET WINDOW
# janela = tk.Tk() # janela redimensionavel PRINCIPAL
# janela.title("GUI TESTE")
# janela.resizable(False,False)

# WIDGET LABEL
# ttk.Label(janela, text= "componente Label").grid(column=0, row=0)

# WIDGET BUTTON
import tkinter as tk
contador = 0
def contador_label(lblRotulo):
   def funcao_contar():
      global contador
      contador = contador + 1
      lblRotulo.config(text=str(contador))
      lblRotulo.after(1, funcao_contar)
      funcao_contar()
janela = tk.Tk()
janela.title("Contagem dos Segundos")
lblRotulo = ttk.Label(janela,foreground='green')
lblRotulo.pack()
contador_label(lblRotulo)
btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()
janela.mainloop()


