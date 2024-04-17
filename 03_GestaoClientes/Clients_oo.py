"""
Data Science - Clients Object Oriented - paaraujo@gmail.com
  * Object Oriented Version *
    - Class Cliente
  * Uses:
    - Class Menu
"""

# Atributos Cliente - Exemplo:
"""
  id': 1,                                        -> numerico
  nome': 'Jose Reis',                            -> string
  identificacao': 1234567,                       -> numerico
  genero': 'M',                                  -> 1 Caracter: 'M' 'F'
  dataNascimento': '1990-01-31',                 -> objeto datetime.date -> str no ficheiro
  morada': 'Rua A 1, 2 Esq, 1500-000 Lisboa' }   -> string
"""

from Menu_oo import Menu
from datetime import date, datetime

format_date = "%Y-%m-%d"

class Cliente:
    clientes=[] # Static variable
    def __init__(self, id, nome, identificacao, genero, dataNascimento, morada):
        self.id=id
        self.nome=nome
        self.identificacao=identificacao
        self.genero=genero
        self.dataNascimento=dataNascimento
        self.morada=morada
    def __str__(self):
        dataNasc = self.dataNascimento      # Convert date to string
        dataNascimentoStr = dataNasc.strftime(format_date)
        retStr='-----\nid: '+str(self.id)+'\nNome: '+self.nome+'\nidentificacao: '+str(self.identificacao)
        retStr+='\ngenero: '+self.genero+'\ndataNascimento: '+dataNascimentoStr+'\nmorada: '+self.morada
        return retStr
    def show(self):
        print(str(self))
    def showMin(self):
        print(str(self.id)+":",self.nome)
     
    @staticmethod
    def findCliente(cliId):
        for cli in Cliente.clientes:
            if cli.id == cliId:
                return cli
    @staticmethod
    def mostrar():
        for cliente in Cliente.clientes:
            cliente.show()
    @staticmethod
    def adicionar():
        cliId = Menu.getIntMsg("Diga o id: ")
        cliNome = input("Diga o nome: ")
        cliIdentificacao = Menu.getIntMsg("Diga a identificacao: ")
        cliGenero = input("Diga o genero [M,F]: ")
        cliDataNascimentoStr = input("Diga a dataNascimento[AAAA-MM-DD]: ")
        # Convert string to date
        cliDataNascimento = datetime.strptime(cliDataNascimentoStr, format_date).date()
        cliMorada = input("Diga a morada: ")
        Cliente.clientes.append(Cliente(cliId,cliNome,cliIdentificacao,cliGenero,cliDataNascimento,cliMorada))
    @staticmethod
    def editar():
        for cli in Cliente.clientes:
           cli.showMin()
        cliId = int(input("Diga o id do cliente que pretende alterar: "))
        # Alterar mais algum atributo
        cliMorada = input("Diga a nova morada: ")
        Cliente.findCliente(cliId).morada = cliMorada
    @staticmethod
    def remover():
        for cli in Cliente.clientes:
           cli.showMin()
        cliId = int(input("Diga o id do cliente que pretende remover: "))
        Cliente.clientes.remove(Cliente.findCliente(cliId))
    @staticmethod
    def menu():
        Cliente.menu = Menu()
        Cliente.menu.setOptions(["----- Menu Gestao Clientes -----","1: Mostrar Clientes","2: Adicionar Cliente","3: Editar Cliente","4: Remover Cliente","5: Voltar"])
        Cliente.menu.setMethods([0,Cliente.mostrar,Cliente.adicionar,Cliente.editar,Cliente.remover,0])
        Cliente.menu.setMsg("----- ClientMenu ----- Qual a opcao?")
        Cliente.menu.once()
    @staticmethod
    def init():
        dataNasc = datetime.strptime('1990-01-31', format_date).date()
        Cliente.clientes.append(Cliente(1, 'Jose Reis', 1234567, 'M', dataNasc, 'Rua A 1, 2 Esq, 1500-000 Lisboa'))
        dataNasc = datetime.strptime('2001-05-25', format_date).date()
        Cliente.clientes.append(Cliente(2, 'Luisa Silva', 2345678, 'F', dataNasc, 'Rua B, n. 4, 1 Drt 1400-001 Lisboa'))
