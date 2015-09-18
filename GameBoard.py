# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:37:01 2015

@author: rsalem
"""

# On importe Tkinter
from tkinter import *
from PIL import Image, ImageTk
from Model import *
from random import *
import MessageBox 



class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, name, gameBoardImage, backCardImage, provinceBonus, allProvincesBonus, 
                     endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, officials, carriage, closeDeck, openDeck, IAone, IAthree, IAfour, human, houses, **kwargs):
        Frame.__init__(self, fenetre, width=0, height=0, **kwargs)


        self.fenetre = fenetre 
        
        self.name = name
        self.gameBoardImage = gameBoardImage
        self.backCardImage = backCardImage

        self.officials = officials
        
        self.carriage = carriage

        self.provinceBonus = provinceBonus
        self.allProvincesBonus = allProvincesBonus
        self.endGameBonus = endGameBonus
        self.longRouteBonus7 = longRouteBonus7
        self.longRouteBonus6 = longRouteBonus6
        self.longRouteBonus5 = longRouteBonus5
        
        self.closeDeck = closeDeck        
        self.openDeck = openDeck
        self.binDeck = list()
        
        self.playerRoadCount = 0 
        
        self.IAone= IAone
        self.IAthree= IAthree
        self.IAfour= IAfour
        self.human = human
        
        self.houses = houses
    
        self.official = None        
        
        self.messageBox = None
        
        #Create a self.canvas
        self.canvas = Canvas(fenetre, width=1273, height=800)
        self.canvas.pack()
        
        self.initializeImage()
        self.initializeText()
        
        self.play(EVENT.BEGIN_TURN)
        
    
    def initializeImage(self):
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
        for official in self.officials:
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
        player1bonus = Image.open('utils/images/playerbonus.png')
        player2bonus = Image.open('utils/images/playerbonus.png')
        player3bonus = Image.open('utils/images/playerbonus.png')
        player4bonus = Image.open('utils/images/playerbonus.png')
        
        #Hand
        handplayer = list()
        for card in self.human.hand:
            handplayer.append(Image.open('utils/images/' + card.city.image))

        #Road
        roadplayerHuman = list()
        for card in self.human.road:
            roadplayerHuman.append(Image.open('utils/images/' + card.city.image))
        
        # Put the image into a self.canvas compatible class, and stick in an
        # arbitrary variable to the garbage collector doesn't destroy it
        self.canvas.board = ImageTk.PhotoImage(thurnplan)
        self.canvas.Deck = ImageTk.PhotoImage(DeckPlan)
        
        #Bonus Provinces
        self.canvas.bonusschweiz = ImageTk.PhotoImage(bonusschweizplan)
        self.canvas.bonuswurttemberg = ImageTk.PhotoImage(bonuswurttembergplan)
        self.canvas.bonusbohmenp = ImageTk.PhotoImage(bonusbohmenplan)
        self.canvas.bonusbaden = ImageTk.PhotoImage(bonusbadenplan)
        self.canvas.bonusbaiern = ImageTk.PhotoImage(bonusbaiernplan)
        
        #Bonus End and All provinces
        self.canvas.bonusend = ImageTk.PhotoImage(bonusendplan)
        self.canvas.bonusall = ImageTk.PhotoImage(bonusallplan)
        
        #Bonus road
        self.canvas.bonus5 = ImageTk.PhotoImage(bonus5plan)
        self.canvas.bonus6 = ImageTk.PhotoImage(bonus6plan)
        self.canvas.bonus7 = ImageTk.PhotoImage(bonus7plan)
        
        #Open cards
        self.canvas.card01 = ImageTk.PhotoImage(Card01plan)
        self.canvas.card02 = ImageTk.PhotoImage(Card02plan)
        self.canvas.card03 = ImageTk.PhotoImage(Card03plan)
        self.canvas.card04 = ImageTk.PhotoImage(Card04plan)
        self.canvas.card05 = ImageTk.PhotoImage(Card05plan)
        self.canvas.card06 = ImageTk.PhotoImage(Card06plan)
        
        #Official
        self.canvas.postillion = ImageTk.PhotoImage(Oficial01)
        self.canvas.postillionTile = ImageTk.PhotoImage(OficialTile01)
        self.canvas.amtmann = ImageTk.PhotoImage(Oficial02)
        self.canvas.amtmannTile = ImageTk.PhotoImage(OficialTile02)
        self.canvas.postmeister = ImageTk.PhotoImage(Oficial03)
        self.canvas.postmeisterTile = ImageTk.PhotoImage(OficialTile03)
        self.canvas.wagner = ImageTk.PhotoImage(Oficial04)
        self.canvas.wagnerTile = ImageTk.PhotoImage(OficialTile04)
    
        self.canvas.hand = ImageTk.PhotoImage(hand)
        self.canvas.house = ImageTk.PhotoImage(house)
        self.canvas.wheel = ImageTk.PhotoImage(wheel) 

        self.canvas.player1bonus = ImageTk.PhotoImage(player1bonus) 
        self.canvas.player2bonus = ImageTk.PhotoImage(player2bonus) 
        self.canvas.player3bonus = ImageTk.PhotoImage(player3bonus) 
        self.canvas.player4bonus = ImageTk.PhotoImage(player4bonus) 
        
        self.canvas.handplayer = list()
        for card in handplayer:
            self.canvas.handplayer.append(ImageTk.PhotoImage(card))

        self.canvas.roadplayerHuman = list()
        for card in roadplayerHuman:
            self.canvas.roadplayerHuman.append(ImageTk.PhotoImage(card))

        
        # Add the image to the self.canvas, and set the anchor to the top left / north west corner
        self.canvas.config(bg="light goldenrod")
        
        canvasBlue = self.canvas.create_rectangle(635, 5, 950, 220, fill = self.IAone.color.name)
        canvasYellow = self.canvas.create_rectangle(955, 5, 1270, 220, fill = self.human.color.name)
        canvasRed = self.canvas.create_rectangle(635, 225, 950, 430, fill = self.IAthree.color.name)
        canvasGreen = self.canvas.create_rectangle(955, 225, 1270, 430, fill = self.IAfour.color.name)
    
        
        self.canvas.create_image(0, 0, image=self.canvas.board, anchor='nw')
        self.closeDeckButton = Button(self.canvas, text=len(self.closeDeck), image=self.canvas.Deck, command=self.ClickCloseDeck, compound="center", font="Helvetica 20", fg="white")
        self.closeDeckButton.place(x = 1140, y = 440, anchor='nw')
        
        
        #Bonus Provinces
        self.bonusSchweiz = self.canvas.create_image(155, 428, image=self.canvas.bonusschweiz, anchor='nw')
        self.bonusWurttemberg = self.canvas.create_image(142, 203, image=self.canvas.bonuswurttemberg, anchor='nw')
        self.bonusBohmenp = self.canvas.create_image(549, 215, image=self.canvas.bonusbohmenp, anchor='nw')
        self.bonusBaden = self.canvas.create_image(181, 16, image=self.canvas.bonusbaden, anchor='nw')
        self.bonusBaiern = self.canvas.create_image(418, 220, image=self.canvas.bonusbaiern, anchor='nw')
        
        #Bonus End and All provinces
        self.bonusEnd = self.canvas.create_image(780, 540, image=self.canvas.bonusend, anchor='nw')
        self.bonusAll = self.canvas.create_image(830, 540, image=self.canvas.bonusall, anchor='nw')
        
        #Bonus road
        self.bonus5 = self.canvas.create_image(880, 540, image=self.canvas.bonus5, anchor='nw')
        self.bonus6 = self.canvas.create_image(930, 540, image=self.canvas.bonus6, anchor='nw')
        self.bonus7 = self.canvas.create_image(980, 540, image=self.canvas.bonus7, anchor='nw')
        
        #Open cards
        self.card01 = Button(self.canvas, image=self.canvas.card01, command=lambda arg=0: self.ClickOpenDeck(arg))
        self.card01.place(x = 735, y = 440, anchor='nw')
        
        self.card02 = Button(self.canvas, image=self.canvas.card02, command=lambda arg=1: self.ClickOpenDeck(arg))
        self.card02.place(x = 857, y = 440, anchor='nw')
        
        self.card03 = Button(self.canvas, image=self.canvas.card03, command=lambda arg=2: self.ClickOpenDeck(arg))
        self.card03.place(x = 978, y = 440, anchor='nw')
        
        self.card04 = Button(self.canvas, image=self.canvas.card04, command=lambda arg=3: self.ClickOpenDeck(arg))
        self.card04.place(x = 735, y = 485, anchor='nw')
        
        self.card05 = Button(self.canvas, image=self.canvas.card05, command=lambda arg=4: self.ClickOpenDeck(arg))
        self.card05.place(x = 857, y = 485, anchor='nw')
        
        self.card06 = Button(self.canvas, image=self.canvas.card06, command=lambda arg=5: self.ClickOpenDeck(arg))
        self.card06.place(x = 978, y = 485, anchor='nw')
        
        self.closeRoad = Button(self.canvas, text="Discard road", command=lambda arg=self.human: self.discardRoad(arg))
        self.closeRoad.place(x = 1140, y = 540, anchor='nw')
        self.closeRoad.config(state=DISABLED)

        self.endTurn = Button(self.canvas, text="Finish turn ! ", command=self.playFinish)
        self.endTurn.place(x = 1140, y = 570, anchor='nw')
        self.endTurn.config(state=DISABLED)
        
        #Official
        self.postillionTile = Button(self.canvas, image=self.canvas.postillionTile, command=self.ClickPostillionTile)
        self.postillionTile.place(x = 635, y = 440, anchor='nw')
        self.postillionTile.config(state=DISABLED)
        
        self.amtmannTile = Button(self.canvas, image=self.canvas.amtmannTile, command=self.ClickAmtmannTile)
        self.amtmannTile.place(x = 635, y = 485, anchor='nw')
        self.amtmannTile.config(state=DISABLED)
        
        self.postmeisterTile = Button(self.canvas, image=self.canvas.postmeisterTile, command=self.ClickPostmeisterTile)
        self.postmeisterTile.place(x = 680, y = 440, anchor='nw')
        self.postmeisterTile.config(state=DISABLED)
        
        self.wagnerTile = Button(self.canvas, image=self.canvas.wagnerTile, command=self.ClickWagnerTile)
        self.wagnerTile.place(x = 680, y = 485, anchor='nw')
        self.wagnerTile.config(state=DISABLED)

        
        self.canvas.create_image(640, 40, image=self.canvas.hand, anchor='nw')
        self.canvas.create_image(640, 85, image=self.canvas.house, anchor='nw')
        self.canvas.create_image(640, 130, image=self.canvas.wheel, anchor='nw')
        self.player1bonus = self.canvas.create_image(640, 175, image=self.canvas.player1bonus, anchor='nw')

        
        self.canvas.create_image(640, 250, image=self.canvas.hand, anchor='nw')
        self.canvas.create_image(640, 295, image=self.canvas.house, anchor='nw')
        self.canvas.create_image(640, 340, image=self.canvas.wheel, anchor='nw')
        self.player3bonus = self.canvas.create_image(640, 385, image=self.canvas.player3bonus, anchor='nw')
        
        
        self.canvas.create_image(960, 40, image=self.canvas.hand, anchor='nw')
        self.canvas.create_image(960, 85, image=self.canvas.house, anchor='nw')
        self.canvas.create_image(960, 130, image=self.canvas.wheel, anchor='nw')
        self.player2bonus = self.canvas.create_image(960, 175, image=self.canvas.player2bonus, anchor='nw')
        
        
        self.canvas.create_image(960, 250, image=self.canvas.hand, anchor='nw')
        self.canvas.create_image(960, 295, image=self.canvas.house, anchor='nw')
        self.canvas.create_image(960, 340, image=self.canvas.wheel, anchor='nw')
        self.player4bonus = self.canvas.create_image(960, 385, image=self.canvas.player4bonus, anchor='nw')
        
        self.handPlayer = list()

        self.roadPlayerHuman = list()

    
    def initializeText(self):
#        self.nbCardsCloseDeck = self.closeDeck.create_text(1160, 500, text=len(self.closeDeck), fill="white", anchor='nw', font="Helvetica 16")
        
        self.canvas.create_text(700, 15, text=self.IAone.name, anchor='nw', font="Helvetica 16")
        self.IAoneHand = self.canvas.create_text(652, 55, text=len(self.IAone.hand), anchor='nw', font="Helvetica 14", fill="white")
        self.IAoneHouses = self.canvas.create_text(649, 97, text=len(self.IAone.houses), anchor='nw', font="Helvetica 14", fill="white")
        if self.IAone.carriage != None : 
            self.IAoneCarriages = self.canvas.create_text(654.25, 139, text=self.IAone.carriage.routeLength, anchor='nw', font="Helvetica 14", fill="black")
        else:
            self.IAoneCarriages = self.canvas.create_text(654.25, 139, text="0", anchor='nw', font="Helvetica 14", fill="black")
        
        self.canvas.create_text(700, 225, text=self.IAthree.name, anchor='nw', font="Helvetica 16")
        self.IAthreeHand = self.canvas.create_text(652, 265, text=len(self.IAthree.hand), anchor='nw', font="Helvetica 14", fill="white")
        self.IAthreeHouses = self.canvas.create_text(649, 307, text=len(self.IAthree.houses), anchor='nw', font="Helvetica 14", fill="white")
        if self.IAone.carriage != None : 
            self.IAthreeCarriages = self.canvas.create_text(654.25, 350, text=self.IAthree.carriage.routeLength, anchor='nw', font="Helvetica 14", fill="black")
        else:
            self.IAthreeCarriages = self.canvas.create_text(654.25, 350, text="0", anchor='nw', font="Helvetica 14", fill="black")
        
        self.canvas.create_text(1020, 15, text=self.human.name, anchor='nw', font="Helvetica 16")
        self.humanHand = self.canvas.create_text(972, 55, text=len(self.human.hand), anchor='nw', font="Helvetica 14", fill="white")
        self.humanHouses = self.canvas.create_text(969, 97, text=len(self.human.houses), anchor='nw', font="Helvetica 14", fill="white")
        if self.IAone.carriage != None : 
            self.humanCarriages = self.canvas.create_text(975, 139, text=self.human.carriage.routeLength, anchor='nw', font="Helvetica 14", fill="black")
        else:
            self.humanCarriages = self.canvas.create_text(975, 139, text="0", anchor='nw', font="Helvetica 14", fill="black")
        
        self.canvas.create_text(1020, 225, text=self.IAfour.name , anchor='nw', font="Helvetica 16")
        self.IAfourHand = self.canvas.create_text(972, 265, text=len(self.IAfour.hand), anchor='nw', font="Helvetica 14", fill="white")
        self.IAfourHouses = self.canvas.create_text(969, 307, text=len(self.IAfour.houses), anchor='nw', font="Helvetica 14", fill="white")
        if self.IAone.carriage != None : 
            self.IAfourCarriages = self.canvas.create_text(975, 350, text=self.IAfour.carriage.routeLength, anchor='nw', font="Helvetica 14", fill="black")
        else:
            self.IAfourCarriages = self.canvas.create_text(975, 350, text="0", anchor='nw', font="Helvetica 14", fill="black")
 

    def update(self): 
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
        
        if not self.IAone.bonuses.count:
            player1bonus = Image.open('utils/images/' + self.IAone.bonuses[-1].image)
        else:
            player1bonus = Image.open('utils/images/playerbonus.png')

        if not self.human.bonuses.count:
            player2bonus = Image.open('utils/images/' + self.human.bonuses[-1].image)
        else:
            player2bonus = Image.open('utils/images/playerbonus.png')

        if not self.IAthree.bonuses.count:
            player3bonus = Image.open('utils/images/' + self.IAthree.bonuses[-1].image)
        else:
            player3bonus = Image.open('utils/images/playerbonus.png')

        if not self.IAfour.bonuses.count:
            player4bonus = Image.open('utils/images/' + self.IAfour.bonuses[-1].image)
        else:
            player4bonus = Image.open('utils/images/playerbonus.png')
            

        #Hand
        handplayer = list()
        for card in self.human.hand: 
            handplayer.append(Image.open('utils/images/' + card.city.image))
            
        #Roads
        roadplayerHuman = list()
        for card in self.human.road:
            roadplayerHuman.append(Image.open('utils/images/' + card.city.image))

            
        #Bonus Provinces
        self.canvas.bonusschweiz = ImageTk.PhotoImage(bonusschweizplan)
        self.canvas.bonuswurttemberg = ImageTk.PhotoImage(bonuswurttembergplan)
        self.canvas.bonusbohmenp = ImageTk.PhotoImage(bonusbohmenplan)
        self.canvas.bonusbaden = ImageTk.PhotoImage(bonusbadenplan)
        self.canvas.bonusbaiern = ImageTk.PhotoImage(bonusbaiernplan)
        
        #Bonus End and All provinces
        self.canvas.bonusend = ImageTk.PhotoImage(bonusendplan)
        self.canvas.bonusall = ImageTk.PhotoImage(bonusallplan)
        
        #Bonus road
        self.canvas.bonus5 = ImageTk.PhotoImage(bonus5plan)
        self.canvas.bonus6 = ImageTk.PhotoImage(bonus6plan)
        self.canvas.bonus7 = ImageTk.PhotoImage(bonus7plan)
        
        #Open cards
        self.canvas.card01 = ImageTk.PhotoImage(Card01plan)
        self.canvas.card02 = ImageTk.PhotoImage(Card02plan)
        self.canvas.card03 = ImageTk.PhotoImage(Card03plan)
        self.canvas.card04 = ImageTk.PhotoImage(Card04plan)
        self.canvas.card05 = ImageTk.PhotoImage(Card05plan)
        self.canvas.card06 = ImageTk.PhotoImage(Card06plan)
        
        self.canvas.player1bonus = ImageTk.PhotoImage(player1bonus) 
        self.canvas.player2bonus = ImageTk.PhotoImage(player2bonus) 
        self.canvas.player3bonus = ImageTk.PhotoImage(player3bonus) 
        self.canvas.player4bonus = ImageTk.PhotoImage(player4bonus) 
        
        self.canvas.handplayer = list()
        for card in handplayer:
            self.canvas.handplayer.append(ImageTk.PhotoImage(card))
        
        self.canvas.roadPlayerHuman = list()
        for card in roadplayerHuman:
            self.canvas.roadPlayerHuman.append(ImageTk.PhotoImage(card))
        
        #Bonus Provinces
        self.canvas.itemconfig(self.bonusSchweiz, image=self.canvas.bonusschweiz)
        self.canvas.itemconfig(self.bonusWurttemberg, image=self.canvas.bonuswurttemberg)
        self.canvas.itemconfig(self.bonusBohmenp, image=self.canvas.bonusbohmenp)
        self.canvas.itemconfig(self.bonusBaden, image=self.canvas.bonusbaden)
        self.canvas.itemconfig(self.bonusBaiern, image=self.canvas.bonusbaiern)
        
        self.canvas.itemconfig(self.bonusEnd, image=self.canvas.bonusend)
        self.canvas.itemconfig(self.bonusAll, image=self.canvas.bonusall)
        
        self.canvas.itemconfig(self.bonus5, image=self.canvas.bonus5)
        self.canvas.itemconfig(self.bonus6, image=self.canvas.bonus6)
        self.canvas.itemconfig(self.bonus7, image=self.canvas.bonus7) 
        
        #Open cards
        self.card01.config(image=self.canvas.card01)
        self.card02.config(image=self.canvas.card02)
        self.card03.config(image=self.canvas.card03)
        self.card04.config(image=self.canvas.card04)
        self.card05.config(image=self.canvas.card05)
        self.card06.config(image=self.canvas.card06)

        self.closeDeckButton.config(text =len(self.closeDeck))
        
        self.canvas.itemconfig(self.IAoneHand, text=len(self.IAone.hand))
        self.canvas.itemconfig(self.IAoneHouses, text=len(self.IAone.houses))
        if self.IAone.carriage != None : 
            self.canvas.itemconfig(self.IAoneCarriages, text=self.IAone.carriage.routeLength)
        
        self.canvas.itemconfig(self.IAthreeHand, text=len(self.IAthree.hand))
        self.canvas.itemconfig(self.IAthreeHouses, text=len(self.IAthree.houses))
        if self.IAthree.carriage != None : 
            self.canvas.itemconfig(self.IAthreeCarriages, text=self.IAthree.carriage.routeLength)      
        
        self.canvas.itemconfig(self.humanHand, text=len(self.human.hand))
        self.canvas.itemconfig(self.humanHouses, text=len(self.human.houses))
        if self.human.carriage != None : 
            self.canvas.itemconfig(self.humanCarriages, text=self.human.carriage.routeLength) 
        
        
        self.canvas.itemconfig(self.IAfourHand, text=len(self.IAfour.hand))
        self.canvas.itemconfig(self.IAfourHouses, text=len(self.IAfour.houses))
        if self.IAfour.carriage != None : 
            self.canvas.itemconfig(self.IAfourCarriages, text=self.IAfour.carriage.routeLength)

        self.canvas.itemconfig(self.player1bonus, image=self.canvas.player1bonus, anchor='nw')
        self.canvas.itemconfig(self.player2bonus, image=self.canvas.player2bonus, anchor='nw')
        self.canvas.itemconfig(self.player3bonus, image=self.canvas.player3bonus, anchor='nw')
        self.canvas.itemconfig(self.player4bonus, image=self.canvas.player4bonus, anchor='nw')
        
        self.x = 0
        self.y = 750 
        i = 0
        self.handPlayer.clear()
        for img in self.canvas.handplayer:
            button = Button(self.canvas, image=img, command=lambda arg=i: self.putACard(self.human, arg))
            button.place(x = self.x, y = self.y,anchor="nw")
            button.config(state=DISABLED)
            self.handPlayer.append(button)
            self.x += 125
            i+=1
            
        self.x = 0 
        self.y = 650
        for card in self.canvas.roadPlayerHuman:
            button = Button(self.canvas, image=card)
            button.place(x = self.x, y = self.y,anchor="nw")
            self.roadPlayerHuman.append(button)
            self.x += 125   


    def play(self, event):
        self.event = event
        if self.event == EVENT.BEGIN_TURN:
            if len(self.human.hand) == 0 :
                self.play(EVENT.NO_CARDS_IN_HAND)

            if self.human

            self.card01.config(state=NORMAL)
            self.card02.config(state=NORMAL)
            self.card03.config(state=NORMAL)
            self.card04.config(state=NORMAL)
            self.card05.config(state=NORMAL)
            self.card06.config(state=NORMAL)
            self.closeDeckButton.config(state=NORMAL)
        elif self.event == EVENT.NO_CARDS_IN_HAND:
            self.card01.config(state=NORMAL)
            self.card02.config(state=NORMAL)
            self.card03.config(state=NORMAL)
            self.card04.config(state=NORMAL)
            self.card05.config(state=NORMAL)
            self.card06.config(state=NORMAL)
            self.closeDeckButton.config(state=NORMAL)
        elif self.event == EVENT.TURN:
            self.card01.config(state=NORMAL)
            self.card02.config(state=NORMAL)
            self.card03.config(state=NORMAL)
            self.card04.config(state=NORMAL)
            self.card05.config(state=NORMAL)
            self.card06.config(state=NORMAL)
            self.closeDeckButton.config(state=NORMAL)
            
    
    def takeACard(self, player, inOpen):
        if inOpen != -1:
            card = self.openDeck.pop(inOpen)
            player.hand.append(card)
            if len(self.closeDeck) == 0 :
                shuffle(self.binDeck)
                i = 0
                while i < len(self.binDeck):
                    card = self.binDeck.pop
                    self.closeDeck.add(card)
                card = self.closeDeck.pop()
                self.openDeck.insert(inOpen,card)
            else:
                card = self.closeDeck.pop()
                self.openDeck.insert(inOpen,card)
        else:
            if len(self.closeDeck) == 0 :
                shuffle(self.binDeck)
                i = len(self.binDeck) - 1
                j = 0 
                while i >= j:
                    card = self.binDeck.pop(i)
                    self.closeDeck.append(card)
                    i-=1 
                card = self.closeDeck.pop()
                player.hand.append(card)
            else:
                card = self.closeDeck.pop()
                player.hand.append(card)

        self.card01.config(state=DISABLED)
        self.card02.config(state=DISABLED)
        self.card03.config(state=DISABLED)
        self.card04.config(state=DISABLED)
        self.card05.config(state=DISABLED)
        self.card06.config(state=DISABLED)
        self.closeDeckButton.config(state=DISABLED) 
        self.endTurn.config(state=DISABLED)

        if self.event == EVENT.NO_CARDS_IN_HAND:
            self.postmeisterTile.config(state=NORMAL)
            self.event = EVENT.TURN
        elif self.event == EVENT.TURN:
            self.event = EVENT.END_TURN

        self.update()

        for button in self.handPlayer:
            button.config(state=NORMAL)
                
                
    def discardRoad(self, player):    
        if(len(player.road)) >= 7 and player.carriage != None and player.carriage.routeLength == 6:
            player.carriage = player.carriage.greaterCarriage
            i = len(player.road) - 1 
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card)    
                i-=1
        elif(len(player.road)) >= 6 and player.carriage != None and player.carriage.routeLength == 5:
            player.carriage = player.carriage.greaterCarriage
            i= len(player.road) - 1 
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card)    
                i-=1
        elif(len(player.road)) >= 5 and player.carriage != None and player.carriage.routeLength == 4:
            player.carriage = player.carriage.greaterCarriage
            i= len(player.road) - 1
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card) 
                i-=1
        elif(len(player.road)) >= 4 and player.carriage != None and player.carriage.routeLength == 3:
            player.carriage = player.carriage.greaterCarriage
            i= len(player.road) - 1
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card)    
                i-=1
        elif(len(player.road)) >= 3 and player.carriage == None:            
            player.carriage = self.carriage
            i= len(player.road) - 1
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card)
                i-=1
        else:
            i= len(player.road) - 1
            j = 0
            while i >= j :
                card = player.road.pop(i)
                self.binDeck.append(card)    
                i-=1
        
        i= len(player.hand) - 1
        j = 3
        while i >= j :
            card = player.hand.pop(i)
            self.binDeck.append(card)
            i-=1
                
        self.update()

            
    def putACard(self, player, index):
        if len(player.road) == 0:
            player.road.append(player.hand.pop(index))
        elif self.canPut(player, player.hand[index]) != 0:
            self.runMessageBox(self.canPut(player, player.hand[index]))
            if self.messageBox.wantQuit != 0 :
                if self.messageBox.choix == "Left":
                    player.road.insert(0, player.hand.pop(index))
                elif self.messageBox.choix == "Rigth":
                    player.road.append(player.hand.pop(index))
        else:
            pass

        self.update()

        if self.event == EVENT.END_TURN:
            self.endTurn.config(state=NORMAL)
    
    def canPut(self, player, card):
        for city in player.road:
            if city.name == card.name:
                return 0 
                
        for city in card.city.directlyAdjacentCities :
            if player.road[0].name == city.name:
                if player.road[-1].name == city.name:
                    return 3
                else:
                    return 2    
            elif player.road[-1].name == city.name: 
                if player.road[0].name == city.name: 
                    return 3
                else:
                    return 1
        return 0 
    
    def ClickCloseDeck(self):
        self.takeACard(self.human, -1)
         
    def ClickOpenDeck(self, nbCard):
        self.takeACard(self.human, nbCard)

    def ClickPostillionTile(self):
        print("Official Postillon")
        
    def ClickAmtmannTile(self ):
        print("Official Amtman")
        
    def ClickPostmeisterTile(self):
        self.card01.config(state=NORMAL)
        self.card02.config(state=NORMAL)
        self.card03.config(state=NORMAL)
        self.card04.config(state=NORMAL)
        self.card05.config(state=NORMAL)
        self.card06.config(state=NORMAL)
        self.postmeisterTile.config(state=DISABLED)
        self.closeDeckButton.config(state=NORMAL)
        
    def ClickWagnerTile(self):
        print("Official Wagner")
        
    def runMessageBox(self, canPut):
        self.messageBox = MessageBox.Interface(self.fenetre)
        if canPut == 2 :
            self.messageBox.rigthButton.config(state=DISABLED)
        elif canPut == 1 : 
            self.messageBox.leftButton.config(state=DISABLED)
        else:
            self.messageBox.rigthButton.config(state=NORMAL)
            self.messageBox.leftButton.config(state=NORMAL)
        
        self.fenetre.wait_window(self.messageBox.top)

    def playFinish(self):
        self.play(EVENT.BEGIN_TURN)