from csharp import csharpgenerator, entity
import os
import sys

def main():
    sys.path.append(".")
    Interface()
    ActionChooseOneOption()

def Interface():
    IWelcome()
    IProgrammingLanguagesOptions()

def IWelcome():
    os.system("cmd /C clear")
    print("\n######################################")
    print("#    WELCOME TO CLASS GENERATOR      #")
    print("#         created by Lucas           #")
    print("######################################\n")

def IProgrammingLanguagesOptions():
    print("\nEscolha para qual linguagem deseja gerar a classe:")
    print("     [ 1 ] C#")
    print("     [ 0 ] Sair\n")

def ActionChooseOneOption():

    while True:
        language = input()

        if language == '0':
            break
        elif language == '1':    
            csharpgenerator.CsharpGenerator()
            Interface()

    return

if __name__ == "__main__":
    main()