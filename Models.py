from datetime import datetime


class Category:
    def __init__(self, category):
        self.category = category


class Products:
    def __init__(self, name, price, category: Category):
        self.name = name
        self.price = price
        self.category = category


class Inventory:
    def __init__(self, product: Products, quantity):
        self.product = product
        self.quantity = quantity


class Sell:
    def __init__(self, itemsSold: Products, seller, buyer, quantitySold, date=datetime.now()):
        self.itemsSold = itemsSold
        self.seller = seller
        self.buyer = buyer
        self.quantitySold = quantitySold
        self.date = date


class Provider:
    def __init__(self, nameCompany, cnpj, phoneNumber, category: Category):
        self.nameCompany = nameCompany
        self.cnpj = cnpj
        self.phoneNumber = phoneNumber
        self.category = category


class People:
    def __init__(self, nameClient, phoneClient, cpf, email, adress):
        self.nameClient = nameClient
        self.phoneClient = phoneClient
        self.cpf = cpf
        self.email = email
        self.adress = adress


class Employee(People):
    def __init__(self, clt, nameClient, phoneClient, cpf, email, adress):
        self.clt = clt
        super(Employee, self).__init__(nameClient, phoneClient, cpf, email, adress)
