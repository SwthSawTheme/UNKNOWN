
class Personagem(object):
    
    
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero
        self.sanidade = 0
        self.dinheiro = 0.0
        self.itens = []
        self.relacionamento = {None: 10}
    
            
    def addItem(self,item:str):
        return self.itens.append(item)
    
    def getItens(self):
        return self.itens
    
    def removeItem(self,item: str):
        return self.itens.remove(item)
    
    def addSanidade(self,valor:int):
        self.sanidade += valor
    
    def addDinheiro(self,valor:float):
        self.dinheiro += valor
    
    def getDinheiro(self):
        return self.dinheiro
    
    def updateDinheiro(self,valor:float):
        self.dinheiro -= valor
    
    def addRelacionamento(self,player,valor:int):
        if player.nome not in self.relacionamento:
            self.relacionamento[player.nome] = 10
        self.relacionamento[player.nome] += valor
    
    def updateRelacionamento(self,player,valor: int):
        if player.nome not in self.relacionamento:
            self.relacionamento[player.nome] = 10
        self.relacionamento[player.nome] -= valor
    
    def getRelacionamento(self,player):
        if player.nome in self.relacionamento:
            return self.relacionamento[player.nome]
        else:
            return 0


if __name__ == "__main__":
    player = Personagem("Saw","homem")
    npc = Personagem("Julia","mulher")
    
    