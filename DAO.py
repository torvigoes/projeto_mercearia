from Models import *


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open('category.txt', 'a') as arq:
            arq.writelines(category)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('category.txt', 'r') as arq:
            cls.category = arq.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))  # Retirando os \n e retornando uma lista

        cat = []
        for i in cls.category:
            cat.append(Category(i))  # Retornando uma instância da models

        return cat


class DaoSell:
    @classmethod
    def save(cls, sell: Sell):
        with open('sell.txt', 'a') as arq:
            arq.writelines(sell.itemsSold.name + '|' + sell.itemsSold.price + '|' +
                           sell.itemsSold.category + '|' + sell.seller + '|' + sell.buyer + '|' +
                           str(sell.quantitySold) + '|' + sell.date)  # quantitySold convertida para string, pois
            # na controller será int e sem conversão não concatenará.
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('sell.txt', 'r') as arq:
            cls.sell = arq.readlines()

        cls.sell = list(map(lambda x: x.replace('\n', ''), cls.sell))  # Aqui cada posição da lista será uma venda
        cls.sell = list(map(lambda x: x.split('|'), cls.sell))  # Criando uma lista para cada venda, ou seja,
        # uma lista dentro da lista.

        sel = []
        for i in cls.sell:
            sel.append(Sell(Products(i[0], i[1], i[2]), i[3], i[4], i[5]))  # Parâmetros de acordo com a ordem da
            # lista
        return sel


class DaoInventory:
    @classmethod
    def save(cls, product: Products, quantity):
        with open('inventory.txt', 'a') as arq:
            arq.writelines(product.name + '|' + product.price + '|' + product.category + '|' +
                           str(quantity))
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('inventory.txt', 'r') as arq:
            cls.inventory = arq.readlines()

        cls.inventory = list(map(lambda x: x.replace('\n', ''), cls.inventory))
        cls.inventory = list(map(lambda x: x.split('|'), cls.inventory))

        inv = []
        if len(cls.inventory) > 0:
            for i in cls.inventory:
                inv.append(Inventory(Products(i[0], i[1], i[2]), i[3]))

        return inv


class DaoProvider:
    @classmethod
    def save(cls, provider: Provider):
        with open('provider.txt', 'a') as arq:
            arq.writelines(provider.nameCompany + '|' + provider.cnpj + '|' + provider.phoneNumber + '|' +
                           provider.category)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('provider.txt', 'r') as arq:
            cls.provider = arq.readlines()

        cls.provider = list(map(lambda x: x.replace('\n', ''), cls.provider))
        cls.provider = list(map(lambda x: x.split('|'), cls.provider))

        provi = []
        for i in cls.provider:
            provi.append(Provider(i[0], i[1], i[2], i[3]))

        return provi


class DaoPeople:
    @classmethod
    def save(cls, people: People):
        with open('clients.txt', 'a') as arq:
            arq.writelines(people.nameClient + '|' + people.phoneClient + '|' + people.cpf + '|' + people.email + '|' +
                           people.adress)
            arq.writelines('\n')

    @classmethod
    def read(cls):
        with open('clients.txt', 'r') as arq:
            cls.people = arq.readlines()

        cls.people = list(map(lambda x: x.replace('\n', ''), cls.people))
        cls.people = list(map(lambda x: x.split('|'), cls.people))

        peop = []
        for i in cls.people:
            peop.append(People(i[0], i[1], i[2], i[3], i[4]))

        return peop


class DaoEmployee:
    @classmethod
    def save(cls, employee: Employee):
        with open('employee.txt', 'a') as arq:
            arq.writelines(employee.clt + '|' + employee.nameClient + '|' + employee.phoneClient + '|' +
                           employee.cpf + '|' + employee.email + '|' + employee.adress)
            arq.writelines('\n')

        cls.employee = list(map(lambda x: x.replace('\n', ''), cls.employee))
        cls.employee = list(map(lambda x: x.split('|'), cls.employee))

        emplo = []
        for i in cls.employee:
            emplo.append(Employee(i[0], i[1], i[2], i[3], i[4], i[5]))

        return emplo
