# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:48:19 2015

@author: pieagbo
"""

from tkinter import *
from Model import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        
        self.IAs = set()
        self.human = None        
        
        self.fenetre = fenetre
        
        self.wantQuit = 1
        
        self.playerColor = Color.BLUE
        self.IALevel = None
        
        self.pack(fill=BOTH)
        
        self.message = Label(self, text="Thurn And Taxis !", font="Helvetica 13")     
        
        self.settingsFrame = LabelFrame(self, text="Parametres de jeu", padx=15, pady=15)
    
        self.playerName = StringVar() 
        self.playerName.set("Rangivaru")
        self.playerNameLabel = Label(self.settingsFrame, text="Entrez un nom : ")   
        self.playerNameInput = Entry(self.settingsFrame, textvariable=self.playerName, width=40)
        
        self.playerColorLabel = Label(self.settingsFrame, text="Choisissez votre couleur : ")   
        self.playerColorButtonBlue = Button(self.settingsFrame, bg="blue", relief=FLAT, width=10, command=lambda: self.chooseColor(Color.BLUE))
        self.playerColorButtonYellow = Button(self.settingsFrame, bg="yellow", relief=FLAT, width=10, command=lambda: self.chooseColor(Color.YELLOW))
        self.playerColorButtonRed = Button(self.settingsFrame, bg="red", relief=FLAT, width=10, command=lambda: self.chooseColor(Color.RED))
        self.playerColorButtonGreen = Button(self.settingsFrame, bg="green", relief=FLAT, width=10, command=lambda: self.chooseColor(Color.GREEN))
        
        self.IALevelLabel = Label(self.settingsFrame, text="Choisissez le niveau des IA : ")
        self.IALevelValue = StringVar()
        self.IALevelValue.set('Novice')
        self.IALevelNovice = Radiobutton(self.settingsFrame, text="Novice", variable=self.IALevelValue, value='Novice')
        self.IALevelIntermediate = Radiobutton(self.settingsFrame, text="Moyen", variable=self.IALevelValue, value='Intermediate')
        self.IALevelExpert = Radiobutton(self.settingsFrame, text="Expert", variable=self.IALevelValue, value='Expert')
        
#        self.firstPlayerLabel = Label(self.settingsFrame, text="Souhaitez-vous commencer ?")
#        self.firstPlayer = StringVar() 
#        self.firstPlayer.set('Non')
#        self.firstPlayerYes = Radiobutton(self.settingsFrame, text="Oui", variable=self.firstPlayer, value='Oui')
#        self.firstPlayerNo = Radiobutton(self.settingsFrame, text="Non", variable=self.firstPlayer, value='Non')
        
        self.play = Button(self, text="Jouer", width=10, command=self.playGame)
        self.quit = Button(self, text="Quitter", width=10, command=self.fenetre.destroy)

        self.message.pack()
        self.settingsFrame.pack(fill="y", expand="no")
        self.playerNameLabel.grid(row=0,column=0,)
        self.playerNameInput.grid(row=0,column=1, columnspan=3)
        self.playerColorLabel.grid(row=1,column=0, pady=5)
        self.playerColorButtonBlue.grid(row=1,column=1, pady=5)
        self.playerColorButtonYellow.grid(row=1,column=2, pady=5)
        self.playerColorButtonRed.grid(row=1,column=3, pady=5)
        self.playerColorButtonGreen.grid(row=1,column=4, pady=5)
        self.IALevelLabel.grid(row=2,column=0,pady=5)
        self.IALevelNovice.grid(row=2,column=1,pady=5)
        self.IALevelIntermediate.grid(row=2,column=2,pady=5)
        self.IALevelExpert.grid(row=2,column=3,pady=5)
#        self.firstPlayerLabel.grid(row=3,column=0,pady=5)
#        self.firstPlayerYes.grid(row=3,column=1,pady=5)
#        self.firstPlayerNo.grid(row=3,column=2,pady=5)
        self.play.pack(pady=5)
        self.quit.pack()
        
    def chooseColor(self, color):
        self.playerColor = color
        if color == Color.BLUE:
            self.playerColorButtonBlue.config(relief=RAISED)
            self.playerColorButtonRed.config(relief=FLAT)
            self.playerColorButtonGreen.config(relief=FLAT)
            self.playerColorButtonYellow.config(relief=FLAT)
        elif color == Color.RED:
            self.playerColorButtonBlue.config(relief=FLAT)
            self.playerColorButtonRed.config(relief=RAISED)
            self.playerColorButtonGreen.config(relief=FLAT)
            self.playerColorButtonYellow.config(relief=FLAT)
        elif color == Color.YELLOW:
            self.playerColorButtonBlue.config(relief=FLAT)
            self.playerColorButtonRed.config(relief=FLAT)
            self.playerColorButtonGreen.config(relief=FLAT)
            self.playerColorButtonYellow.config(relief=RAISED)
        elif color == Color.GREEN:
            self.playerColorButtonBlue.config(relief=FLAT)
            self.playerColorButtonRed.config(relief=FLAT)
            self.playerColorButtonGreen.config(relief=RAISED)
            self.playerColorButtonYellow.config(relief=FLAT)
    
    def playGame(self):
        if self.playerColor == Color.BLUE:
            self.IAs.add(IA("Bob", Color.GREEN, self.IALevelValue.get()))
            self.IAs.add(IA("Tim", Color.RED, self.IALevelValue.get()))
            self.IAs.add(IA("Rachid", Color.YELLOW, self.IALevelValue.get()))
        elif self.playerColor == Color.RED:
            self.IAs.add(IA("Bob", Color.GREEN, self.IALevelValue.get()))
            self.IAs.add(IA("Tim", Color.BLUE, self.IALevelValue.get()))
            self.IAs.add(IA("Rachid", Color.YELLOW, self.IALevelValue.get()))
        elif self.playerColor == Color.YELLOW:
            self.IAs.add(IA("Bob", Color.GREEN, self.IALevelValue.get()))
            self.IAs.add(IA("Tim", Color.RED, self.IALevelValue.get()))
            self.IAs.add(IA("Rachid", Color.BLUE, self.IALevelValue.get()))
        elif self.playerColor == Color.GREEN:
            self.IAs.add(IA("Bob", Color.BLUE, self.IALevelValue.get()))
            self.IAs.add(IA("Tim", Color.RED, self.IALevelValue.get()))
            self.IAs.add(IA("Rachid", Color.YELLOW, self.IALevelValue.get()))
            
        self.wantQuit = 0
        self.human = Human(self.playerName.get(), self.playerColor)
        self.fenetre.destroy()
        
        