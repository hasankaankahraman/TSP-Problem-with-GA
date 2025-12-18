import numpy as np

# Her şehrin kordinatları ve bir id'si var

class City:
    def __init__(self, x, y, id):
        self.x = x
        self.y = y
        self.id = id 

    # Öklid
    def distance(self, city):
        x_dis = abs(self.x - city.x)
        y_dis = abs(self.y - city.y)
        distance = np.sqrt((x_dis ** 2) + (y_dis ** 2))
        return distance

    def __repr__(self):
        return f"Sehir_{self.id}"