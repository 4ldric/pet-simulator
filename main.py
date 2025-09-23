from abc import abstractmethod


class Pet:
    def __init__(self, nome, idade, raca, fome=15, felicidade=100, energia=50):
        self.__nome = nome
        self.__idade = idade
        self.__raca = raca
        self.__fome = fome
        self.__felicidade = felicidade
        self.__energia = energia

    # Getters
    def get_nome(self):
        return self.__nome
    def get_idade(self):
        return self.__idade
    def get_raca(self):
        return self.__raca
    def get_fome(self):
        return self.__fome
    def get_felicidade(self):
        return self.__felicidade
    def get_energia(self):
        return self.__energia

    # Comportamentos obrigatorios
    @abstractmethod
    def dormir(self):
        self.__fome += self.get_energia() // 2
        self.__energia = 100
        return f'recuperou sua energia e aumentou sua fome para {self.get_fome()}'
    # comportamentos restantes
    def comer(self, comida):
        pass

    def brincar(self, bricadeira):
        pass

#  Raças
class cachorro(Pet):
    def dormir(self):
        if not self.get_energia() < 65:
            print(f"{self.get_nome} não esta com sono!")
        else:
            return f"{self.get_nome()} se deitou para dormir..\nSeu pet {super().dormir()}"
    
    def brincar(self):
        return f"{self.get_nome()} esta brincando!"
    
    def comer(self):
        return f"{self.get_nome()} esta comendo!"

class gato(Pet):
    def dormir(self):
        return f"{self.get_nome()} se deitou para dormir!"

    def brincar(self):
        return f"{self.get_nome()} esta brincando!"

    def comer(self):
        return f"{self.get_nome()} esta comendo!"


dog = cachorro("spike", 1, "cachorro")
