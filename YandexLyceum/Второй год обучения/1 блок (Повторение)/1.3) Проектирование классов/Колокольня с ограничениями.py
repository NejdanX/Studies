class BellTower:
    def __init__(self, *args):
        self.bells_order = [i for i in args]

    def sound(self):
        for bell in self.bells_order:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells_order.append(bell)

    def print_info(self):
        for i in range(len(self.bells_order)):
            print(f'{i + 1} {self.bells_order[i].__class__.__name__}')
            self.bells_order[i].print_info()
        print()


class Bell:
    def __init__(self, *args, **kwargs):
        self.kwargs_param = sorted([str(key + ': ' + value) for key, value in kwargs.items()])
        self.args_param = list(args)

    def print_info(self):
        print(*self.kwargs_param, sep=', ', end='')
        if self.kwargs_param and self.args_param:
            print('; ', end='')
        print(*self.args_param, sep=', ', end='')
        if not self.kwargs_param and not self.args_param:
            print('-', end='')
        print()


class LittleBell(Bell):
    def sound(self):
        print('ding')


class BigBell(Bell):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s = 'ding'

    def sound(self):
        print(self.s)
        if self.s == 'ding':
            self.s = 'dong'
        else:
            self.s = 'ding'


class SizedBellTower(BellTower):
    def __init__(self, *args, size=10):
        self.size = size
        while len(args) > size:
            args = args[1:]
        super().__init__(*args)

    def print_info(self):
        super().print_info()

    def append(self, bell):
        self.bells_order.append(bell)
        if len(self.bells_order) > self.size:
            self.bells_order = self.bells_order[1:]


class TypedBellTower(BellTower):
    def __init__(self, *args, bell_type=LittleBell):
        super().__init__(*(bell for bell in args if type(bell) == bell_type))
        self.bell_type = bell_type

    def append(self, bell):
        if type(bell) == self.bell_type:
            super().append(bell)


bells = [BigBell(), BigBell("медный"), BigBell(цвет="серебристый"), BigBell("звонкий", диаметр="5 см"), BigBell("ля"),
         LittleBell("звонкий"), LittleBell(нота="до"), LittleBell(),
         LittleBell("тихий", "мелодичный", вес="100 грамм", нота="ре"), LittleBell()]
bt = BellTower(*bells)
sbt_default = SizedBellTower(*bells)
sbt_1 = SizedBellTower(*bells, size=1)
sbt_2 = SizedBellTower(*bells, size=2)
sbt_10 = SizedBellTower(*bells, size=10)
sbt_15 = SizedBellTower(*bells, size=15)
sbt_25 = SizedBellTower(*bells, size=25)
tbt_1 = TypedBellTower()
tbt_2 = TypedBellTower(bell_type=LittleBell)
tbt_3 = TypedBellTower(bell_type=BigBell)
bts = [bt, tbt_1, tbt_2, tbt_3, sbt_default, sbt_1, sbt_2, sbt_10, sbt_15, sbt_25]

new_bells = [LittleBell("на верёвочке", "с бантиком", "не звонит", "пластмассовый"),
             BigBell(вес="200 г", диаметр="7 см", цвет="красный", металл="медь"),
             BigBell("медный", нота="фа"),
             LittleBell("тихий" "с бантиком", "мелодичный", вес="100 грамм", нота="ре"),
             BigBell(цвет="серебристый"),
             LittleBell(),
             LittleBell("стеклянный"),
             LittleBell(вес="2 кг"),
             BigBell(),
             BigBell("на верёвочке", "с бантиком", "не звонит", "пластмассовый"),
             LittleBell(вес="200 г", диаметр="7 см", цвет="красный", металл="медь"),
             BigBell("звонкий", диаметр="5 см")]

for bt in bts:
    bt.sound()

for bt in bts:
    bt.print_info()