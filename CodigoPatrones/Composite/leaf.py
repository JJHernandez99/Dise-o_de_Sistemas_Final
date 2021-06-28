class Leaf():
    '''Clase que representa objetos en la parte inferior o hoja del arbol'''
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)