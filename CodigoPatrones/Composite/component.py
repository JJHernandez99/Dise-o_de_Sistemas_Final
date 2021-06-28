from abc import abstractmethod
class Expression():
    '''Clase con sus respectivos metodos abstractos'''
    @abstractmethod
    def add(self, child):
        pass

    @abstractmethod
    def remove(self,child):
        pass

    @abstractmethod
    def showDetails(self):
        pass 