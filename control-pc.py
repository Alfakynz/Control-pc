# All import
import subprocess
from tkinter import *
from tkinter import messagebox, ttk

# All functions
def shutdown():
    messagebox.showinfo("Info", "The pc will shutdown")
    subprocess.run(["shutdown", "/s", "/t", "1"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def sleep():
    messagebox.showinfo("Info", "The pc will turn to sleep")
    subprocess.run(["shutdown", "/h"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def restart():
    messagebox.showinfo("Info", "The pc will restart")
    subprocess.run(["shutdown", "/r", "/t", "1"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    quit()

def open_app(name):
    subprocess.run([name])

def quit_app():
    root.destroy()

def on_enter(event):
    event.widget["background"] = "#383838"
    event.widget["bordercolor"] = "black"

def on_leave(event):
    event.widget["background"] = "#1e1e1e"
    event.widget["bordercolor"] = "#1e1e1e"

# Principal window
root = Tk()
root.geometry("400x400")
root.title("Control PC")
root.resizable(width = True, height = True)

# Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand = True, fill = "both")

menu_tab = ttk.Frame(notebook)
apps_tab = ttk.Frame(notebook)
settings_tab = ttk.Frame(notebook)

notebook.add(menu_tab, text = "Menu")
notebook.add(apps_tab, text="Applications")
notebook.add(settings_tab, text = "Settings")

# Style
style = ttk.Style()
style.configure("TButton", padding = (5, 5, 5, 5), font = "Arial 12 bold", background = "#1e1e1e", borderwidth = 5, relief = "solid", bordercolor = "#1e1e1e", foreground = "#1e1e1e")

# Buttons
btn_shutdown = ttk.Button(menu_tab, text = "Shutdown", command = shutdown)
btn_shutdown.pack(pady = 10)

btn_sleep = ttk.Button(menu_tab, text = "Turn sleep", command = sleep)
btn_sleep.pack(pady = 10)

btn_restart = ttk.Button(menu_tab, text = "Restart", command = restart)
btn_restart.pack(pady = 10)

btn_openPsiphon = ttk.Button(apps_tab, text = "Open Psiphon", command = lambda: open_app(r"C:\Users\me\Apps\psiphon.exe"))
btn_openPsiphon.pack(pady = 10)

btn_quit = ttk.Button(menu_tab, text = "Quit", command = quit_app)
btn_quit.pack(pady = 10)

root.mainloop()