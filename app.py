import tkinter as tk 
from tkinter import filedialog, Text
import os


root = tk.Tk()

apps = []
if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()


    filename = filedialog.askopenfilename(initialdir="/",title = "select file",
    filetypes=(("executables","*.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text = app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=500, width=500,bg="#a9a9a9")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight= 0.8,relx=0.1,rely=0.1)

openFile = tk.Button(root, text="openfile", 
padx=10,pady=5,fg="white",bg="blue" ,command =addApp)
openFile.pack()

runapps = tk.Button(root, text="runapps", padx=10,pady=5,fg="white",bg="blue", command= runApps)
runapps.pack()
root.mainloop() 

for app in apps:
    label = tk.Label(frame, Text=app)
    label.pack()
with open('save.txt','w') as f:
    for app in apps:
        f.write(app + ',')