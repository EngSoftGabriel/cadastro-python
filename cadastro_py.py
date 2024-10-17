import PySimpleGUI as sg

# Lista para armazenar os cadastros
cadastros = []

# Função para adicionar um novo usuário
def cadastrar_usuario(nome, idade, email):
    usuario = {"nome": nome, "idade": idade, "email": email}
    cadastros.append(usuario)
    sg.popup("Usuário cadastrado com sucesso!")

# Função para exibir a lista de usuários
def listar_usuarios():
    if not cadastros:
        sg.popup("Nenhum usuário cadastrado.")
    else:
        lista = "\n".join(
            [f"{i+1}. {u['nome']} - {u['idade']} anos - {u['email']}" for i, u in enumerate(cadastros)]
        )
        sg.popup_scrolled(lista, title="Lista de Usuários", size=(50, 10))

# Função para buscar um usuário pelo nome
def buscar_usuario(nome):
    encontrados = [u for u in cadastros if u["nome"].lower() == nome.lower()]
    if encontrados:
        resultado = "\n".join(
            [f"{u['nome']} - {u['idade']} anos - {u['email']}" for u in encontrados]
        )
        sg.popup_scrolled(resultado, title="Usuários Encontrados")
    else:
        sg.popup("Usuário não encontrado.")

# Função para excluir um usuário pelo nome
def excluir_usuario(nome):
    global cadastros
    cadastros = [u for u in cadastros if u["nome"].lower() != nome.lower()]
    sg.popup(f"Usuários com o nome '{nome}' foram excluídos (se existiam).")

# Layout da interface gráfica
layout = [
    [sg.Text("Nome"), sg.Input(key="-NOME-")],
    [sg.Text("Idade"), sg.Input(key="-IDADE-")],
    [sg.Text("Email"), sg.Input(key="-EMAIL-")],
    [sg.Button("Cadastrar"), sg.Button("Listar Usuários")],
    [sg.Button("Buscar Usuário"), sg.Button("Excluir Usuário")],
    [sg.Button("Sair")],
]

# Criação da janela
janela = sg.Window("Sistema de Cadastro", layout)

# Loop principal da interface gráfica
while True:
    evento, valores = janela.read()

    if evento == sg.WINDOW_CLOSED or evento == "Sair":
        break
    elif evento == "Cadastrar":
        nome = valores["-NOME-"]
        idade = valores["-IDADE-"]
        email = valores["-EMAIL-"]
        if nome and idade and email:
            cadastrar_usuario(nome, idade, email)
        else:
            sg.popup("Preencha todos os campos!")
    elif evento == "Listar Usuários":
        listar_usuarios()
    elif evento == "Buscar Usuário":
        nome = sg.popup
