# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:56:21 2015

@author: pieagbo
"""

from enum import Enum
from lxml import etree

class CardinalPoint(Enum):
    SOUTH = 1
    WEST = 2
    NORTH = 3
    EAST = 4


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 4
    
    
class Player:
    def __init__(self, name, color): 
        self.name = name
        self.nbHouse = 20 
        self.nbPoint = 0
        self.color = color
        self.carriage = None 
        self.hand = list()       
        self.road = list()
        self.cities = set()
        self.bonuses = set()
        raise NotImplementedError
        

class Human(Player):
    def __init__(self, name, color): 
        Player.__init__(self, name, color)


class IA(Player):
    def __init__(self, name, color, level):
        Player.__init__(self, name, color)
        self.level = level
        

class Official:
    def __init__(self, name): 
        self.name = name 
        raise NotImplementedError

class PostalCarrier(Official):
    def __init__(self, name): 
        Official.__init__(self, name)


class Postmaster(Official):
    def __init__(self, name, level):
        Official.__init__(self, name)


class Administrator(Official):
    def __init__(self, name): 
        Official.__init__(self, name)


class Cartwright(Official):
    def __init__(self, name, level):
        Official.__init__(self, name)


class Card:
    def __init__(self, name, city): 
        self.name = name
        self.city = city
        raise NotImplementedError
        

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
    def __init__(self, nbVictoryPoint, bonus): 
        self.nbVictoryPoint = nbVictoryPoint
        self.smallerBonus = bonus
        raise NotImplementedError


class LongRouteBonus(Bonus):
    def __init__(self, nbVictoryPoint, bonus, routeLength): 
        Bonus.__init__(self, nbVictoryPoint, bonus)
        self.routeLength = routeLength


class EndGameBonus(Bonus):
    def __init__(self, nbVictoryPoint, bonus): 
        Bonus.__init__(self, nbVictoryPoint, bonus)
        
        
class ProvinceBonus(Bonus):
    def __init__(self, nbVictoryPoint, bonus): 
        Bonus.__init__(self, nbVictoryPoint, bonus)
        self.provinces = set()
        
       
class AllProvincesBonus(Bonus):
    def __init__(self, nbVictoryPoint, bonus, provinceNameAvoid): 
        Bonus.__init__(self, nbVictoryPoint, bonus)
        self.provinces = set()
        self.provinceNameAvoid = provinceNameAvoid
        
        
class Province:
    def __init__(self, name): 
        self.name = name
        self.cities = set()
        

class City:
    def __init__(self, name, province): 
        self.name = name
        self.province = province
        self.directlyAdjacentCities = set()
        

class Carriage: 
    def __init__(self, routeLength, nbVictoryPoint, greaterCarriage): 
        self.routeLength = routeLength
        self.nbVictoryPoint = nbVictoryPoint
        self.greaterCarriage = greaterCarriage


class Houses:    
    def __init__(self,color):
        self.color = color
        
        
    def parse_houses(self):
        tree = etree.parse("Elements.xml")
        for houses in tree.xpath("/game_elements/houses"):
            return (houses.text)