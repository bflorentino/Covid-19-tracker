from tkinter import *
from typing import Reversible
from PIL import Image, ImageTk
import Scrapper

root = Tk()
root.title("Basic Covid-19 Tracker")
root.geometry("850x600")
root.resizable(False, False)
root.config(background="white")
root.iconbitmap("Img.ico")

# Covid-19 Cases Frame 
Cases = Frame(root, bg = "white")
Cases.pack(padx = (30,0), pady=(50, 0))
labelCasesTitle = Label(Cases, text = "Covid-19 Cases:", font = ("Arial", 30), fg = "#281D1D", bg = "white")
labelCasesTitle.pack(anchor="center", pady = (0, 20))
TextCases = StringVar()
labelCases = Label(Cases, textvariable=TextCases, font = ("Arial", 25),fg = "#A7A2A2", bg = "white")
labelCases.pack()

# Covid-19 Deaths Frame 
Deaths = Frame(root, bg = "white")
Deaths.pack(padx = (30,0), pady=(30, 0))
labelDeathsTitle = Label(Deaths, text = "Deaths:", font = ("Arial", 30), fg = "#281D1D", padx = 50, bg = "white")
labelDeathsTitle.pack( anchor="center", pady = (0, 20))
TextDeaths = StringVar()
labelDeaths = Label(Deaths, textvariable=TextDeaths, font = ("Arial", 25),fg = "red", bg = "white")
labelDeaths.pack()

# Covid-19 Recovered Frame 
Recovered = Frame(root, bg = "white")
Recovered.pack(padx = (30,0), pady=(30, 0))
labelRecoveredTitle = Label(Recovered, text = "Recovered:", font = ("Arial", 30), fg = "#281D1D", padx = 50, bg = "white")
labelRecoveredTitle.pack(anchor="center", pady = (0, 20))
TextRecovered = StringVar()
labelRecovered = Label(Recovered, textvariable=TextRecovered, font = ("Arial", 25),fg = "green", bg = "white")
labelRecovered.pack()

# Update Info Button 
btnFrame = Frame(root, bg = "white")
btnFrame.pack()
ButtonUpdate = Button(btnFrame, text = "Update", padx = 5, font = ("Arial", 20), bg = "#58B61C", fg = "white", bd = 0, cursor="hand2", command= lambda: Scrapper.updateCovid19Info(TextCases, TextDeaths, TextRecovered))
ButtonUpdate.pack(pady = (30,5))

Scrapper.updateCovid19Info(TextCases, TextDeaths, TextRecovered)

root.mainloop()