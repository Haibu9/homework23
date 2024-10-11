from pprint import pprint

def check(wordB, wordL):
    b = False
    for i in range(0, len(wordB) - len(wordL)):
        x = 0
        b = False
        for j in range(0, len(wordL)):
            if wordB[i + j] == wordL[j]:
                x += 1
            else:
                x = 0
        if x == len(wordL):
            b = True
            break
    return b

class  Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __len__(self):
        len_ = len(self.name) + len(str(self.weight)) + len(self.category) + 4
        return len_

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        file2 = file.read()
        file.close()
        return file2

    def add(self, *products):
        list_ = open(self.__file_name, 'a')
        pcts = self.get_products()
        for pr in products:
            if not check(pcts, str(pr)):
                list_.write(f'{str(pr)}\n')
            else:
                print(f'Продукт {pr} уже есть в магазине')
        list_.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())