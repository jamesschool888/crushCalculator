import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk
import pygame
import random

def loadingScreen():
    pygame.mixer.music.stop()

def result():
    loadingScreen()
    rng = random.randint(1, 100)
    return rng

def destroyMainPage():
    global bgLabel, frame, label, entry1, entry2, button, data1, data2
    bgLabel.destroy()
    frame.destroy()
    label.destroy()
    entry1.destroy()
    entry2.destroy()
    button.destroy()
    resultPage()

def tryAgain():
    for widget in root.winfo_children():
        widget.destroy()
    mainPage()

def resultPage():
    global name1, name2, rngResult
    name1 = str(data1.get())
    name2 = str(data2.get())
    rngResult = result()

    if rngResult <= 10:
        ten()
    elif rngResult <= 20:
        twenty()
    elif rngResult <= 30:
        thirty()
    elif rngResult <= 40:
        forty()
    elif rngResult <= 50:
        fifty()
    elif rngResult <= 60:
        sixty()
    elif rngResult <= 70:
        seventy()
    elif rngResult > 70:
        final()

def ten():
    global menuButton, bgLabel, newBgImage
    bg = (Image.open(r'10.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=30, padx=30, side='bottom')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n halos wala kang pagasa sa kanya ahahah",  font=('Comic Sans MS', 20))
    label.pack(pady=12, padx=10)

    pygame.mixer.music.load(r'10.mp3')
    pygame.mixer.music.play(-1)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=12, padx=10)

def twenty():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'20.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'20.jpeg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='bottom')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n humanap ka na lang ng iba totoy",  font=('Comic Sans MS', 20))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def thirty():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'30.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'30.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='bottom')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n kung ayaw niya sau edi wag!!!!",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def forty():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'40.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'40.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='bottom')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n suyuin mo na lang",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def fifty():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'50.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'50.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='bottom')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n amen",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def sixty():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'60.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'60.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='left', anchor='sw')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n hahahh",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def seventy():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'70.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'70.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='left', anchor='sw')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n pang fubu kayo",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def final():
    global menuButton, bgLabel, newBgImage
    pygame.mixer.music.load(r'Kiss of Life.mp3')
    pygame.mixer.music.play(-1)

    bg = (Image.open(r'80.jpg')) 
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(pady=20, padx=30, side='left', anchor='sw')
    label = ctk.CTkLabel(master=frame, text=f"{name1} and {name2} are {rngResult}" + "% compatible!!!!\n bagay kaung dalawa",  font=('Comic Sans MS', 17))
    label.pack(pady=5, padx=10)

    menuButton = ctk.CTkButton(master=frame, text='try again', font=('Comic Sans MS', 15), command=tryAgain)
    menuButton.pack(pady=5, padx=10)

def mainPage():
    global bgLabel, frame, label, entry1, entry2, button, data1, data2, newBgImage
    bg = (Image.open(r'alden_maine.png'))
    bgResize = bg.resize((900, 525), Image.LANCZOS)
    newBgImage = ImageTk.PhotoImage(bgResize)
    
    bgLabel = Label(root, image=newBgImage)
    bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
    
    frame = ctk.CTkFrame(master=root, corner_radius=20)
    frame.pack(side='left', pady=10, padx=10)

    label = ctk.CTkLabel(master=frame, text="Crush Calculator", font=('Comic Sans MS', 24))
    label.pack(pady=12, padx=10)

    data1 = StringVar()
    data2 = StringVar()

    entry1 = ctk.CTkEntry(master=frame, textvariable=data1, placeholder_text='Test')
    entry1.pack(pady=12, padx=10)

    entry2 = ctk.CTkEntry(master=frame, textvariable=data2)
    entry2.pack(pady=12, padx=10)

    button = ctk.CTkButton(master=frame, text='Calculate', font=('Comic Sans MS', 15), command=destroyMainPage)
    button.pack(pady=12, padx=10)

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Crush Calculator")
    root.geometry("720x420")
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("green")

    pygame.init()
    pygame.mixer.music.load('ggmy1.mp3')
    pygame.mixer.music.play(-1)

    mainPage()
    root.mainloop()