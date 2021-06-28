from leaf import Leaf
from composite import Composite

class Main():
    def main(self):

        topLevelcategory = Composite("Gerente General")
        subMenuItem1 = Composite("Gerente 1")
        subMenuItem2 = Composite("Gerente 2")
        subMenuItem11 = Leaf("Desarrollador 11")
        subMenuItem12 = Leaf("Desarrollador 12")
        subMenuItem21 = Leaf("Desarrollador 21")
        subMenuItem22 = Leaf("Desarrollador 22")

        subMenuItem1.add(subMenuItem11)
        subMenuItem1.add(subMenuItem12)
        subMenuItem2.add(subMenuItem21)
        subMenuItem2.add(subMenuItem22)

        topLevelcategory.add(subMenuItem1)
        topLevelcategory.add(subMenuItem2)
        topLevelcategory.showDetails()

if __name__ == "__main__":
    menu = Main()
    menu.main()