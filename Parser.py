# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:23:53 2015

@author: pieagbo
"""

from Model import *
from lxml import *

class ParseXMLElements:
    def __init__(self):
        self.officials = set() 
        self.provinces = set()
        self.cities = set()
        self.carriages = list()
        self.provinceBonuses = list()
        self.allProvincesBonuses = list()
        self.endGameBonuses = list()
        self.longRouteBonuses = list()
        self.longRouteBonuses7 = list()
        self.longRouteBonuses6 = list()
        self.longRouteBonuses5 = list()
        self.cards = list()
        self.cityDict = {}
        self.provinceDict = {}
        self.houses = set() 
        self.tree = etree.parse("utils/game_elements-Thurn_and_Taxis.xml")
    
        for node in self.tree.iter('game'):
            self.gameName =  node.find('name').text
            self.game_board_image = node.find('game_board_image').text
            self.back_card_image = node.find('back_card_image').text
            self.nb_copies_city_cards = int(node.find('nb_copies_city_cards').text)
            self.nb_min_city_cards_close_route = node.find('nb_min_city_cards_close_route').text
            self.nb_max_city_cards_route_closed = node.find('nb_max_city_cards_route_closed').text
            self.nb_city_cards_Cartwright_advantage = node.find('nb_city_cards_Cartwright_advantage').text
            self.initial_nb_houses= node.find('initial_nb_houses').text
                
         
        for node in self.tree.iter('houses'):
            yellowHouse = House(Color.YELLOW, node.find('black_house_image').text)
            redHouse = House(Color.RED, node.find('red_house_image').text)
            greenHouse = House(Color.GREEN, node.find('green_house_image').text)
            blueHouse = House(Color.BLUE, node.find('blue_house_image').text)
            
        self.houses.add(yellowHouse)
        self.houses.add(redHouse)
        self.houses.add(greenHouse)
        self.houses.add(blueHouse)


        for node in self.tree.iter('officials'):
            for official in node.iter('official'):
                name = official.find('name').text
                symbol_image = official.find('symbol_image').text
                person_image = official.find('person_image').text
                if name == "Postmaster" : 
                    postmaster = Postmaster(name,symbol_image,person_image)
                    self.officials.add(postmaster)
                elif name == "Postal carrier" : 
                    postalcarrier = PostalCarrier(name,symbol_image,person_image)
                    self.officials.add(postalcarrier)
                elif name == "Administrator" : 
                    administrator = Administrator(name,symbol_image,person_image)
                    self.officials.add(administrator)
                elif name == "Cartwright" : 
                    cartwright = Cartwright(name,symbol_image,person_image)
                    self.officials.add(cartwright)
                    
           
        for node in self.tree.iter('carriages'):
            for carriage in node.iter('carriage'):
                route_length = int(carriage.find('route_length').text)
                nb_victory_points = int(carriage.find('nb_victory_points').text)
                carriage = Carriage(route_length,nb_victory_points)    
                self.carriages.append(carriage)
           
        carriage_greater = None
        for cr in self.carriages:
            cr.greaterCarriage = carriage_greater
            carriage_greater = cr
        self.carriages.reverse()
        self.carriage = self.carriages[0]

        
        for node in self.tree.iter('provinces'):
            for province in node.iter('province'):
                name = province.find('name').text
                province = Province(name)
                self.provinces.add(province)
                
        
        for node in self.tree.iter('provinces'):
            for province in node.iter('province'):
               for city in province.iter('city'):
                   name = city.find('name').text
                   image = city.find('image').text
                   city = City(name,image)
                   self.cities.add(city)
                  
        for c in self.cities:
            self.cityDict[c.name] = c  
            
        for p in self.provinces:
            self.provinceDict[p.name] = p
            
        for node in self.tree.iter('provinces'):
            for province in node.iter('province'):
                for city in province.iter('city'):
                    p = self.provinceDict.get(province.find('name').text)
                    p.cities.add(self.cityDict.get(city.find('name').text))
        
        for node in self.tree.iter('provinces'):
            for province in node.iter('province'):
                for city in province.iter('city'):
                    c = self.cityDict.get(city.find('name').text)
                    c.province = self.provinceDict.get(province.find('name').text)
        
        for node in self.tree.iter('direct_adjacences'):
            for direct_adjacence in node.iter('direct_adjacence'):
                c = self.cityDict.get(direct_adjacence.find('from').text)
                c.directlyAdjacentCities.add(self.cityDict.get(direct_adjacence.find('to').text))
                
        for node in self.tree.iter('direct_adjacences'):
            for direct_adjacence in node.iter('direct_adjacence'):
                c = self.cityDict.get(direct_adjacence.find('to').text)
                c.directlyAdjacentCities.add(self.cityDict.get(direct_adjacence.find('from').text))
        
        for c in self.cities:
            i = 0 
            while i < self.nb_copies_city_cards:
                card = ClosePick(c.name, c)
                self.cards.append(card)
                i+=1
        
        for node in self.tree.iter('bonus'):
            for provinces_bonus in node.iter('provinces_bonus'):
                for province_bonus in node.iter('province_bonus'):
                    province_bonusSet = list()
                    for tile in province_bonus.iter('tile'):
                        image = tile.find('image').text
                        nb_victory_points = int(tile.find('nb_victory_points').text)
                        bonus = ProvinceBonus(nb_victory_points, image)
                        for province in provinces_bonus.iter('province'):
                            bonus.provinces.add(self.provinceDict.get(province.find('name').text)) 
                        province_bonusSet.append(bonus)
                    province_bonusSet.reverse()
                    self.provinceBonuses.append(province_bonusSet)
                    
        
        for provinceBonusesList in self.provinceBonuses:
            bonus_smaller = None
            for bonus in provinceBonusesList:
                bonus.smallerBonus = bonus_smaller
                bonus_smaller = bonus
         
        self.provinceBonus = list()
        for provinceBonusesList in self.provinceBonuses:
             self.provinceBonus.append(provinceBonusesList.pop())

            
        for node in self.tree.iter('bonus'):
            for all_provinces_bonus in node.iter('all_provinces_bonus'):
                for tile in all_provinces_bonus.iter('tile'):
                    image = tile.find('image').text
                    nb_victory_points = int(tile.find('nb_victory_points').text)
                    bonus = AllProvincesBonus(nb_victory_points, image)
                    self.allProvincesBonuses.append(bonus)
                
                self.allProvincesBonuses.reverse() 
                for p in self.provinceDict:
                    if p != all_provinces_bonus.find('province_name_avoid').text:
                        for bonus in self.allProvincesBonuses:
                            bonus.provinces.add(self.provinceDict[p])

        bonus_smaller = None
        for bonus in self.allProvincesBonuses:
            bonus.smallerBonus = bonus_smaller
            bonus_smaller = bonus
        
        self.allProvincesBonus = self.allProvincesBonuses.pop()
        
        for node in self.tree.iter('bonus'):
            for long_route_bonus in node.iter('long_route_bonus'):
                for tile in long_route_bonus.iter('tile'):
                    image = tile.find('image').text
                    nb_victory_points = int(tile.find('nb_victory_points').text)
                    route_length = int(tile.find('route_length').text)
                    
                    longroutebonus = LongRouteBonus(nb_victory_points, image, route_length)
                    if route_length == 7 : 
                        self.longRouteBonuses7.append(longroutebonus)
                    elif route_length == 6:
                        self.longRouteBonuses6.append(longroutebonus)
                    elif route_length == 5:
                        self.longRouteBonuses5.append(longroutebonus)
        
        self.longRouteBonuses7.reverse()
        self.longRouteBonuses.append(self.longRouteBonuses7)
        
        self.longRouteBonuses6.reverse()
        self.longRouteBonuses.append(self.longRouteBonuses6)
        
        self.longRouteBonuses5.reverse()
        self.longRouteBonuses.append(self.longRouteBonuses5)
        

        for longRouteBonusesList in self.longRouteBonuses:
            bonus_smaller = None
            for bonus in longRouteBonusesList:
                bonus.smallerBonus = bonus_smaller
                bonus_smaller = bonus
        
        self.longRouteBonus7 = self.longRouteBonuses7.pop()
        self.longRouteBonus6 = self.longRouteBonuses6.pop()
        self.longRouteBonus5 = self.longRouteBonuses5.pop()
        
        for node in self.tree.iter('bonus'):
            for end_game_bonus in node.iter('end_game_bonus'):
                for tile in end_game_bonus.iter('tile'):
                    image = tile.find('image').text
                    nb_victory_points = int(tile.find('nb_victory_points').text)
                    bonus = EndGameBonus(nb_victory_points, image)
                    self.endGameBonuses.append(bonus)
                
                self.endGameBonuses.reverse() 

        bonus_smaller = None
        for bonus in self.endGameBonuses:
            bonus.smallerBonus = bonus_smaller
            bonus_smaller = bonus
        
        self.endGameBonus = self.endGameBonuses.pop()

        