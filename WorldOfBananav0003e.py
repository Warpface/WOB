#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:59:22 2018

@author: aleksander
"""

import json; import random; import time;

"""------------------------DATA STORAGE------------------------"""
"""
playerData contains:
    name: player name
    health: player start healthpoints
    stamina: movement points before needing rest
    inventory space: duh'
    inventory: LIST object with items in inventory
--------
itemData contains:
    every item has a DICT type. The name of this dict is the item name
    item stats:
        inventory usage: how much space it takes up in the inv.
        durability: "item health points"
        uses: "describes different uses of the items
            eat: INT type health gain or loss when eating said item
            hit: INT type base damage when hitting enemy or object
--------



"""
playerData = {
        "name": "player1",
        "health": 100,
        "stamina": 10, #movement points before needing rest
        "inventorySpace": 10,
        "inventory": {"banana": 100, "spork": 100} #list of items in inventory
        
        }
itemData = {
        "banana":{
                "inventoryUsage": 2,
                "durability": 1,
                "uses": {
                        "eat": 10, #hp gained when eaten
                        "damage": 1   #base damage per hit
                        }
                },
        "spork":{
                "inventoryUsage": 0.2,
                "durability": 50,
                "uses": {
                        "damage": 20, #base damage per hit
                        }
                }
        }
creatureData = {
        "rat":{
                "health": 10,
                "actions": {
                        "bite":{
                                "damage":15,
                                "chance":95
                                },
                        "tailwhip":{
                                "damage":1,
                                "chance":95
                                },
                        "squeak":{
                                "damage":0,
                                "chance":100
                                },
                        "flee":{
                                "chance":60   #in %
                                }
                        }
                },
        "Vampire":{
                "health": 70,
                "actions": {
                        "bite":{
                                "damage":40,
                                "chance":95
                                },
                        "stare":{
                                "damage":1,
                                "chance":95
                                },
                        "scratch":{
                                "damage":25,
                                "chance":100
                                },
                        "flee":{
                                "chance":20   #in %
                                }
                        }
                },
        "Cthulhu":{
                "health": 5000,
                "actions": {
                        "quack":{
                                "damage":50000,
                                "chance":100
                                }
                        }
                }
        }

"""------------------------FUNCTIONS------------------------"""
def chance(chance):
    chance = chance/100
    if chance >= (random.random()):
        return(True)
    else:
        return(False)
            
def creatureEncounter(creature):
    creaturePresent = 1 #Creature is present
    creatureAlive = 1 #Creature is alive
    creatureHealth = creatureData[creature]["health"]
    
    print("you have encountered a {} with {} health. You have {} health, what do you want to do?(attack/flee)".format(creature,creatureHealth,playerData["health"]))
    while creaturePresent == 1 and creatureAlive == 1:
        #Player acts first
        action = input("action: ")
        if action == "flee":
            fleeRoll = random.randint(1,100)
            if fleeRoll >= 50:
                print("You escape.")
                creaturePresent = 0
                break
            else:
                print("the %s outsmarted you, it is still there.... you moron...."%(creature))
        elif action == "attack":
            #attackItem = input("Attack with?(%s)"%(list(playerData["inventory"])))
            print("In inventory: ")
            for x in playerData["inventory"]:
                print(x)
            attackItem = input("Attack with? ")
            if attackItem in playerData['inventory'].keys():
                creatureHealth -= itemData[attackItem]["uses"]["damage"]
                if creatureHealth <= 0:
                    creatureAlive = 0
                    print("%s is dead."%creature)
                    break
                print("%s health is at %d."%(creature,creatureHealth))
        #Creature acts second
        creatureAction = random.choice(list(creatureData[creature]["actions"]))
        if creatureAction == "flee":
            print("The {} got away!".format(creature))
            creaturePresent = 0
        else:
            print("{} {}s for {} damage".format(creature, creatureAction, creatureData[creature]["actions"]["{}".format(creatureAction)]["damage"]))
            playerData["health"] -= creatureData[creature]["actions"]["{}".format(creatureAction)]["damage"]
            if playerData["health"] <= 0 or playerData["health"] == 0:
                if playerData["health"] <= 0:
                    playerData["health"] = 0
                print("Your health is at {}".format(playerData["health"]))
                print("---you died---")
                break
            print("Your health is at {}".format(playerData["health"]))
            
            
            
            
    print("....CHIRP......CHIRP............CHIRP........")
    time.sleep(1)
    

        
        
        
"""------------------------MAIN------------------------""" 

creatureEncounter(random.choice(list(creatureData)))





















