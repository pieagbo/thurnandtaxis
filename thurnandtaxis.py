# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:27:52 2015

@author: pieagbo
"""

from Parser import *
from tkinter import *
import GameBoard
import MessageBox
import SettingsBoard
from random import *
from tkinter.messagebox import *


class ThurnAndTaxis: 
    def __init__(self):
        self.name = None
        self.gameBoardWidth = 1900
        self.gameBoardHeight = 1000
        self.gameBoardImage = "utils/images/"
        self.backCardImage = "utils/images/"
        self.nbMinCityCardsCloseRoute = None        
        self.nbMaxCityCardsRouteClosed = None    
        self.nbCityCardsCartwrightAdvantage = None    
        self.initialNbHouses = None

        self.officials = None
        self.provinces = None
        self.cities = None
        self.carriages = None
        
        self.provinceBonus = None
        self.allProvincesBonus = None
        self.endGameBonus = None
        self.longRouteBonus7 = None
        self.longRouteBonus6 = None
        self.longRouteBonus5 = None
        
        self.closeDeck = list()
        self.openDeck = list()
        self.binDeck = list()
        
        self.IAone= None
        self.IAthree= None
        self.IAfour= None
        self.human = None
        
        self.houses = None
        
        self.settings = None
 
        self.board = None
        
        self.messageBox = None
        
        self.runSettingsBoard()
        if self.settings.wantQuit != 1 :        
            self.parser = ParseXMLElements()
            
            self.initGame(self.parser.gameName, self.parser.game_board_image, self.parser.back_card_image,
                          self.parser.nb_min_city_cards_close_route, self.parser.nb_max_city_cards_route_closed,self.parser.nb_city_cards_Cartwright_advantage,
                          self.parser.initial_nb_houses, self.parser.officials, self.parser.provinces,self.parser.cities,self.parser.carriages,self.parser.provinceBonus,
                          self.parser.allProvincesBonus,self.parser.endGameBonus, self.parser.longRouteBonus7, self.parser.longRouteBonus6, self.parser.longRouteBonus5,
                          self.parser.cards,self.parser.houses, self.settings.human, self.settings.IAone,self.settings.IAthree, self.settings.IAfour)
    
    def initGame(self, name, gameBoardImage, backCardImage, nbMinCityCardsCloseRoute, nbMaxCityCardsRouteClosed, 
                       nbCityCardsCartwrightAdvantage, initialNbHouses, officials, provinces, cities, carriages, 
                       provinceBonus, allProvincesBonus, endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, cards, houses, human, IAone, IAthree, IAfour):
        self.name = name
        self.gameBoardWidth = 1900
        self.gameBoardHeight = 1000
        self.gameBoardImage += gameBoardImage
        self.backCardImage += backCardImage
        self.nbMinCityCardsCloseRoute = nbMinCityCardsCloseRoute        
        self.nbMaxCityCardsRouteClosed = nbMaxCityCardsRouteClosed    
        self.nbCityCardsCartwrightAdvantage = nbCityCardsCartwrightAdvantage    
        self.initialNbHouses = initialNbHouses

        self.officials = officials
        self.provinces = provinces
        self.cities = cities
        self.carriages = carriages
        
        self.provinceBonus = provinceBonus
        self.allProvincesBonus = allProvincesBonus
        self.endGameBonus = endGameBonus
        self.longRouteBonus7 = longRouteBonus7
        self.longRouteBonus6 = longRouteBonus6
        self.longRouteBonus5 = longRouteBonus5
        
        self.closeDeck = cards
        shuffle(self.closeDeck)
        shuffle(self.closeDeck)  
        shuffle(self.closeDeck)  
        
        i = 0 
        while i < 6 : 
            card = self.closeDeck.pop()
            self.openDeck.append(card)
            i+=1
        
        self.binDeck = list()
        
        self.IAone= IAone
        self.IAthree= IAthree
        self.IAfour= IAfour
    
        self.human = human
        
        self.houses = houses
        
        self.runGameBoard(self.name, self.gameBoardWidth, self.gameBoardHeight, self.gameBoardImage,self.backCardImage,self.provinceBonus, 
                          self.allProvincesBonus, self.endGameBonus, self.longRouteBonus7, self.longRouteBonus6, self.longRouteBonus5,self.officials, self.closeDeck, self.openDeck,
                          self.IAone, self.IAthree, self.IAfour, self.human, self.houses)       
        
        
    def runSettingsBoard(self):
        fenetre = Tk()
        fenetre.geometry('600x235+200+200')
        self.settings = SettingsBoard.Interface(fenetre)
        self.settings.mainloop()

    
    def runGameBoard(self, name, gameBoardWidth, gameBoardHeight, gameBoardImage, backCardImage, provinceBonus, allProvincesBonus, 
                     endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, officials, closeDeck, openDeck, IAone, IAthree, IAfour, human, houses):
        fenetre = Tk()
        self.board = GameBoard.Interface(fenetre, name, gameBoardWidth, gameBoardHeight, gameBoardImage, backCardImage, provinceBonus,
                                         allProvincesBonus, endGameBonus, longRouteBonus7, longRouteBonus6, longRouteBonus5, officials, closeDeck, openDeck, IAone, IAthree, IAfour, human, houses)
        self.board.mainloop()
    
    def runMessageBox(self):
        fenetre = Tk()
        fenetre.geometry('200x150+200+200')
        self.messageBox = MessageBox.Interface(fenetre)
        self.messageBox.mainloop()
        
    
if __name__ == '__main__':
    ThurnAndTaxis()

