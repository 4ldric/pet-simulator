from abc import ABC, abstractmethod


class Pet(ABC):
    """classe orquestradora da parte animal do jogo"""
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
    
    @abstractmethod
    def get_brincadeiras_disponiveis(self):
        pass

    @abstractmethod
    def brincar(self, bricadeira):
        pass

    # comportamentos restantes
    def comer(self, comida):
        pass


#  Raças
class cachorro(Pet):
    def dormir(self):
        if not self.get_energia() < 65:
            print(f"{self.get_nome} não esta com sono!")
        else:
            return f"{self.get_nome()} se deitou para dormir..\nSeu pet {super().dormir()}"
    
    def get_brincadeiras_disponiveis(self):
        lista_brincadeiras = {
            "Jogar-graveto": 10,
            "Corrida": 20,
            "Cabo-guerra": 30 
        }
        return lista_brincadeiras

    def brincar(self,brincadeira):
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


class Jogo:
    """Classe orquestradora das logicas do game"""
    def __init__(self):
        self.dog = cachorro("spike", 1, "cachorro")
        self.listas_brincadeiras = self.dog.get_brincadeiras_disponiveis()

    def brincadeira(self):
        print(" === Brincadeiras ===")
        for indice, brincadeira in enumerate(self.listas_brincadeiras, start=1):
            print( f"""» [{indice}]. {brincadeira}""" )
        escolha = int(input("\nEscolha a brincadeira: "))
        indice_ajustado = escolha - 1
        brincadeiras = list(self.listas_brincadeiras.items())
        


jogo = Jogo()

jogo.brincadeira()
