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
    
    def __init__(self, fenetre, name, gameBoardWidth, gameBoardHeight, gameBoardImage, backCardImage, provinceBonus, allProvincesBonus, 
                     endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, officials, closeDeck, openDeck, IAs, human, houses, **kwargs):
        Frame.__init__(self, fenetre, width=0, height=0, **kwargs)

        self.name = name
        self.gameBoardWidth = gameBoardWidth
        self.gameBoardHeight = gameBoardHeight
        self.gameBoardImage = gameBoardImage
        self.backCardImage = backCardImage

        self.officials = officials
        
        self.provinceBonus = provinceBonus
        self.allProvincesBonus = allProvincesBonus
        self.endGameBonus = endGameBonus
        self.longRouteBonus7 = longRouteBonus7
        self.longRouteBonus6 = longRouteBonus6
        self.longRouteBonus5 = longRouteBonus5
        
        self.closeDeck = closeDeck        
        self.openDeck = openDeck
        
        self.IAs = IAs
        
        self.human = human
        
        self.houses = houses
        
        #Create a canvas
        canvas = Canvas(fenetre, width=1900, height=1000)
        canvas.pack()
    
#        background = Image.open('utils/images/bg.jpg')
#        canvas.backg = ImageTk.PhotoImage(background)
#        canvas.create_image(0, 0, image=canvas.backg, anchor='nw')
    
        # Load the image file
        thurnplan = Image.open(self.gameBoardImage)
        DeckPlan = Image.open(self.backCardImage)
        
        #Bonus Provinces
        for bonus in self.provinceBonus:
            if 'baiern' in bonus.image:
                bonusbaiernplan = Image.open('utils/images/' + bonus.image)
            elif 'wurttemberg' in bonus.image:
                bonuswurttembergplan = Image.open('utils/images/' + bonus.image)
            elif 'baden' in bonus.image:
                bonusbadenplan = Image.open('utils/images/' + bonus.image)
            elif 'bohmen' in bonus.image:
                bonusbohmenplan = Image.open('utils/images/' + bonus.image)
            elif 'schweiz' in bonus.image:
                bonusschweizplan = Image.open('utils/images/' + bonus.image)
        
        #Bonus End and All provinces
        bonusendplan = Image.open('utils/images/' + self.endGameBonus.image)
        bonusallplan = Image.open('utils/images/' + self.allProvincesBonus.image)
        
        #Bonus road
        bonus5plan = Image.open('utils/images/' + self.longRouteBonus5.image)
        bonus6plan = Image.open('utils/images/' + self.longRouteBonus6.image)
        bonus7plan = Image.open('utils/images/' + self.longRouteBonus7.image)
        
        #Open cards
        Card01plan = Image.open('utils/images/' + self.openDeck[0].city.image)
        Card02plan = Image.open('utils/images/' + self.openDeck[1].city.image)
        Card03plan = Image.open('utils/images/' + self.openDeck[2].city.image)
        Card04plan = Image.open('utils/images/' + self.openDeck[3].city.image)
        Card05plan = Image.open('utils/images/' + self.openDeck[4].city.image)
        Card06plan = Image.open('utils/images/' + self.openDeck[5].city.image)
        
        #Official
        for official in officials:
            if 'postillion' in official.personImage:
                Oficial01 = Image.open('utils/images/' + official.personImage)
                OficialTile01 = Image.open('utils/images/' + official.symbolImage)
            elif 'amtmann' in official.personImage:
                Oficial02 = Image.open('utils/images/' + official.personImage)
                OficialTile02 = Image.open('utils/images/' + official.symbolImage)
            elif 'postmeister' in official.personImage:
                Oficial03 = Image.open('utils/images/' + official.personImage)
                OficialTile03 = Image.open('utils/images/' + official.symbolImage)
            elif 'wagner' in official.personImage:
                Oficial04 = Image.open('utils/images/' + official.personImage)
                OficialTile04 = Image.open('utils/images/' + official.symbolImage)
        

        hand = Image.open('utils/images/hand.png')
        house = Image.open('utils/images/house.png')
        wheel = Image.open('utils/images/wheel.png')
        playerbonus = Image.open('utils/images/playerbonus.png')

        
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
    
        canvas.hand = ImageTk.PhotoImage(hand)
        canvas.house = ImageTk.PhotoImage(house)
        canvas.wheel = ImageTk.PhotoImage(wheel) 
        canvas.playerbonus = ImageTk.PhotoImage(playerbonus) 
        
        # Add the image to the canvas, and set the anchor to the top left / north west corner
        
        canvas.config(bg="light goldenrod")
        
        canvasBlue = canvas.create_rectangle(635, 5, 950, 220, fill = "blue")
        canvasRed = canvas.create_rectangle(635, 225, 950, 430, fill = "red")
        canvasGreen = canvas.create_rectangle(955, 225, 1270, 430, fill = "green")
        canvasYellow = canvas.create_rectangle(955, 5, 1270, 220, fill = "yellow")
        
        canvas.create_image(0, 0, image=canvas.board, anchor='nw')
        canvas.create_image(1140, 440, image=canvas.Deck, anchor='nw', tag="CloseDeck")
        canvas.create_text(1160, 500, text=len(self.closeDeck), fill="white", anchor='nw', font="Helvetica 16")
        canvas.tag_bind("CloseDeck", "<Button-1>", self.ClickCloseDeck)
        
        #Bonus Provinces
        canvas.create_image(155, 428, image=canvas.bonusschweiz, anchor='nw')
        canvas.create_image(142, 203, image=canvas.bonuswurttemberg, anchor='nw')
        canvas.create_image(549, 215, image=canvas.bonusbohmenp, anchor='nw')
        canvas.create_image(181, 16, image=canvas.bonusbaden, anchor='nw')
        canvas.create_image(418, 220, image=canvas.bonusbaiern, anchor='nw')
        
        #Bonus End and All provinces
        canvas.create_image(780, 540, image=canvas.bonusend, anchor='nw')
        canvas.create_image(830, 540, image=canvas.bonusall, anchor='nw')
        
        #Bonus road
        canvas.create_image(880, 540, image=canvas.bonus5, anchor='nw')
        canvas.create_image(930, 540, image=canvas.bonus6, anchor='nw')
        canvas.create_image(980, 540, image=canvas.bonus7, anchor='nw')
        
        #Open cards
        canvas.create_image(735, 440, image=canvas.card01, anchor='nw', tag="OpenDeck")
        canvas.create_image(857, 440, image=canvas.card02, anchor='nw', tag="OpenDeck")
        canvas.create_image(978, 440, image=canvas.card03, anchor='nw', tag="OpenDeck")
        canvas.create_image(735, 480, image=canvas.card04, anchor='nw', tag="OpenDeck")
        canvas.create_image(857, 480, image=canvas.card05, anchor='nw', tag="OpenDeck")
        canvas.create_image(975, 480, image=canvas.card06, anchor='nw', tag="OpenDeck")
        canvas.tag_bind("OpenDeck", "<Button-1>", self.ClickOpenDeck)
        
        #Official
#        canvas.create_image(640, 440, image=canvas.postillion, anchor='nw')
        canvas.create_image(635, 440, image=canvas.postillionTile , anchor='nw', tag="postillionTile")
        canvas.tag_bind("postillionTile", "<Button-1>", self.ClickPostillionTile)
        
#        canvas.create_image(690, 440, image=canvas.amtmann, anchor='nw')
        canvas.create_image(635, 485, image=canvas.amtmannTile, anchor='nw', tag="amtmannTile")
        canvas.tag_bind("amtmannTile", "<Button-1>", self.ClickAmtmannTile)
        
#        canvas.create_image(640, 900, image=canvas.postmeister, anchor='nw')
        canvas.create_image(680, 440, image=canvas.postmeisterTile, anchor='nw', tag="postmeisterTile")
        canvas.tag_bind("postmeisterTile", "<Button-1>", self.ClickPostmeisterTile)
        
#        canvas.create_image(690, 900, image=canvas.wagner, anchor='nw')
        canvas.create_image(680, 485, image=canvas.wagnerTile, anchor='nw', tag="wagnerTile")
        canvas.tag_bind("wagnerTile", "<Button-1>", self.ClickWagnerTile)
        
        canvas.create_image(640, 40, image=canvas.hand, anchor='nw')
        canvas.create_image(640, 85, image=canvas.house, anchor='nw')
        canvas.create_image(640, 130, image=canvas.wheel, anchor='nw')
        canvas.create_image(640, 175, image=canvas.playerbonus, anchor='nw')
        canvas.create_text(700, 15, text="Player 1", anchor='nw', font="Helvetica 16")
        
        canvas.create_image(640, 250, image=canvas.hand, anchor='nw')
        canvas.create_image(640, 295, image=canvas.house, anchor='nw')
        canvas.create_image(640, 340, image=canvas.wheel, anchor='nw')
        canvas.create_image(640, 385, image=canvas.playerbonus, anchor='nw')
        canvas.create_text(700, 225, text="Player 2", anchor='nw', font="Helvetica 16")
        
        canvas.create_image(960, 40, image=canvas.hand, anchor='nw')
        canvas.create_image(960, 85, image=canvas.house, anchor='nw')
        canvas.create_image(960, 130, image=canvas.wheel, anchor='nw')
        canvas.create_image(960, 175, image=canvas.playerbonus, anchor='nw')
        canvas.create_text(1020, 15, text="Player 3", anchor='nw', font="Helvetica 16")
        
        canvas.create_image(960, 250, image=canvas.hand, anchor='nw')
        canvas.create_image(960, 295, image=canvas.house, anchor='nw')
        canvas.create_image(960, 340, image=canvas.wheel, anchor='nw')
        canvas.create_image(960, 385, image=canvas.playerbonus, anchor='nw')
        canvas.create_text(1020, 225, text="Player 4", anchor='nw', font="Helvetica 16")

        
#        #Cards Human Player
#        HandCardsPH = LabelFrame(canvas, text="Hand cards", labelanchor="n", width=770, height=90)
#        HandCardsPH.pack();
#        HandCardsPH.place(x = 605, y = 883);
#        RoadCardsPH = LabelFrame(canvas, text="Road", labelanchor="n", width=900, height=90)
#        RoadCardsPH.pack();
#        RoadCardsPH.place(x = 550, y = 750);
#        
#        #Cards IA Player
#        HandCardsIA1 = LabelFrame(canvas, text="Hand cards", labelanchor="n", width=90, height=500)
#        HandCardsIA1.pack();
#        HandCardsIA1.place(x = 50, y = 250);
#        RoadCardsIA1 = LabelFrame(canvas, text="Road", labelanchor="n", width=90, height=770)
#        RoadCardsIA1.pack();
#        RoadCardsIA1.place(x = 200, y = 100);        
#        
#        HandCardsIA2 = LabelFrame(canvas, text="Hand cards", labelanchor="n", width=770, height=90)
#        HandCardsIA2.pack();
#        HandCardsIA2.place(x = 605, y = 25);
#        RoadCardsIA2 = LabelFrame(canvas, text="Road", labelanchor="n", width=900, height=90)
#        RoadCardsIA2.pack();
#        RoadCardsIA2.place(x = 550, y = 150);
#        
#        HandCardsIA3 = LabelFrame(canvas, text="Hand cards", labelanchor="n", width=90, height=500)
#        HandCardsIA3.pack();
#        HandCardsIA3.place(x = 1770, y = 250);
#        RoadCardsIA3 = LabelFrame(canvas, text="Road", labelanchor="n", width=90, height=770)
#        RoadCardsIA3.pack();
#        RoadCardsIA3.place(x = 1620, y = 100);
        

        
    def ClickCloseDeck(self, event):
         print("Close Deck")
         
    def ClickOpenDeck(self, event):
        print("Open Deck")

    def ClickPostillionTile(self, event):
        print("Official Postillon")
        
    def ClickAmtmannTile(self, event ):
        print("Official Amtman")
        
    def ClickPostmeisterTile(self, event):
        print("Official Postmeister")
        
    def ClickWagnerTile(self, event):
        print("Official Wagner")
