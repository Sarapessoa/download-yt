import os
import threading
from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
import tkinter.ttk as ttk
import pygame

pygame.init()
success_sound = pygame.mixer.Sound('effect/success.mp3')

def download_video():
    link = entry.get()
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        output_file = stream.default_filename
        stream.download()
        videoclip = VideoFileClip(output_file)
        audioclip = videoclip.audio
        output_folder = "mp3"
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        output_path = os.path.join(output_folder, output_file[:-4] + '.mp3')
        audioclip.write_audiofile(output_path)
        audioclip.close()
        videoclip.close()
        os.remove(output_file)
        success_sound.play()
        status_label.config(text="Download e conversão do vídeo concluídos com sucesso!")
        entry.delete(0, tk.END)
        root.after(4000, lambda: status_label.config(text=""))
    except Exception as e:
        status_label.config(text="Erro ao baixar e converter o vídeo: {}".format(str(e)))

def start_download_thread():
    thread = threading.Thread(target=download_video)
    thread.start()

root = tk.Tk()

root.attributes('-fullscreen', True)

root.geometry('{}x{}+0+0'.format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.geometry('{}x{}+{}+{}'.format(root.winfo_screenwidth(), root.winfo_screenheight(), root.winfo_screenwidth() // 2, root.winfo_screenheight() // 2))
root.attributes('-fullscreen', False)

label = tk.Label(root, text="Insira seu link!", font=("Arial", 20))
label.pack()
label.place(relx=0.5, rely=0.4, anchor='center')

entry = tk.Entry(root, width=60)
entry.pack(side='top', fill='both', expand=True)
entry.place(relx=0.5, rely=0.5, anchor='center')

style = ttk.Style()
style.configure("Custom.TButton", font=("Arial", 12), foreground="red", background="red")

button = ttk.Button(root, width=40, style="Custom.TButton" ,text="Baixar e converter vídeo" ,command=start_download_thread)
button.pack(side='top', fill='both', expand=True)
button.place(relx=0.5, rely=0.6, anchor='center')

status_label = tk.Label(root, font=("Arial", 16))
status_label.pack(side='top', fill='both', expand=True)
status_label.place(relx=0.5, rely=0.7, anchor='center')

root.mainloop()
