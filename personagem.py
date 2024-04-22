
class Personagem(object):
    
    
    def __init__(self,nome,genero):
        self.nome = nome
        self.genero = genero
        self.sanidade = 0
        self.dinheiro = 0.0
        self.itens = []
        self.relacionamento = {}
    
            
    def adicionarItem(self,item:str):
        pass
    
    def removerItem(self,item: str):
        pass
    
    def alterarSanidade(self,valor: int):
        pass
    
    def alterarDinheiro(self,valor: float):
        pass
    
    def aumentarRelacionamento(player,valor: int):
        pass
    
    def diminuirRelacionamento(player,valor: int):
        pass
    
    def verificarRelacionamento(player:str):
        pass
        