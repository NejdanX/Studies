class BellTower:
    def __init__(self, *args):
        self.bells_order = [i for i in args]

    def sound(self):
        for bell in self.bells_order:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells_order.append(bell)


class LittleBell:
    def sound(self):
        print('ding')


class BigBell:
    def __init__(self):
        self.s = 'ding'

    def sound(self):
        print(self.s)
        if self.s == 'ding':
            self.s = 'dong'
        else:
            self.s = 'ding'


bell_tower = BellTower()
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()
bell_tower.append(BigBell())
bell_tower.sound()