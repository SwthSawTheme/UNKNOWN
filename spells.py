from player import Player

class Spells(object):
    
    def __init__(self):
        self.name = str
        self.description = str
        self.ingredients = {str: int}
        self.consequences = str
        self.difficulty = int
        
    def getAvailability(self,player:Player):
        pass
    
    def calculateIngredientCost(self,player:Player):
        pass
    
    def getConsequences(self,player:Player):
        pass