# Gerar de Claquetes🎬

📝 **Descrição**

Este projeto consiste em um aplicativo gerador de claquetes para produções audiovisuais. O aplicativo é desenvolvido em Python e utiliza as bibliotecas Pillow, FFmpeg e Tkinter para criar uma claquete com até 5 segundos de duração, fade-in e fade-out, informações de projeto, data e hora, informações de cena, take, diretor e outras especificidades de produção audiovisual. O usuário pode inserir os dados necessários para gerar a claquete.

🔖 **Tags**

#Python #Pillow #FFmpeg #Tkinter #ProduçãoAudiovisual

🔗 **Referências**

- [Site oficial do Python](https://www.python.org/)
- [Documentação da biblioteca Pillow](https://pillow.readthedocs.io/en/stable/)
- [Documentação da biblioteca FFmpeg](https://ffmpeg.org/documentation.html)
- [Documentação da biblioteca Tkinter](https://docs.python.org/3/library/tkinter.html)

🚀 **Instruções de Início**

1. Clone o repositório para sua máquina local:

```
git clone https://github.com/seu_usuario/nome_do_projeto.git
```

2. Instale as dependências necessárias:

```
pip install pillow
pip install ffmpeg-python
pip install tkinter
```

3. Execute o arquivo `claquete.py` para iniciar o aplicativo:

```
python claquete.py
```

4. Insira as informações necessárias para gerar a claquete e clique em "Gerar Claquete".

5. A claquete gerada será salva no diretório do projeto com o nome `claquete.mp4`.

6. Para criar um executável, utilize o PyInstaller:

```
pip install pyinstaller
pyinstaller --onefile claquete.py
```

O executável será gerado na pasta `dist/` do projeto.

