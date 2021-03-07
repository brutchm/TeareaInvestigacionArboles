from CL.AVLTreeManager import AVLTreeManager
from CL.BlackRedManager import BlackRedManager
from CL.BTreeController import BTreeController
from CL.BPlusTreeController import BPlusTreeController

def addNode(controller):
    num = int(input("Digite el numero que desea añadir al arbol AVL"))
    controller.addNode(num)


def printInOrden(controller):
    print(controller.getInOrden())


def printPreOrden(controller):
    print(controller.getPreOrden())


def printPostOrden(controller):
    print(controller.getPostOrden())


def addBlackRedNode(controllerBlackRed):
    num = int(input("Digite el numero que desea añadir al arbol Rojo/Negro"))
    controllerBlackRed.insert(num)


def printBlackRed(controllerBlackRed):
    controllerBlackRed.print()

def addBTree(controllerBTree):
    num = int(input("Digite el numero que desea añadir al arbol B"))
    controllerBTree.insert_in_btree(num)

def findBTree(controllerBTree):
    num = int(input("Digite el numero que desea encontrar en el arbol B"))
    print(controllerBTree.find(num))

def deleteBTree(controllerBTree):
    num = int(input("Digite el numero que desea eliminar en el arbol B"))
    controllerBTree.delete(num)

def addBPlusTree(controllerBPlusTree):
    num = int(input("Digite el numero que desea agregar en el arbol B+"))
    print(controllerBPlusTree.insert_in_bplustree(num))

def findBPlusTree(controllerBPlusTree):
    num = int(input("Digite el numero que desea agregar en el arbol B+"))
    print(controllerBPlusTree.find(num))

def executeOption(x, controllerAVL, controllerBlackRed, controllerBTree, controllerBPlusTree):
    if x == 1:
        addNode(controllerAVL)
        return None
    if x == 2:
        printInOrden(controllerAVL)
        return None
    if x == 3:
        printPreOrden(controllerAVL)
        return None
    if x == 4:
        printPostOrden(controllerAVL)
        return None
    if x == 5:
        addBlackRedNode(controllerBlackRed)
        return None
    if x == 6:
        printBlackRed(controllerBlackRed)
        return None
    if x == 7:
        addBTree(controllerBTree)
        return None
    if x == 8:
        findBTree(controllerBTree)
        return None
    if x == 9:
        addBPlusTree(controllerBPlusTree)
        return None
    if x == 10:
        findBPlusTree(controllerBPlusTree)
        return None
    if x == 0:
        print("Gracias por usar el programa")
        return None
    print("Digite una opcion valida")


def menu():
    x = -1
    controllerAVL = AVLTreeManager()
    controllerBlackRed = BlackRedManager()
    controllerBTree = BTreeController(5)
    controllerBPlusTree = BPlusTreeController(5)

    while x != 0:
        print("                                                                                  ")
        print("**********************************************************************************")
        print("                                                                                  ")
        print("                                     Menú                                         ")
        print("                                                                                  ")
        print("************************************ AVL *****************************************")
        print("   1. Agregar Nodo AVL")
        print("   2. Imprimir In Orden AVL")
        print("   3. Imprimir Pre Orden AVL")
        print("   4. Imprimir Post Orden AVL")
        print("***************************** Black Red Tree *************************************")
        print("  5. Agregar Nodo Black Red Tree")
        print("  6. Imprimir Black Red Tree")
        print("********************************** B Tree ****************************************")
        print("  7. Agregar Nodo B Tree")
        print("  8. Encontrar número en B Tree")
        print("********************************** B+ Tree ***************************************")
        print("  9. Agregar Nodo B+ Tree")
        print("  10. Encontrar número en B+ Tree")
        print("**********************************************************************************")
        print("  0. Salir")
        print("**********************************************************************************")
        print("                                                  ")

        x = int(input("Digite el numero de opción a elegir"))

        executeOption(x, controllerAVL, controllerBlackRed, controllerBTree, controllerBPlusTree)


if __name__ == '__main__':
    menu()
