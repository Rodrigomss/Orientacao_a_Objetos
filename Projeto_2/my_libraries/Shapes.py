import math as m


class Point:

    def __init__(self, n, x, y):
        self.n = n
        self.x = x
        self.y = y

    def getNumber(self):
        return self.n

    def getType(self):
        return 'Ponto '

    def printCoord(self):
        print(f'\n* Ponto {self.n}:\n'
              f'     x = {self.x}\n'
              f'     y = {self.y}')

    def details(self):
        print(f'* Ponto {self.n}:')
        print(f'     Está em ({self.x}, {self.y}).')

    def calcLength(self, x2, y2):
        length = m.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2)
        return float(f'{length:.2f}')


class Line:

    def __init__(self, n, x1, y1, x2, y2):
        self.P1 = Point(0, x1, y1)
        self.P2 = Point(0, x2, y2)
        self.n = n

    def getNumber(self):
        return self.n

    def getType(self):
        return 'Linha '

    def printCoord(self):
        print(f'\n* Linha {self.n}:\n'
              f'     Ponto inicial = ({self.P1.x}, {self.P1.y})\n'
              f'     Ponto final = ({self.P2.x}, {self.P2.y})')

    def calcAngCoeff(self):  # Coeficiente angular
        a = (self.P2.y - self.P1.y) / (self.P2.x - self.P1.x)
        return a

    def calcLinCoeff(self):  # Coeficiente linear
        b = (self.P2.x * self.P1.y - self.P2.y * self.P1.x) / (self.P2.x - self.P1.x)
        return b

    def details(self):
        print(f'* Linha {self.n}:')
        print(f'     O ponto inicial está em ({self.P1.x}, {self.P1.y})'
              f' e o ponto final em ({self.P2.x}, {self.P2.y}).')
        print(f'     O comprimento é {self.P1.calcLength(self.P2.x, self.P2.y)}.')
        print(f'     A inclinação é {self.calcAngCoeff()}')
        print(f'     Corta o eixo Y em {self.calcLinCoeff()}')

    def collisionLine(self, x2, y2):
        # Equação da reta: y = a*x+b
        a = self.calcAngCoeff()
        b = self.calcLinCoeff()
        y = a * x2 + b
        if y == y2:
            return True
        else:
            return False
        # aux = y - y2
        # return aux


class Circle(Point):

    def __init__(self, n, x, y, radius):
        super().__init__(n, x, y)
        self.r = radius

    def getNumber(self):
        return self.n

    def getType(self):
        return 'Círculo '

    def calcPerimeter(self):
        """ calcula o perímetro deste círculo e mostra no terminal"""
        perimeter = 2 * m.pi * self.r
        return f'{perimeter:.2f}'

    def calcArea(self):
        """ calcula a área deste circulo e mostra no terminal"""
        area = m.pi * self.r ** 2
        return f'{area:.2f}'

    def pointIn(self, pt):
        """ Verifica se o ponto está dentro deste círculo"""
        pass

    def collision(self, x2, y2):
        """ Defina mais funções de seu interesse aqui"""
        dc = (x2 - self.x)**2 + (y2 - self.y)**2
        if dc == self.r**2:
            return True
        else:
            return False

    def printCoord(self):
        print(f'\n* Círculo {self.n}:\n     Centro em ({self.x}, {self.y}) e raio {self.r}')

    def details(self):
        print(f'* Círculo {self.n}:')
        print(f'     O ponto central está em ({self.x}, {self.y}) e o seu raio é {self.r}.')
        print(f'     O perímetro é {self.calcPerimeter()}.')
        print(f'     A área é {self.calcArea()}.')
