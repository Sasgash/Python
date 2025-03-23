import customtkinter as ctk

# Configuração aparência
ctk.set_appearance_mode('dark')

# Criação de funções de funcionalidades


def validar_login():
    # .get para pegar o que foi esquito no entry em que atribuimos as variaveis campo_usuario e campo_senha
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    # Verificar se usuario = gash e senha igual Bibissauro@04
    if usuario == 'gash' and senha == 'Bibissauro@04':
        resultado_login.configure(text='Login feito com sucesso')
    else:
        resultado_login.configure(text='login incorreto')


# Criação da janela principal
app = ctk.CTk()
app.title('Sistema login')
app.geometry('500x300')

# Criação dos campos
# Label
label_usuario = ctk.CTkLabel(app, text='Usuário')
label_usuario.pack(pady=10)  # Distancia do elemento anterior e posterior

# Entry
# placeholder_text texto que esta escrito no entry
campo_usuario = ctk.CTkEntry(app, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

# Label
label_senha = ctk.CTkLabel(app, text='Senha')
label_senha.pack(pady=10)  # Distancia do elemento anterior e posterior

# Entry
# placeholder_text texto que esta escrito no entry
campo_senha = ctk.CTkEntry(app, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

# Button
botao = ctk.CTkButton(app, text='Login', command=validar_login)
botao.pack(pady=10)

# Campo feedback de login
resultado_login = ctk.CTkLabel(app, text='')
resultado_login.pack(pady=10)
# Criação das funções de funcionalidades

# Iniciar a aplicação
app.mainloop()
