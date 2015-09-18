# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:01:24 2015

@author: pieagbo
"""

from tkinter import *
from Model import *

class Interface():
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, parent):
         
        top = self.top = Toplevel(parent)
        
        self.choix = "droite"
        self.wantQuit = 1
        
        
        self.message = Label(top, text="Placer la ville à ")     
                
        self.rigthButton = Button(top, text="Droite", width=10, command=lambda: self.choose("Rigth"))
        self.leftButton = Button(top, text="Gauche", width=10, command=lambda: self.choose("Left"))
        
        
        self.cancel = Button(top, text="Annuler", width=10, command=self.Cancel)

        self.message.grid(row=0,column=1, columnspan=3, pady=5)

        self.rigthButton.grid(row=1,column=2, pady=5)
        self.leftButton.grid(row=1,column=1, pady=5)

        self.cancel.grid(row=2,column=2, pady=5)
        
    def choose(self, choix):
        self.choix = choix
        self.wantQuit = 1
        self.top.destroy()

    
    def Cancel(self):
        self.wantQuit = 0
        self.top.destroy()
        