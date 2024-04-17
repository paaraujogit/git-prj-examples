"""
Data Science - Main - paaraujo@gmail.com
  * main file *
    - execute the application
"""

from Menu_oo import Menu
from Clients_oo import Cliente

def filesNotImplemented():
    print("Ficheiros Nao Implementados")

menu = Menu()
menu.setOptions(["***** Menu Clientes *****","1: Gerir Clientes","2: Gerir Carros","3: Gerir Produtos","4: Gerir Ficheiros","5: Sair"])
menu.setMethods([0,Cliente.menu,0,0,filesNotImplemented,0])  # 0: First is message ; middle is Not implemented ; Last is Return
menu.setMsg("***** MainMenu ***** Qual a opcao?")
Cliente.init()
menu.loop()
print("Obrigado pela utilizacao!")
