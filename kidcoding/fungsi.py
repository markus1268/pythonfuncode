import math

def circle_area(r):
    area = math.pi * r * r
    return area

list_radius = [3, 5, 7, 9, 10, 15, 17, 20, 30, 55, 75, 125]
for radius in list_radius:
    print('Luas lingkaran dengan radius {} : {:.2f}'.format(radius, circle_area(radius)))

