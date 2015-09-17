# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:01:24 2015

@author: pieagbo
"""

from tkinter import *
from Model import *

class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        
        self.choix = "droite"
        self.fenetre = fenetre
        self.wantQuit = 1
        
        self.pack(fill=BOTH)
        
        self.message = Label(self, text="Placer la ville à ")     
                
        self.rigthButton = Button(self, text="Droite", width=10, command=lambda: self.choose("Rigth"))
        self.leftButton = Button(self, text="Gauche", width=10, command=lambda: self.choose("Left"))
        
        
        self.cancel = Button(self, text="Annuler", width=10, command=self.Cancel)

        self.message.grid(row=0,column=1, columnspan=3, pady=5)

        self.rigthButton.grid(row=1,column=1, pady=5)
        self.leftButton.grid(row=1,column=2, pady=5)

        self.cancel.grid(row=2,column=2, pady=5)
        
    def choose(self, choix):
        self.choix = choix
        self.wantQuit = 1
        self.fenetre.destroy()
        print(self.choix)

    
    def Cancel(self):
        self.wantQuit = 0
        self.fenetre.destroy()