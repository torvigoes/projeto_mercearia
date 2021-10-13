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