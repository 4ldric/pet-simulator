from abc import abstractmethod


class Pet:
    def __init__(self, nome, idade, raca):
        self.__nome = nome
        self.__idade = idade
        self.__raca = raca

    # Getters
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_raca(self):
        return self.__raca
    
    # Comportamentos
    @abstractmethod
    def dormir(self):
        pass
    
    def comer(self):
        pass
    
    
    def brincar(self):
        pass

#  Raças
class cachorro(Pet):
    def dormir(self):
        return f"{self.get_nome()} se deitou para dormir!"
    
    def brincar(self):
        return f"{self.get_nome()} esta brincando!"
    
    def comer(self):
        return f"{self.get_nome()} esta comendo!"
    
dog = cachorro("spike", 1, "cachorro")

