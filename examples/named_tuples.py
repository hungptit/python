import namedtuple

Point = namedtuple('Point', ['x', 'y'])
x = Point(1, 2)
x = Point(x=1, y=22)

values = (1, 2)
y = Point(*values)

dict = {'x': 1, 'y': 4}
z = Point(**dict)
