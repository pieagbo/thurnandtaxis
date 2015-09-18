# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:56:21 2015

@author: pieagbo
"""

from enum import Enum

class CardinalPoint(Enum):
    SOUTH = 1
    WEST = 2
    NORTH = 3
    EAST = 4
    

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"


class EVENT(Enum):
    BEGIN_TURN = 0 
    ADMINISTRATOR = 1
    SUPPLY_OR_DISPLAY = 2
    POSTMASTER = 3 
    DISCARD_ROUTE = 4
    HAND = 5 
    POSTAL_CARRIER = 6
    END_TURN = 7 
    CLOSE_ROUTE = 8
    CARTWRIGHT = 9
    ROUTE = 10
    PLACE_HOUSE = 11   
    NO_CARDS_IN_HAND = 12
    TURN = 13
    
class Player:
    def __init__(self, name, color, order): 
        self.name = name
        self.nbPoint = 0
        self.color = color
        self.order = order
        self.carriage = None 
        self.houses = list()
        self.hand = list()       
        self.road = list()
        self.cities = set()
        self.bonuses = list()
        

class Human(Player):
    def __init__(self, name, color, order): 
        Player.__init__(self, name, color, order)


class IA(Player):
    def __init__(self, name, color, level, order):
        Player.__init__(self, name, color, order)
        self.level = level
        

class Official:
    def __init__(self, name, symbolImage, personImage): 
        self.name = name
        self.symbolImage = symbolImage
        self.personImage = personImage
        

class PostalCarrier(Official):
    def __init__(self, name, symbolImage, personImage): 
        Official.__init__(self, name, symbolImage, personImage)


class Postmaster(Official):
    def __init__(self, name, symbolImage, personImage):
        Official.__init__(self, name, symbolImage, personImage)


class Administrator(Official):
    def __init__(self, name, symbolImage, personImage): 
        Official.__init__(self, name, symbolImage, personImage)


class Cartwright(Official):
    def __init__(self, name, symbolImage, personImage):
        Official.__init__(self, name, symbolImage, personImage)


class Card:
    def __init__(self, name, city): 
        self.name = name
        self.city = city

class PlayerHand(Card):
    def __init__(self, name, city): 
        Card.__init__(self, name, city)


class PlayerRoad(Card):
    def __init__(self, name, city): 
        Card.__init__(self, name, city)


class OpenPick(Card):
    def __init__(self, name, city): 
        Card.__init__(self, name, city)


class ClosePick(Card):
    def __init__(self, name, city): 
        Card.__init__(self, name, city)
        

class BinPick(Card):
    def __init__(self, name, city): 
        Card.__init__(self, name, city)
        
        
class Bonus:
    def __init__(self, nbVictoryPoint, image): 
        self.nbVictoryPoint = nbVictoryPoint
        self.image = image
        self.smallerBonus = None
        

class LongRouteBonus(Bonus):
    def __init__(self, nbVictoryPoint, image, routeLength): 
        Bonus.__init__(self, nbVictoryPoint, image)
        self.routeLength = routeLength


class EndGameBonus(Bonus):
    def __init__(self, nbVictoryPoint, image): 
        Bonus.__init__(self, nbVictoryPoint, image)
        
        
class ProvinceBonus(Bonus):
    def __init__(self, nbVictoryPoint, image): 
        Bonus.__init__(self, nbVictoryPoint, image)
        self.provinces = set()
        
       
class AllProvincesBonus(Bonus):
    def __init__(self, nbVictoryPoint, image): 
        Bonus.__init__(self, nbVictoryPoint, image)
        self.provinces = set()
        
        
class Province:
    def __init__(self, name): 
        self.name = name
        self.cities = set()
        

class City:
    def __init__(self, name, image): 
        self.name = name
        self.image = image
        self.province = None
        self.directlyAdjacentCities = set()
        

class Carriage: 
    def __init__(self, routeLength, nbVictoryPoint): 
        self.routeLength = routeLength
        self.nbVictoryPoint = nbVictoryPoint
        self.greaterCarriage = None

class House:    
    def __init__(self, color, image):
        self.color = color
        self.image = image