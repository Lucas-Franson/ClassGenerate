

class Entity():

    className = ""
    propertiesNames = []
    methodsNames = []

    def __init__(self):
        self.setClassName()
        self.setPropertiesNames()
        self.setMethodsNames()

    def setClassName(self):
        name = input("\nName: ")
        nameTreated = self.handlePropertyName(name)
        self.className = nameTreated

    def setPropertiesNames(self):
        properties = input("\nPropriedades (separe por vírgula): ")
        for prop in properties.split(','):
            self.propertiesNames.append(self.handlePropertyName(prop))

    def setMethodsNames(self):
        methods = input("\nMétodos (separe por vírgula): ")
        for prop in methods.split(','):
            self.methodsNames.append(self.handleMethodName(prop))

    def handlePropertyName(self, name):
        result = ""
        for text in name.split(" "):
            result += text.strip().capitalize()
        return result

    def handleMethodName(self, name):
        result = ""
        for text in name.split(" "):
            result += text.strip().capitalize()
        return result[0:1].lower() + result[1:]

    def __str__(self):
        print("\n#######################################\n")
        print(f"    Classe: {self.className}")
        print(f"    Propriedades: {self.propertiesNames}")
        print(f"    Métodos: {self.methodsNames}")
        print("\n#######################################\n")

    def __repr__(self):
        return f"{self.className}()"