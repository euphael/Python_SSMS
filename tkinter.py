import tkinter as tk
from tkinter import ttk

# criar a janela principal
root = tk.Tk()
root.title("Dados da OR")

# Criar um frame central para conter os widgets
central_frame = tk.Frame(root)
central_frame.pack(pady=20, padx=20)

# criar o input "Número da OR"
label_or = tk.Label(central_frame, text="Número da OR:")
label_or.grid(row=0, column=0, sticky="w", padx=5, pady=5)

input_or = tk.Entry(central_frame, width=47)
input_or.grid(row=0, column=1, padx=5, pady=5)

# adicionar lista com os dados da OR com scrollbar
frame_listbox_or = tk.Frame(central_frame)
frame_listbox_or.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

listbox_or = tk.Listbox(frame_listbox_or, width=75, height=15)
listbox_or.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_or = tk.Scrollbar(frame_listbox_or, orient="vertical", command=listbox_or.yview)
scrollbar_or.pack(side=tk.RIGHT, fill="y")

listbox_or.config(yscrollcommand=scrollbar_or.set)

# adicionar combobox de itens
label_item = tk.Label(central_frame, text="Selecione o item:")
label_item.grid(row=2, column=0, sticky="w", padx=5, pady=5)

combo_items = ttk.Combobox(central_frame, values=["Item 1", "Item 2", "Item 3"], width=75)
combo_items.grid(row=2, column=1, padx=5, pady=5)

# adicionar input para quantidade de itens
label_quantidade = tk.Label(central_frame, text="Quantidade:")
label_quantidade.grid(row=3, column=0, sticky="w", padx=5, pady=5)

input_quantidade = tk.Entry(central_frame, width=75)
input_quantidade.grid(row=3, column=1, padx=5, pady=5)

# adicionar botão para adicionar dados da OR na lista
button_add = tk.Button(central_frame, text="Adicionar")
button_add.grid(row=4, column=0, columnspan=2, pady=5, sticky="ew")

# Nova Listbox para itens adicionados com scrollbar
frame_listbox_itens_adicionados = tk.Frame(central_frame)
frame_listbox_itens_adicionados.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

listbox_itens_adicionados = tk.Listbox(frame_listbox_itens_adicionados, width=75, height=15)
listbox_itens_adicionados.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_itens_adicionados = tk.Scrollbar(frame_listbox_itens_adicionados, orient="vertical", command=listbox_itens_adicionados.yview)
scrollbar_itens_adicionados.pack(side=tk.RIGHT, fill="y")

listbox_itens_adicionados.config(yscrollcommand=scrollbar_itens_adicionados.set)

# adicionar botão para remover item selecionado
button_remove = tk.Button(central_frame, text="Remover Item Selecionado")
button_remove.grid(row=6, column=0, columnspan=2, pady=5, sticky="ew")

# adicionar botão para gerar planilhas
button_generate = tk.Button(central_frame, text="Gerar Planilhas")
button_generate.grid(row=7, column=0, columnspan=2, pady=5, sticky="ew")

def add_or_to_list():
    or_number = input_or.get()
    item = combo_items.get()
    quantity = input_quantidade.get()
    
    # Adicionar dados na nova Listbox
    listbox_itens_adicionados.insert(tk.END, f"Número da OR: {or_number}, Produto: {item}, Quantidade: {quantity}")

def remove_selected_item():
    selected_index = listbox_itens_adicionados.curselection()
    if selected_index:
        listbox_itens_adicionados.delete(selected_index)

# Vincular a função add_or_to_list ao botão "Adicionar"
button_add.config(command=add_or_to_list)

# Vincular a função remove_selected_item ao botão "Remover Item Selecionado"
button_remove.config(command=remove_selected_item)

root.mainloop()