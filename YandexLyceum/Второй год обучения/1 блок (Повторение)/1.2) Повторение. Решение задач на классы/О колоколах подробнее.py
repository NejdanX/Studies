class BellTower:
    def __init__(self, *args):
        self.bells_order = [i for i in args]

    def sound(self):
        for bell in self.bells_order:
            bell.sound()
        print('...')

    def append(self, bell):
        self.bells_order.append(bell)


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



Bell("бронзовый").print_info()
LittleBell("медный", нота="ля").print_info()
BigBell(название="Корноухий", вес="1275 пудов").print_info()