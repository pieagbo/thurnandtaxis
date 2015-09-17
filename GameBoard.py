# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:37:01 2015

@author: rsalem
"""

# On importe Tkinter
from tkinter import *
from PIL import Image, ImageTk
from Model import *


class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, name, gameBoardWidth, gameBoardHeight, gameBoardImage, backCardImage, provinceBonus, allProvincesBonus, 
                     endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, officials, closeDeck, openDeck, IAone, IAthree, IAfour, human, houses, **kwargs):
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
        self.binDeck = list()
        
        self.IAone= IAone
        self.IAthree= IAthree
        self.IAfour= IAfour
        self.human = human
        
        self.houses = houses
        
        #Create a self.canvas
        self.canvas = Canvas(fenetre, width=1273, height=800)
        self.canvas.pack()
        
        self.initializeImage()
        self.initializeText()
        
        self.play()
        
    
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
        i = 0 
        handplayer = list()
        while i < len(self.human.hand):
            handplayer.append(Image.open('utils/images/' + self.human.hand[i].city.image))
            i+=1
        
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
        
        # Add the image to the self.canvas, and set the anchor to the top left / north west corner
        self.canvas.config(bg="light goldenrod")
        
        canvasBlue = self.canvas.create_rectangle(635, 5, 950, 220, fill = self.IAone.color.name)
        canvasYellow = self.canvas.create_rectangle(955, 5, 1270, 220, fill = self.human.color.name)
        canvasRed = self.canvas.create_rectangle(635, 225, 950, 430, fill = self.IAthree.color.name)
        canvasGreen = self.canvas.create_rectangle(955, 225, 1270, 430, fill = self.IAfour.color.name)
    
        
        self.canvas.create_image(0, 0, image=self.canvas.board, anchor='nw')
        self.canvas.create_image(1140, 440, image=self.canvas.Deck, anchor='nw', tag="CloseDeck")
        self.canvas.tag_bind("CloseDeck", "<Button-1>", self.ClickCloseDeck)
        
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
        self.card01 = self.canvas.create_image(735, 440, image=self.canvas.card01, anchor='nw', tag="OpenDeck1")
        self.card02 = self.canvas.create_image(857, 440, image=self.canvas.card02, anchor='nw', tag="OpenDeck2")
        self.card03 = self.canvas.create_image(978, 440, image=self.canvas.card03, anchor='nw', tag="OpenDeck3")
        self.card04 = self.canvas.create_image(735, 480, image=self.canvas.card04, anchor='nw', tag="OpenDeck4")
        self.card05 = self.canvas.create_image(857, 480, image=self.canvas.card05, anchor='nw', tag="OpenDeck5")
        self.card06 = self.canvas.create_image(975, 480, image=self.canvas.card06, anchor='nw', tag="OpenDeck6")
        self.canvas.tag_bind("OpenDeck1", "<Button-1>", lambda event,arg=0: self.ClickOpenDeck(event, arg))
        self.canvas.tag_bind("OpenDeck2", "<Button-1>", lambda event,arg=1: self.ClickOpenDeck(event, arg))
        self.canvas.tag_bind("OpenDeck3", "<Button-1>", lambda event,arg=2: self.ClickOpenDeck(event, arg))
        self.canvas.tag_bind("OpenDeck4", "<Button-1>", lambda event,arg=3: self.ClickOpenDeck(event, arg))
        self.canvas.tag_bind("OpenDeck5", "<Button-1>", lambda event,arg=4: self.ClickOpenDeck(event, arg))
        self.canvas.tag_bind("OpenDeck6", "<Button-1>", lambda event,arg=5: self.ClickOpenDeck(event, arg))
        
        #Official
#        self.canvas.create_image(640, 440, image=self.canvas.postillion, anchor='nw')
        self.canvas.create_image(635, 440, image=self.canvas.postillionTile , anchor='nw', tag="postillionTile")
        self.canvas.tag_bind("postillionTile", "<Button-1>", self.ClickPostillionTile)
        
#        self.canvas.create_image(690, 440, image=self.canvas.amtmann, anchor='nw')
        self.canvas.create_image(635, 485, image=self.canvas.amtmannTile, anchor='nw', tag="amtmannTile")
        self.canvas.tag_bind("amtmannTile", "<Button-1>", self.ClickAmtmannTile)
        
#        self.canvas.create_image(640, 900, image=self.canvas.postmeister, anchor='nw')
        self.canvas.create_image(680, 440, image=self.canvas.postmeisterTile, anchor='nw', tag="postmeisterTile")
        self.canvas.tag_bind("postmeisterTile", "<Button-1>", self.ClickPostmeisterTile)
        
#        self.canvas.create_image(690, 900, image=self.canvas.wagner, anchor='nw')
        self.canvas.create_image(680, 485, image=self.canvas.wagnerTile, anchor='nw', tag="wagnerTile")
        self.canvas.tag_bind("wagnerTile", "<Button-1>", self.ClickWagnerTile)
        
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
        

        for card in self.canvas.handplayer:
            self.canvas.create_image(0,755, image=card, anchor="nw")

    
    def initializeText(self):
        self.nbCardsCloseDeck = self.canvas.create_text(1160, 500, text=len(self.closeDeck), fill="white", anchor='nw', font="Helvetica 16")
        
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
            print(self.IAone.bonuses)
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
            
        i = 0 
        handplayer = list()
        while i < len(self.human.hand):
            handplayer.append(Image.open('utils/images/' + self.human.hand[i].city.image))
            i+=1

        
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
        self.canvas.itemconfig(self.card01, image=self.canvas.card01)
        self.canvas.itemconfig(self.card02, image=self.canvas.card02)
        self.canvas.itemconfig(self.card03, image=self.canvas.card03)
        self.canvas.itemconfig(self.card04, image=self.canvas.card04)
        self.canvas.itemconfig(self.card05, image=self.canvas.card05)
        self.canvas.itemconfig(self.card06, image=self.canvas.card06) 
        
        self.canvas.itemconfig(self.nbCardsCloseDeck, text=len(self.closeDeck)) 
        
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
        
        for card in self.canvas.handplayer:
            self.canvas.create_image(0,755, image=card, anchor="nw")

    def play(self):
        pass
    
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
                i = 0
                while i < len(self.binDeck):
                    card = self.binDeck.pop
                    self.closeDeck.add(card)
                
                card = self.closeDeck.pop()
                player.hand.append(card)
            else:
                card = self.closeDeck.pop()
                player.hand.append(card)
                
                
    def discardRoad(self, player):
        i = 0 
        while i < len(player.road):
            card = player.road.plop()        
            self.binDeck.add(card)
            i+=1
            
    def putACard(self, player, card):
        if len(player.road) == 0:
            road.append(card)
        elif self.canPut(player, hand) == 1:
            self.runSettingsBoard()
            if self.messageBoxself.wantQuit != 0 :
                if self.messageBoxself.choix == "Left":
                    player.road.insert(0,card)
                elif self.messageBoxself.choix == "Rigth":
                    player.road.append(card)
        else:
            print('pas cool')
    
    def canPut(self, player, card):
        if card.city.directlyAdjacentCities.count(player.road[0]) > 0 : 
            return 1
        elif card.city.directlyAdjacentCities.count(player.road[len(player.road) - 1]) > 0 : 
            return 1
        else:
            return 0
    
    def ClickCloseDeck(self, event):
        self.takeACard(self.human, -1)
        self.update()
         
    def ClickOpenDeck(self, event, nbCard):
        self.takeACard(self.human, nbCard)
        self.update()



    def ClickPostillionTile(self, event):
        print("Official Postillon")
        
    def ClickAmtmannTile(self, event ):
        print("Official Amtman")
        
    def ClickPostmeisterTile(self, event):
        print("Official Postmeister")
        
    def ClickWagnerTile(self, event):
        print("Official Wagner")
