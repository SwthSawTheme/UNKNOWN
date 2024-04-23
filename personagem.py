
class Personagem(object):
    
    
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero
        self.sanidade = 0
        self.dinheiro = 0.0
        self.itens = []
        self.relacionamento = {None: 10}
    
            
    def adicionarItem(self,item:str):
        return self.itens.append(item)
    
    def verificarItens(self):
        return self.itens
    
    def removerItem(self,item: str):
        return self.itens.remove(item)
    
    def alterarSanidade(self,valor:int):
        self.sanidade += valor
    
    def aumentarDinheiro(self,valor:float):
        self.dinheiro += valor
    
    def verificarDinheiro(self):
        return self.dinheiro
    
    def diminuirDinheiro(self,valor:float):
        self.dinheiro -= valor
    
    def aumentarRelacionamento(self,player,valor:int):
        if player.nome not in self.relacionamento:
            self.relacionamento[player.nome] = 10
        self.relacionamento[player.nome] += valor
    
    def diminuirRelacionamento(self,player,valor: int):
        if player.nome not in self.relacionamento:
            self.relacionamento[player.nome] = 10
        self.relacionamento[player.nome] -= valor
    
    def verificarRelacionamento(self,player):
        if player.nome in self.relacionamento:
            return self.relacionamento[player.nome]
        else:
            return 0


if __name__ == "__main__":
    player = Personagem("Saw","homem")
    npc = Personagem("Julia","mulher")
    
    npc.aumentarRelacionamento(player,1)
    print(npc.nome)
    print(npc.verificarRelacionamento(player))
    print(player.nome)
    print(player.verificarRelacionamento(npc))