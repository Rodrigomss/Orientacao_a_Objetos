<<<<<<< HEAD
from my_libraries.Shapes import *
from my_libraries.Board import *

P1 = Point(1, 3, 3)

P2 = Point(2, 3, 3)

P3 = Point(3, 0, 5)

L4 = Line(4, 1, 5, 4, 2)

dashboard = CartesianBoard()
dashboard.insertShape(P1)
dashboard.insertShape(P2)
dashboard.insertShape(P3)
dashboard.insertShape(L4)

dashboard.showShapes()
dashboard.printDetails()
dashboard.verifyCollision(P1, P3)
dashboard.verifyCollision(P2, L4)

print(L4.collisionLine(P2.x, P2.y))
=======
from my_libraries.Shapes import *
from my_libraries.Board import *

P1 = Point(1, 3, 3)

P2 = Point(2, 3, 3)

P3 = Point(3, 0, 5)

L4 = Line(4, 1, 5, 4, 2)

dashboard = CartesianBoard()
dashboard.insertShape(P1)
dashboard.insertShape(P2)
dashboard.insertShape(P3)
dashboard.insertShape(L4)

dashboard.showShapes()
dashboard.printDetails()
dashboard.verifyCollision(P1, P3)
dashboard.verifyCollision(P2, L4)

print(L4.collisionLine(P2.x, P2.y))
>>>>>>> origin/main
