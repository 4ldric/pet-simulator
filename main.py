from abc import ABC, abstractmethod
from random import randint
from re import I

class Pet(ABC):
    """classe orquestradora da parte animal do jogo"""
    def __init__(self, nome, raca, idade= 1, fome=100, felicidade= 10, energia= 70):
        self.__nome = nome
        self.__raca = raca
        self.__idade = idade
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
        return f"{self.get_nome()} recuperou sua energia e aumentou sua fome para {self.get_fome()}"

    @abstractmethod
    def get_brincadeiras_disponiveis(self):
        pass

    @abstractmethod
    def brincar(self, brincadeira):
        self.__energia -= self.get_brincadeiras_disponiveis()[brincadeira]
        self.__fome += self.get_brincadeiras_disponiveis()[brincadeira]
        self.__felicidade += randint(self.get_brincadeiras_disponiveis()[brincadeira] * 2, self.get_brincadeiras_disponiveis()[brincadeira] * 4)
        return f"{self.get_nome()} brincou tanto que perdeu {self.get_brincadeiras_disponiveis()[brincadeira]} de energia, aumentou sua fome para {self.get_fome()} e aumentou sua felicidade para {self.get_felicidade()}"

    @abstractmethod
    def get_comidas_disponiveis(self):
        pass

    @abstractmethod
    def comer(self, comida):
        self.__fome -= self.get_comidas_disponiveis()[comida]
        self.__felicidade += self.get_comidas_disponiveis()[comida] // 2
        self.__energia -= self.get_comidas_disponiveis()[comida] // 2
        return f"{self.get_nome()} saciou sua fome para {self.get_fome()}, aumentou sua felicidade para {self.get_felicidade()} e diminui sua energia para {self.get_energia()}! "

#  Raças
class cachorro(Pet):
    def dormir(self):
        if not self.get_energia() >= 65:
            print(f"{self.get_nome()} não esta com sono!")
        else:
            return f"{self.get_nome()} se deitou para dormir..\nSeu pet {super().dormir()}"
    
    def get_brincadeiras_disponiveis(self):
        lista_brincadeiras = {"Jogar-graveto": 10, "Corrida": 20, "Cabo-guerra": 30 }
        return lista_brincadeiras

    def brincar(self,brincadeira):
        if not self.get_energia() > self.get_brincadeiras_disponiveis()[brincadeira]:
            return False
        else:
            return (f"{self.get_nome()}, {super().brincar(brincadeira)}")
    
    def get_comidas_disponiveis(self):
        lista_comidas = {"petisco": 10, "carne": 20, "ração": 30}
        return lista_comidas

    def comer(self, comida):
        if not self.get_fome() < 100:
            return False
        else:
            return f"{self.get_nome()} {super().comer(comida)}"

class gato(Pet):
    def dormir(self):
        if not self.get_energia() >= 65:
            return f"{self.get_nome()} não esta com sono!"
        else:
            return f"{self.get_nome()} {super().dormir()}"

    def get_brincadeiras_disponiveis(self):
        lista_brincadeiras = {"arranhador": 10, "perseguir-laser": 20, "caçar-rato": 30}
        return lista_brincadeiras

    def brincar(self, brincadeira):
        if not self.get_energia() > self.get_brincadeiras_disponiveis()[brincadeira]:
            return False
        else:
            return super().brincar(brincadeira)

    def get_comidas_disponiveis(self):
        lista_comidas = {"petisco": 10, "peixe": 20, "ração": 30}
        return lista_comidas

    def comer(self, comida):
        if not self.get_fome() < 100:
            return False
        else:
            return super().comer(comida)


class Jogo:
    """Classe orquestradora das logicas do game"""        
    def brincadeira(self):
        print(" === Brincadeiras ===")
        brincadeiras = []
        for indice, brincadeira_disponivel in enumerate(self.meu_pet.get_brincadeiras_disponiveis(), start=1):
            brincadeiras.append(brincadeira_disponivel)
            print( f"""» [{indice}]. {brincadeira_disponivel}""" )
        escolha = int(input("\nEscolha a brincadeira: "))
        indice_ajustado = escolha - 1
        brincadeira = brincadeiras[indice_ajustado]
        resultado = self.meu_pet.brincar(brincadeira)
        if not resultado:
            print(f"{self.get_nome()} não tem energia suficiente para esta brincadeira!" )
        else:
            print(resultado)

    def alimentar(self):
        comidas = []
        print("=== comidas ===")
        for indice, comida_disponivel in enumerate(self.meu_pet.get_comidas_disponiveis(), start = 1):
            comidas.append(comida_disponivel)
            print(f"""» [{indice}]. {comida_disponivel}""")
        escolha = int(input("\nEscolha a comida para seu pet: "))
        indice_ajustado = escolha - 1
        comida = comidas[indice_ajustado]
        resultado = self.meu_pet.comer(comida)
        if not resultado:
            print(f"{self.meu_pet.get_nome()} esta de buxo cheio!")
        else:
            print(resultado)

    def dormir(self):
        self.meu_pet.dormir()

    def criar_pet(self):
        racas_disponiveis = {"Cachorro": cachorro, "Gato": gato}
        lista_racas = []
        print("=== Raças Disponiveis ===")
        for indice, raca in enumerate(racas_disponiveis, start = 1):
            lista_racas.append(raca)
            print( f"» [{indice}]. {raca}")
        escolha = input("Escolha a raça do seu pet ou digite [0] para cancelar: ")
        if escolha != "0":
            indice_ajustado = int(escolha) - 1
            nome = input("Digite o nome do seu pet: ")
            raca =  lista_racas[indice_ajustado]
            return self.meu_pet = racas_disponiveis[raca](nome,raca)
        else:
            print("saindo...")
            
    def menu_inicial(self):
        print("\n=== Menu Inicial ===")
        print(
            """
» [1]. Escolher raça
» [2]. Sair 
            """)
        escolha = input("Digite uma opção: ")
        if escolha == "1":
            self.criar_pet()
        else:
            print("Saindo...")
            

    def iniciar_jogo(self):
        self.meu_pet = None
        jogar = True
        while jogar:
            if self.meu_pet is None:
                self.menu_inicial()
            else:
                self.menu_principal()
jogo = Jogo()


jogo.iniciar_jogo()
