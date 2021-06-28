class Composite():
    '''Clase que representa objetos de cualquier nivel de la jerarquia de arbol a excepcion
    del nivel inferior o de la hoja. Mantiene al objeto hijo agregandolos y eliminandolos de la estrucura de arbol'''

    def __init__(self, *args):

        self.position = args[0]
        self.children = []
    
    def add(self, child):
        self.children.append(child)

    def remove(self, child):
        self.children.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end="")
            child.showDetails()