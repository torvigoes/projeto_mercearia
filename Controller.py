from Models import *
from DAO import *
from datetime import datetime


class ControllerCategory:
    def registerCategory(self, newCategory):
        exists = False
        x = DaoCategory.read()
        for i in x:
            if i.category == newCategory:
                exists = True

        if not exists:
            DaoCategory.save(newCategory)
            print('Categoria cadastrada com sucesso!\n')
        else:
            print('A categoria que deseja cadastrar já existe.')

    def removeCategory(self, removedCategory):
        x = DaoCategory.read()
        cat = list(filter(lambda x: x.category == removedCategory, x))  # Filtrando se existe a categoria para remover

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].category == removedCategory:
                    del x[i]  # Deletando a categoria da memória RAM
                    break
            print('Categoria removida com sucesso!')

        #TODO: COLOCAR SEM CATEGORIA NO ESTOQUE

            with open('category.txt', 'w') as arq:  # Reescrevendo o arquivo sem a categoria deletada
                for i in x:
                    arq.writelines(i.category)
                    arq.writelines('\n')

    def modifyCategory(self, changeCategory, changedCategory):
        x = DaoCategory.read()
        cat = list(filter(lambda x: x.category == changeCategory, x))  # Checando se a categoria para alteração existe

        if len(cat) > 0:
            changed_cats = list(filter(lambda x: x.category == changedCategory, x))  # Checando se a categoria para qual será alterada já existe
            if len(changed_cats) == 0:
                x = list(map(lambda x: Category(changedCategory) if(x.category == changeCategory) else x, x))  # Alterando somente a categoria desejada, para a categoria referida
                print('Alteração efetuada com sucesso!')

                #TODO: ALTERAR A CATEGORIA TAMBÉM DO ESTOQUE

            else:
                print('A categoria para qual deseja alterar já existe!')

        else:
            print('A categoria que deseja alterar não existe!')

        with open('category.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.category)
                arq.writelines('\n')

    def showCategory(self):
        category = DaoCategory.read()
        if len(category) == 0:
            print('Categoria vazia!')
        else:
            for i in category:
                print(f'Categoria: {i.category}')

class ControllerInventory:
    def registerProduct(self, name, price, category, quantity):

        x = DaoInventory.read()
        y = DaoCategory.read()

        read_category = list(filter(lambda x: x.category == category, y))  # y é o parâmetro passado para o filter, que ira checar a variável
        read_name = list(filter(lambda x: x.product.name == name, x))

        if len(read_category) > 0: #  Checando se a categoria existe
            if len(read_name) == 0:  #  Caso a categoria exista, e o produto ainda não exista
                product = Products(name, price, category)
                DaoInventory.save(product, quantity)
                print('Produto cadastrado com sucesso!')

            else:
                print('Produto já existe em estoque!')
        else:
            print('Categoria inexistente!')
