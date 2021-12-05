import os
import sys
from csharp.entity import Entity
from csharp.generator import Generator

class CsharpGenerator():

    entities = []

    def __init__(self):
        self.interface()
        self.actionChooseOneOption()

    def interface(self):
        self.iWelcome()
        self.iActionOptions()

    def iWelcome(self):
        os.system("cmd /C clear")
        print("\n############################")
        print("#    C# CLASS GENERATOR    ")
        print("#                          ")
        print(f"#    Entidades criadas: {self.entities}")
        print("############################\n")

    def iActionOptions(self):
        print("\nO que deseja fazer:")
        print("     [ 1 ] Adicionar entidade")
        print("     [ 2 ] Gerar documentos")
        print("     [ 0 ] Voltar\n")
    
    def actionChooseOneOption(self):

        while True:
            action = input()

            if action == '0':
                break
            if action == '1':
                buildEntity = Entity()
                self.entities.append(buildEntity)
                self.interface()
            if action == '2':
                generate = Generator(self.entities)
                generate.generateEntities()

        return