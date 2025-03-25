import customtkinter as ctk #Importação da biblioteca para criar interface
import random #Importação da biblioteca que randomiza numeros

app = ctk.CTk()
app.title('Sistema de sorteio')
app.geometry('300x700')

lista_nomes = []

def dez(): #Função para sortear de 1 a 10
    lista = list(range(1, 11)) #O comando lista cria uma lista com o range de 10, e com isso atribui a uma variavel chamada lista, que aqui no caso vai de 1 a 10
    numero_sorteado = random.choice(lista) #Esse comano random escolhe um numero aleatório de acordo com o intervalo que da lista, esse numero aleatório é atribuido a uma variavel

    label_resultado.configure(text=f'Número sorteado é: {numero_sorteado}') #Aqui eu imprimo o numero aleatório ao label (tela) informado, que no caso ´o label_resultado

def cem(): #Função para sortear de 1 a 100
    lista = list(range(1, 101))#O comando list cria uma lista com o range de 100, e com isso atribui a uma variavel chamada lista, que aqui no caso vai de 1 a 100
    numero_sorteado = random.choice(lista) #Esse comano random escolhe um numero aleatório de acordo com o intervalo que da lista, esse numero aleatório é atribuido a uma variavel

    label_resultado.configure(text=f'Número sorteado é: {numero_sorteado}') #Aqui eu imprimo o numero aleatório ao label (tela) informado, que no caso ´o label_resultado

def mil(): #Função para sortear de 1 a 1000
    lista = list(range(1, 1001)) #O comando list cria uma lista com o range de 100, e com isso atribui a uma variavel chamada lista, que aqui no caso vai de 1 a 1000
    numero_sorteado = random.choice(lista) #Esse comano random escolhe um numero aleatório de acordo com o intervalo que da lista, esse numero aleatório é atribuido a uma variavel

    label_resultado.configure(text=f'Número sorteado é: {numero_sorteado}') #Aqui eu imprimo o numero aleatório ao label (tela) informado, que no caso ´o label_resultado

def intervalo(): #Função para sortear no intervalo desejado
    num = int(input_invtervalo.get()) #Nessa linha eu precisava pegar o número que o usuario iria colocar no input (input_intervalo) para criar uma lista com o intervalo desejado, por isso usei o .get, ele pega o que foi escrito no input e atribui a uma variavel
    lista = list(range(1, num + 1 )) #Nessa linha eu criei a lista novamente com o comano list, so que dessa vez o range ia do 1 ate o numero que foi pego no input_intervalo + 1 para contar o intervalo todo
    numero_sorteado = random.choice(lista)
    if num == 1:
        label_resultado.configure(text='Informe um número maior que 1')
    else:     
        label_resultado.configure(text=f'Número sorteado é: {numero_sorteado}') #Nessas ultimas 4 linhas eu criei uma verificação para que o usuário não digitasse 1, pois nao tem como fazer sorteio com apenas um numero, e se ele no digitasse 1 iria imprimir normalemnte no label_resultado

def nomes(): #Função para adicionar uma lista de nomes no botao adicionar
    
    nome = input_nomes.get() #Nessa linha eu preciava pegar o nome que o usuario iria colocar no input de input_nomes e atribuir a uma variavel
    if not nome:  #Este if confere se a variavel nome está vazia
        label_resultado.configure(text='Digite um nome!') #Se ela estiver o label_resultado ira mostrar 'Digite outro nome!'
        return

    if nome in lista_nomes:  #Com o comando in eu confiro se o nome que esta na variavel nome informado pelo usuario nao esta no vetor lista_nomes
        label_resultado.configure(text='Nome já adicionado!') #Se ja estiver adicionado o label ira mostar 'Nome ja adicionado'
    else: # Se nao tiver sido adicionado e nem em branco a função ira adicionar o nome informado pelo usuario na lista_nomes
        lista_nomes.append(nome) #O comando append adiciona um valor dentro da ultima posição do vetor, no caso entre parenteses esta informando que o valor adicionado no vetoe lista_nomes é a variavel nome
        label_resultado.configure(text='Nome adicionado!') #Aqui eu imprimo o nome aleatório ao label (tela) informado, que no caso ´o label_resultado


def sortear_nome(): #Função para adicionar o nome
    
    nome_sorteado = random.choice(lista_nomes) # type: ignore
    if lista_nomes:  # Se a lista não estiver vazia
        nome_sorteado = random.choice(lista_nomes)
        label_resultado.configure(text=f'Nome sorteado: {nome_sorteado}')
    else:
        label_resultado.configure(text='Nenhum nome na lista!')

#Label 1 a 10
label_10 = ctk.CTkLabel(app, text='Sortear de 1 a 10',font= ("Arial", 16))
label_10.pack(pady=10)

#Botao para sortear de 1 a 10
botao_10 = ctk.CTkButton(app, text='Sortear', command=dez)
botao_10.pack(pady=10)

#Label 1 a 100
label_100 = ctk.CTkLabel(app, text='Sortear de 1 a 100', font= ("Arial", 16))
label_100.pack(pady=10)

#Botao para sortear de 1 a 100
botao_100 = ctk.CTkButton(app, text='Sortear', command=cem)
botao_100.pack(pady=10)

#Label 1 a 1000
label_1000 = ctk.CTkLabel(app, text='Sortear de 1 a 1000', font= ("Arial", 16))
label_1000.pack(pady=10)

#Botao para sortear de 1 a 1000
botao_1000 = ctk.CTkButton(app, text='Sortear', command=mil)
botao_1000.pack(pady=10)

#Label do intervalo desejado pelo usuário
label_invtervalo = ctk.CTkLabel(app, text='Sortear intervalo deseado', font= ("Arial", 16))
label_invtervalo.pack(pady=10)

#Input onde o usuário informa o intervalo desejado
input_invtervalo = ctk.CTkEntry(app, placeholder_text='Intervalo')
input_invtervalo.pack(pady=10)

#Botao para sortear um numero no intervalo desejado pelo usuário
botao_intervalo = ctk.CTkButton(app, text='Sortear', command=intervalo)
botao_intervalo.pack(pady=10)

#Label do nome desejado do usuario

label_nomes = ctk.CTkLabel(app, text='Sortear nome deseado', font= ("Arial", 16))
label_nomes.pack(pady=10)

#Input para informar o nome que vai ser adicionado 

input_nomes = ctk.CTkEntry(app, placeholder_text='Nome')
input_nomes.pack(pady=10)

#Botão para adiocionar o nome escrito

botao_nomes_adicionar = ctk.CTkButton(app, text='Adicionar', command=nomes)
botao_nomes_adicionar.pack(pady=10)

#Botão para sortear o nome da lista

botao_nomes = ctk.CTkButton(app, text='Sortear', command=sortear_nome)
botao_nomes.pack(pady=10)

#Label onde aparece o resultado dos sorteios, está em branco o text pois com o .configure usado nas funções o que aparecera na tela dependera do resultado das funções

label_resultado = ctk.CTkLabel(app, text='', font= ("Arial", 18))
label_resultado.pack(pady=10)



app.mainloop()


#Código feito por Gabriel Fernandes de Abreu GitHub: Sasgash