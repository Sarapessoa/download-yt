## Descrição

Este é um projeto de um downloader de vídeos do YouTube, construído em Python usando as bibliotecas PyTube e MoviePy. O projeto também usa as bibliotecas Tkinter e Pygame para criar uma interface gráfica simples.

## Tecnologias Usadas

- Python
- PyTube
- MoviePy
- Tkinter
- Pygame

## Requisitos

- Python 3.7 ou superior
- PyTube
- MoviePy
- Tkinter
- Pygame

## Como usar

1. Clone este repositório em sua máquina local.<br>
2. Abra o arquivo `downloader.py` em um editor de código Python.<br>
3. Certifique-se de que as bibliotecas necessárias estão instaladas em seu ambiente de desenvolvimento.<br>
4. Execute o arquivo `downloader.py`.<br>
5. Insira o link do vídeo do YouTube que deseja baixar.<br>
6. Clique no botão "Baixar e converter vídeo".<br>
7. Aguarde enquanto o vídeo é baixado e convertido em um arquivo MP3.<br>
8. Quando o download e a conversão estiverem concluídos, você ouvirá um som de sucesso e verá uma mensagem de status.<br>

## Estrutura do código

O código está dividido em duas partes principais:<br><br>

1. `Função download_video()`: responsável por baixar e converter o vídeo.<br>
2. `Função start_download_thread()`: responsável por iniciar uma nova thread para a função `download_video()`.<br>

A interface gráfica foi criada com o uso das bibliotecas Tkinter e Pygame, permitindo que o usuário insira o link do vídeo
a ser baixado e clique em um botão para iniciar o download e conversão. A mensagem de status é exibida em uma label na tela.


## Autor

Sara Pessoa Silva
