import tkinter as tk
from tkinter import ttk  # Importa caixas de seleção

# Cria janela principal
viga = tk.Tk()
viga.title("VIGA")

# Lista com itens que o usuário deve preencher
campos = [
    "Vão da Viga (m):",
    "Largura da Seção - bw (cm):",
    "Altura da Seção - h (cm):",
    "Cobrimento (cm):",
    "Resistência do Concreto - fck (MPa):",
    "Carregamento (kN/m):"]

entradas = []

# Cria texto e caixa vazia
for i, txt in enumerate(campos):
  tk.Label(viga, text=txt).pack()
  e = tk.Entry(viga)
  e.pack()
  entradas.append(e)  # Guarda a caixinha na lista

# Para o fck, verificar preenchimento
  if i == 4:
    aviso_fck = tk.Label(viga, text="", fg="red", font=("Arial", 8))
    aviso_fck.pack()

# Opções classe do aço
tk.Label(viga, text="Classe do Aço:").pack()
# Cria a caixa com opções
opção_aco = ttk.Combobox(viga, values=["CA-50", "CA-60"], state="readonly")
opção_aco.pack()

# Botão executado
def clicar():
  try:
    # Lê o valor do fck e transforma em número decimal
    fck_valor = float(entradas[4].get())

    # Verifica se está no intervalo permitido
    if fck_valor < 20 or fck_valor > 90:
      aviso_fck.config(text="⚠️ Atenção: O fck deve estar entre 20 e 90 MPa!")
    else:
      aviso_fck.config(text="")  # Limpa o aviso se estiver tudo certo

  except ValueError:
    # Se o utilizador escrever letras em vez de números
    aviso_fck.config(text="⚠️ Erro: Digite apenas números!")

# Cria o botão
tk.Button(
    viga, text="Ok", bg="green", fg="white", font=("Arial", 12, "bold"), command=clicar
).pack(pady=15)

viga.mainloop()