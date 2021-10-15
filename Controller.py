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
        cat = list(filter(lambda x: x.category == removedCategory, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe!')
        else:
            for i in range(len(x)):
                if x[i].category == removedCategory:
                    del x[i]
                    break
            print('Categoria removida com sucesso!')

            with open('category.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.category)
                    arq.writelines('\n')
