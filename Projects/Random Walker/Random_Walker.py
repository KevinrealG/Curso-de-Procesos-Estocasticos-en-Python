import random
import matplotlib.pyplot as plt

class Walker:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.path_x = [x]
        self.path_y = [y]

    def step(self):
        choice = random.randint(0, 3)

        if choice == 0:
            self.x += 1
        elif choice == 1:
            self.x -= 1
        elif choice == 2:
            self.y += 1
        else:
            self.y -= 1

        self.path_x.append(self.x)
        self.path_y.append(self.y)

walker = Walker()

for _ in range(1000):
    walker.step()