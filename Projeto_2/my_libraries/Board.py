from my_libraries.Shapes import *


class CartesianBoard:

    def __init__(self):
        self.shapes = {}

    def insertShape(self, shape):
        name = shape.getType() + str(shape.getNumber())
        self.shapes[name] = shape
        print(f'\n({name}) foi adicionado ao plano cartesiano.')

    def removeShape(self, shape):
        name = shape.getType() + str(shape.getNumber())
        del self.shapes[name]
        print(f'\n({name}) foi removido do plano cartesiano.')

    def showShapes(self):
        print('\n\nEste plano cartesiano possui as seguintes formas:')
        for shape in self.shapes.keys():
            print(f'* {shape}')

    def printDetails(self):
        global aux
        print('\n\nDetalhes de cada forma:')
        for key in self.shapes.keys():
            self.shapes[key].details()

    def verifyCollision(self, shape1, shape2):
        name1 = shape1.getType() + str(shape1.getNumber())
        name2 = shape2.getType() + str(shape2.getNumber())
        # print('\n\n')
        if shape1.getType() == 'Ponto ' and shape2.getType() == 'Ponto ':
            if shape1.calcLength(shape2.x, shape2.y) == 0:
                print(f'({name1}) está colidindo com ({name2})')
            else:
                print(f'Não há colisão entre ({name1}) e ({name2})')

        if shape1.getType == 'Ponto ' and shape2.getType == 'Linha ':
            print(shape2.collisionLine(shape1.x, shape1.y))
            if shape2.collisionLine(shape1.x, shape1.y):
                print(f'({name1}) está colidindo com {name2}')

        # if shape1.getType == 'Linha ' and shape2.getType == 'Ponto ':
        #     if shape1.collisionLine(shape2.x, shape2.y) == 0:
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')

        # if shape1.getType == 'Ponto ' and shape2.getType == 'Círculo ':
        #     if shape1.calcLength(shape2.x, shape2.y) == 0:
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')
        #
        # if shape1.getType == 'Círculo ' and shape2.getType == 'Ponto ':
        #     if shape2.calcLength(shape1.x, shape1.y) == 0:
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')
        #
        # if shape1.getType == 'Linha ' and shape2.getType == 'Linha ':
        #     if shape1.calcLength(shape2.x, shape2.y) == 0:
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')
        #
        # if shape1.getType == 'Linha ' and shape2.getType == 'Círculo ':
        #     if :
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')
        #
        # if shape1.getType == 'Círculo ' and shape2.getType == 'Linha ':
        #     if :
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')
        #
        # if shape1.getType == 'Círculo ' and shape2.getType == 'Círculo ':
        #     if :
        #         print(f'({name1}) está colidindo com ({name2})')
        #     else:
        #         print(f'Não há colisão entre ({name1}) e ({name2})')



    # def collisions(self):
    #     print('\n\nColisões:')
    #     for i in self.shapes.keys():
    #         for j in self.shapes.keys():
    #             if self.shapes[i] == self.shapes[j]:
    #                 aux = i
    #             if self.shapes[aux] != self.shapes[j]:
    #                 if self.verifyCollision(self.shapes[aux], self.shapes[j]):
    #                     shape1 = self.shapes[i].getType() + str(self.shapes[i].getNumber())
    #                     shape2 = self.shapes[j].getType() + str(self.shapes[j].getNumber())
    #                     print(f'({shape1}) está colidindo com ({shape2})')