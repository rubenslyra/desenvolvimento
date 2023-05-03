import os
from tkinter import *
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from ffmpeg import *


# Função que gera a imagem da claquete com os dados inseridos


def gerar_claquete(diretor, cena, take, titulo, duracao):
    # Criar imagem em branco
    img = Image.new('RGB', (800, 600), color='blue')
    draw = ImageDraw.Draw(img)

    # Adicionar texto com as informações da claquete
    font = ImageFont.truetype('arial.ttf', size=30)
    draw.text((100, 100), f"Diretor: {diretor}", font=font, fill='white')
    draw.text((100, 150), f"Cena: {cena}", font=font, fill='white')
    draw.text((100, 200), f"Take: {take}", font=font, fill='white')
    draw.text((100, 250), f"Titulo: {titulo}", font=font, fill='white')
    draw.text(
        (100, 300), f"Duracao: {duracao} segundos", font=font, fill='white')

    # Adicionar data e hora na claquete
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    draw.text((500, 500), data_hora, font=font, fill='white')

    # diretório outputs/
    if not os.path.exists('outputs/'):
        os.makedirs('outputs/')

    # Salvar imagem da claquete no diretório outputs/ com o nome "claquete.png" adicionando 1 no final do nome caso já exista
    i = 1
    while os.path.exists(f"outputs/claquete{i}.png"):
        i = + 1
    img.save(f"outputs/claquete{i}.png")

    # adiciona 1 no final do nome do vídeo caso já exista
    vi = 1
    while os.path.exists(f"outputs/claquete{vi}.mp4"):
        vi = + 1

    # Criar vídeo .mp4 de 5seg com a claquete libx264 e exportar  para o diretório atual com o nome "Claquete.mp4" incluindo fade-in e fade-out
    os.system(
        f'ffmpeg -loop 1 -i outputs/claquete{i}.png -c:v libx264 -t 5 -pix_fmt yuv420p -vf "fade=in:0:30,fade=out:120:30" outputs/claquete{vi}.mp4')

    # Exibir mensagem de sucesso no terminal
    terminal.insert(END, "Claquete gerada com sucesso!")


# Criar interface gráfica com tkinter
janela = Tk()
janela.geometry("400x400")


# Trocar o ícone da janela para o ícone "iconClaquete.png" no diretório atual
janela.iconbitmap("./assets/iconClaquete.ico")

# Título da janela
janela.title("Gerador de Claquete")

# Cor de fundo da janela em hexadecimal
janela["bg"] = "#302F2F"

# Adicionar campos de entrada para os dados da claquete
diretor = Entry(janela, width=30)
cena = Entry(janela, width=30)
take = Entry(janela, width=30)


projeto_label = Label(janela, text="Projeto:")
projeto_label.pack()
projeto = Entry(janela, width=30)
projeto.pack()

titulo_label = Label(janela, text="Título:")
titulo_label.pack()
titulo = Entry(janela, width=30)
titulo.pack()

cena_label = Label(janela, text="Cena:")
cena_label.pack()
cena.pack()

take_label = Label(janela, text="Take:")
take_label.pack()
take.pack()

duracao_label = Label(janela, text="Duração:")
duracao_label.pack()
duracao = Entry(janela, width=30)
duracao.pack()

diretor_label = Label(janela, text="Diretor:")
diretor_label.pack()
diretor.pack()

# dados de data e hora da claquete com datetime do python
data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Função que chama a função "gerar_claquete" passando os dados inseridos nos campos de entrada


def exportar_claquete():
    gerar_claquete(diretor.get(), cena.get(), take.get(),
                   titulo.get(), duracao.get())


# Função para validar os campos de entrada
# def validar_campos():
#     if diretor.get() == "" or cena.get() == "" or take.get() == "" or titulo.get() == "" or duracao.get() == "":
#         return False
#     else:
#         return True


# Cor de fundo dos títulos de entrada em hexadecimal
projeto_label["bg"] = "#302F2F"
titulo_label["bg"] = "#302F2F"
cena_label["bg"] = "#302F2F"
take_label["bg"] = "#302F2F"
duracao_label["bg"] = "#302F2F"
diretor_label["bg"] = "#302F2F"

# Cor do texto dos títulos de entrada em hexadecimal
projeto_label["fg"] = "#FFFFFF"
titulo_label["fg"] = "#FFFFFF"
cena_label["fg"] = "#FFFFFF"
take_label["fg"] = "#FFFFFF"
duracao_label["fg"] = "#FFFFFF"
diretor_label["fg"] = "#FFFFFF"


# Botão para exportar a claquete com o texto "Exportar claquete" que chama a função "exportar_claquete" quando clicado
exportar = Button(janela, text="Exportar claquete",
                  command=exportar_claquete)
exportar.pack()

# Botão para fechar a janela com o texto "Fechar" que chama a função "janela.destroy" quando clicado

fechar = Button(janela, text="Fechar", command=janela.destroy)


# Criar um terminal para exibir as etapas do processo de geração da claquete
terminal = Text(janela, height=10, width=50, bg="#302F2F", fg="#FFFFFF")
terminal.pack()

# Adicionar texto ao terminal
terminal.insert(END, "Bem vindo ao gerador de claquete!\n")
terminal.insert(
    END, "Preencha os campos de entrada e clique em exportar claquete para gerar a claquete.\n")


# Iniciar janela
janela.mainloop()
