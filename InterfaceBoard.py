# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 14:33:48 2015

@author: rsalem
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:37:01 2015

@author: rsalem
"""

# On importe Tkinter
from tkinter import *
from PIL import Image, ImageTk


class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=600, height=500, **kwargs)
        
        self.ThurnPlan()
        self.initialize()
        
    def initialize(self):
        pass  
        
    
    def ThurnPlan(self):
        
        #Create a canvas
        canvas = Canvas(fenetre, width=1900, height=1000, bg='beige')
        canvas.pack()
        
        # Load the image file
        thurnplan = Image.open('Z:/ThurnUndTaxis/TUT/images/thurnplan.jpg')
        DeckPlan = Image.open('Z:/ThurnUndTaxis/TUT/images/deck.jpg')
        
        #Bonus Provinces
        bonusschweizplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusschweiz0.png')
        bonuswurttembergplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonuswurttemberg0.png')
        bonusbohmenplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusbohmen0.png')
        bonusbadenplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusbaden0.png')
        bonusbaiernplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusbaiern0.png')
        
        #Bonus End and All provinces
        bonusendplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusend0.png')
        bonusallplan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonusall0.png')
        
        #Bonus road
        bonus5plan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonus5.png')
        bonus6plan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonus6.png')
        bonus7plan = Image.open('Z:/ThurnUndTaxis/TUT/images/bonus7.png')
        
        #Open cards
        Card01plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        Card02plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        Card03plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        Card04plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        Card05plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        Card06plan = Image.open('Z:/ThurnUndTaxis/TUT/images/card12.png')
        
        #Official
        Oficial01 = Image.open('Z:/ThurnUndTaxis/TUT/images/postillion.bmp')
        OficialTile01 = Image.open('Z:/ThurnUndTaxis/TUT/images/postalCarrierTile.png')
        Oficial02 = Image.open('Z:/ThurnUndTaxis/TUT/images/amtmann.bmp')
        OficialTile02 = Image.open('Z:/ThurnUndTaxis/TUT/images/administratorTile.png')
        Oficial03 = Image.open('Z:/ThurnUndTaxis/TUT/images/postmeister.bmp')
        OficialTile03 = Image.open('Z:/ThurnUndTaxis/TUT/images/postmasterTile.png')
        Oficial04 = Image.open('Z:/ThurnUndTaxis/TUT/images/wagner.bmp')
        OficialTile04 = Image.open('Z:/ThurnUndTaxis/TUT/images/cartwrightTile.png')
        
        
        # Put the image into a canvas compatible class, and stick in an
        # arbitrary variable to the garbage collector doesn't destroy it
        canvas.board = ImageTk.PhotoImage(thurnplan)
        canvas.Deck = ImageTk.PhotoImage(DeckPlan)
        
        #Bonus Provinces
        canvas.bonusschweiz = ImageTk.PhotoImage(bonusschweizplan)
        canvas.bonuswurttemberg = ImageTk.PhotoImage(bonuswurttembergplan)
        canvas.bonusbohmenp = ImageTk.PhotoImage(bonusbohmenplan)
        canvas.bonusbaden = ImageTk.PhotoImage(bonusbadenplan)
        canvas.bonusbaiern = ImageTk.PhotoImage(bonusbaiernplan)
        
        #Bonus End and All provinces
        canvas.bonusend = ImageTk.PhotoImage(bonusendplan)
        canvas.bonusall = ImageTk.PhotoImage(bonusallplan)
        
        #Bonus road
        canvas.bonus5 = ImageTk.PhotoImage(bonus5plan)
        canvas.bonus6 = ImageTk.PhotoImage(bonus6plan)
        canvas.bonus7 = ImageTk.PhotoImage(bonus7plan)
        
        #Open cards
        canvas.card01 = ImageTk.PhotoImage(Card01plan)
        canvas.card02 = ImageTk.PhotoImage(Card02plan)
        canvas.card03 = ImageTk.PhotoImage(Card03plan)
        canvas.card04 = ImageTk.PhotoImage(Card04plan)
        canvas.card05 = ImageTk.PhotoImage(Card05plan)
        canvas.card06 = ImageTk.PhotoImage(Card06plan)
        
        #Official
        canvas.postillion = ImageTk.PhotoImage(Oficial01)
        canvas.postillionTile = ImageTk.PhotoImage(OficialTile01)
        canvas.amtmann = ImageTk.PhotoImage(Oficial02)
        canvas.amtmannTile = ImageTk.PhotoImage(OficialTile02)
        canvas.postmeister = ImageTk.PhotoImage(Oficial03)
        canvas.postmeisterTile = ImageTk.PhotoImage(OficialTile03)
        canvas.wagner = ImageTk.PhotoImage(Oficial04)
        canvas.wagnerTile = ImageTk.PhotoImage(OficialTile04)
        
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        
        canvas.create_image(700, 275, image=canvas.board, anchor='nw')
        canvas.create_image(600, 300, image=canvas.Deck, anchor='nw')
        
        #Bonus Provinces
        canvas.create_image(855, 704, image=canvas.bonusschweiz, anchor='nw')
        canvas.create_image(842, 478, image=canvas.bonuswurttemberg, anchor='nw')
        canvas.create_image(1249, 489, image=canvas.bonusbohmenp, anchor='nw')
        canvas.create_image(881, 290, image=canvas.bonusbaden, anchor='nw')
        canvas.create_image(1118, 495, image=canvas.bonusbaiern, anchor='nw')
        
        #Bonus End and All provinces
        canvas.create_image(740, 276, image=canvas.bonusend, anchor='nw')
        canvas.create_image(740, 320, image=canvas.bonusall, anchor='nw')
        
        #Bonus road
        canvas.create_image(695, 275, image=canvas.bonus5, anchor='nw')
        canvas.create_image(695, 320, image=canvas.bonus6, anchor='nw')
        canvas.create_image(695, 364, image=canvas.bonus7, anchor='nw')
        
        #Open cards
        canvas.create_image(575, 450, image=canvas.card01, anchor='nw')
        canvas.create_image(575, 500, image=canvas.card02, anchor='nw')
        canvas.create_image(575, 550, image=canvas.card03, anchor='nw')
        canvas.create_image(575, 600, image=canvas.card04, anchor='nw')
        canvas.create_image(575, 650, image=canvas.card05, anchor='nw')
        canvas.create_image(575, 700, image=canvas.card06, anchor='nw')
        
        #Official
        canvas.create_image(1420, 900, image=canvas.postillion, anchor='nw')
        canvas.create_image(1420, 840, image=canvas.postillionTile , anchor='nw')
        canvas.create_image(1540, 900, image=canvas.amtmann, anchor='nw')
        canvas.create_image(1540, 840, image=canvas.amtmannTile, anchor='nw')
        canvas.create_image(1480, 900, image=canvas.postmeister, anchor='nw')
        canvas.create_image(1480, 840, image=canvas.postmeisterTile, anchor='nw')
        canvas.create_image(1600, 900, image=canvas.wagner, anchor='nw')
        canvas.create_image(1600, 840, image=canvas.wagnerTile, anchor='nw')
        
        #GroupHand = LabelFrame(canvas, text="This is a LabelFrame")
        #GroupHand.place(1600,840)
        
        
        

fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy()