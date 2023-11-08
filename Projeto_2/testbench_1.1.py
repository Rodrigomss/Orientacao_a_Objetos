from my_libraries.Shapes import *
from my_libraries.Board import *

P1 = Point(1, 12, 54)
P1.printCoord()

C1 = Circle(2, 13, 15, 4)
C1.printCoord()

L1 = Line(3, 2, 5, 4, 7)
L1.printCoord()

dashboard = CartesianBoard()
dashboard.insertShape(P1)
dashboard.insertShape(C1)
dashboard.insertShape(L1)

dashboard.showShapes()
dashboard.printDetails()

dashboard.removeShape(P1)
dashboard.showShapes()
dashboard.printDetails()
