'''

'''
import random
from collections import defaultdict


class Wendy65:
    def __init__(self):
        self.x = 0
        self.y = 3

    actions = ["up", "down", "right", "left"]

    def terminal(self):
        if self.x == 7 and self.y == 3:
            return True
        else:
            return False

    def transition(self, action):
        if 2 < self.x < 6 or self.x == 8:
            self.y += 1
        elif self.x == 6 or self.x == 7:
            self.y += 2

        if action == "up":
            self.y += 1
        elif action == "down":
            self.y -= 1
        elif action == "right":
            self.x += 1
        else:
            self.x -= 1

        if self.x > 9:
            self.x = 9
        elif self.y > 6:
            self.y = 6
        elif self.x < 0:
            self.x = 0
        elif self.y < 0:
            self.y = 0

        return -1


class Wendy69:
    def __init__(self):
        self.x = 0
        self.y = 3

    actions = ["up", "down", "right", "left", "upright", "upleft", "downright",
               "downleft"]

    def terminal(self):
        if self.x == 7 and self.y == 3:
            return True
        else:
            return False

    def transition(self, action):
        if 2 < self.x < 6 or self.x == 8:
            self.y += 1
        elif self.x == 6 or self.x == 7:
            self.y += 2

        if action == "up":
            self.y += 1
        elif action == "down":
            self.y -= 1
        elif action == "right":
            self.x += 1
        elif action == "left":
            self.x -= 1
        elif action == "upright":
            self.x += 1
            self.y += 1
        elif action == "upleft":
            self.x -= 1
            self.y += 1
        elif action == "downright":
            self.x += 1
            self.y -= 1
        else:
            self.x -= 1
            self.y -= 1

        if self.x > 9:
            self.x = 9
        elif self.x < 0:
            self.x = 0
        if self.y > 6:
            self.y = 6
        elif self.y < 0:
            self.y = 0

        return -1


class Wendy610:
    def __init__(self):
        self.x = 0
        self.y = 3

    actions = ["up", "down", "right", "left", "upright", "upleft", "downright",
               "downleft"]

    def terminal(self):
        if self.x == 7 and self.y == 3:
            return True
        else:
            return False

    def transition(self, action):
        rnd = random.random()
        if rnd < 1/3:
            self.y -= 1
        elif rnd < 2/3:
            self.y += 1

        if 2 < self.x < 6 or self.x == 8:
            self.y += 1
        elif self.x == 6 or self.x == 7:
            self.y += 2

        if action == "up":
            self.y += 1
        elif action == "down":
            self.y -= 1
        elif action == "right":
            self.x += 1
        elif action == "left":
            self.x -= 1
        elif action == "upright":
            self.x += 1
            self.y += 1
        elif action == "upleft":
            self.x -= 1
            self.y += 1
        elif action == "downright":
            self.x += 1
            self.y -= 1
        else:
            self.x -= 1
            self.y -= 1

        if self.x > 9:
            self.x = 9
        elif self.x < 0:
            self.x = 0
        if self.y > 6:
            self.y = 6
        elif self.y < 0:
            self.y = 0

        return -1


def Salsa(episodes, gamma, Wendy):
    q = defaultdict(float)

    for ep in range(episodes):
        wendy = Wendy()
        s = wendy.x, wendy.y
        a = random.choice(wendy.actions) if random.random() < 0.1 else max(
                wendy.actions, key=lambda x: q[(s, x)])
        while not wendy.terminal():
            r = wendy.transition(a)
            primas = wendy.x, wendy.y
            prima = random.choice(wendy.actions) if random.random() < 0.1 \
                else max(wendy.actions, key=lambda x: q[(primas, x)])
            q[(s, a)] = q[(s, a)] + 0.5 * (r + gamma*q[(primas, prima)] -
                                           q[(s, a)])
            s, a = primas, prima
    return [((x, y), max(wendy.actions, key=lambda a: q[((x, y), a)]))
            for x in range(10) for y in range(7)]


print(Salsa("Ejercicio 6.5", 1000, 0.3, Wendy65))
print(Salsa("Ejercicio 6.9", 1000, 0.3, Wendy69))
print(Salsa("Ejercicio 6.10", 1000, 0.3, Wendy610))
