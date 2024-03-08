import os
import subprocess
from tkinter import *
from tkinter import messagebox, ttk

def shutdown():
    messagebox.showinfo('Info', 'Le pc va s\'éteindre')
    subprocess.run(["shutdown", "/s", "/t", "1"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def sleep():
    messagebox.showinfo('Info', 'Le pc va se mettre en veille')
    subprocess.run(["shutdown", "/h"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def restart():
    messagebox.showinfo('Info', 'Le pc va redémarrer')
    subprocess.run(["shutdown", "/r", "/t", "1"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def open_app(name):
    subprocess.run([name])

def quit_app():
    root.destroy()

def on_enter(event):
    event.widget['background'] = '#383838'
    event.widget['bordercolor'] = 'black'

def on_leave(event):
    event.widget['background'] = '#1e1e1e'
    event.widget['bordercolor'] = '#1e1e1e'

def show_settings():
    notebook.select(settings_tab)

# Créer la fenêtre principale
root = Tk()
root.geometry('500x500')
root.title("Contrôle PC")
root.resizable(width = True, height = True)
root['bg'] = '#1e1e1e'

label = Label(root, text = "Que veux-tu faire ?", font = "Arial 20 bold", bg = "#1e1e1e", fg = "white")
label.pack(pady = 10)

notebook = ttk.Notebook(root)
notebook.pack(pady = 10, expand = True, fill = "both")

actions_tab = ttk.Frame(notebook)
notebook.add(actions_tab, text="Actions")

settings_tab = ttk.Frame(notebook)
notebook.add(settings_tab, text = "Paramètres")

# Créer les boutons
style = ttk.Style()
style.configure("TButton", padding = (8, 8, 8, 8), font = "Arial 17 bold", background = "#1e1e1e", borderwidth = 5, relief = "solid", bordercolor = "#1e1e1e", foreground = "#1e1e1e")

btn_shutdown = ttk.Button(root, text = "Éteindre", command = shutdown)
btn_shutdown.pack(pady = 10)

btn_sleep = ttk.Button(root, text = "Mettre en veille", command = sleep)
btn_sleep.pack(pady = 10)

btn_restart = ttk.Button(root, text = "Redémarrer", command = restart)
btn_restart.pack(pady = 10)

btn_openPsiphon = ttk.Button(settings_tab, text = "Ouvrir Psiphon", command = lambda: open_app(r"C:\Users\me\Apps\psiphon.exe"))
btn_openPsiphon.pack(pady = 10)

btn_settings = ttk.Button(root, text = "Paramètres", command = show_settings)
btn_settings.pack(pady = 10)

btn_quit = ttk.Button(root, text = "Quitter", command = quit_app)
btn_quit.pack(pady = 10)

root.mainloop()