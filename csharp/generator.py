
class Generator():

    entities = []

    def __init__(self, entities):
        self.entities = entities

    def generateEntities(self):
        for entity in self.entities:
            try:
                f = open(f'{entity.className}.cs', 'a')

                try:
                    className = entity.className
                    properties = self.generateProperty(entity.propertiesNames)
                    methods = self.generateMethods(entity.methodsNames)
                    f.write('''using System;

namespace Projeto.Models
{{
    public class {0} {{
        
        // Properties
        {1}

        // Methods
        {2}

    }}
}}
                    '''.format(className, 
                                properties, 
                                methods))
                except FileExistsError:
                    print("Arquivo já existe")
                finally:
                    f.close()
            except Exception as e:
                print(e)

    def generateProperty(self, properties):
        prop = ""
        for propertyName in properties:
            text = '\n      public string {} {{ get; set; }}'
            prop += text.format(propertyName)
        return prop 

    def generateMethods(self, methods):
        method = ""
        for function in methods:
            method += "\n       public void {0}() throw new NotImplementedException();\n".format(function)
        return method
