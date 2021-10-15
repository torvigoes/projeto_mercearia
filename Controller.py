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

            with open('category.txt', 'w') as arq:  # Reescrevendo o arquivo sem a categoria deletada
                for i in x:
                    arq.writelines(i.category)
                    arq.writelines('\n')

    def modifyCategory(self, changeCategory, changedCategory):
        x = DaoCategory.read()
        cat = list(filter(lambda x: x.category == changeCategory, x))

        if len(cat) > 0:
            changed_cats = list(filter(lambda x: x.category == changedCategory, x))
            if len(changed_cats) == 0:
                x = list(map(lambda x: Category(changedCategory) if(x.category == changeCategory) else x, x))
                print('Alteração efetuada com sucesso!')

            else:
                print('A categoria para qual deseja alterar já existe!')

        else:
            print('A categoria que deseja alterar não existe!')

        with open('category.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.category)
                arq.writelines('\n')
