class Enemy:
    # basic constant for each enemy
    _HP = 0
    _ALIVE = False
    _SPEED = 0
    _X = 0
    _Y = 0

    # init
    def __init__(self, hp=_HP, alive=_ALIVE, speed=_SPEED, x=_X, y=_Y):
        self.hp = hp
        self.alive = alive
        self.speed = speed
        self.x = x
        self.y = y

    # Each Enemy can attack
    def attack(self):
        pass

    # Each Enemy can move
    def movement(self):
        pass
