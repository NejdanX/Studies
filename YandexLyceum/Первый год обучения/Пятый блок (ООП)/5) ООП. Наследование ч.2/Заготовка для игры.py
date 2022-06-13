class Weapon:
    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.is_alive():
            if (self.range ** 2 >= (target.pos_x - actor.pos_x) ** 2 +
                    (target.pos_y - actor.pos_y) ** 2):
                print(f'Врагу нанесен урон оружием {self.name} в размере {self.damage}')
                target.hp -= self.damage
            else:
                print(f'Враг слишком далеко для оружия {self.name}')
        else:
            print('Враг уже повержен')

    def __str__(self):
        return self.name


class BaseCharacter:
    def __init__(self, x, y, hp):
        self.pos_x = x
        self.pos_y = y
        self.hp = hp

    def move(self, delta_x, delta_y):
        self.pos_x += delta_x
        self.pos_y += delta_y

    def is_alive(self):
        return self.hp > 0

    def get_damage(self, amount):
        if self.is_alive():
            self.hp -= amount

    def get_coords(self):
        return self.pos_x, self.pos_y


class BaseEnemy(BaseCharacter):
    def __init__(self, pos_x, pos_y, weapon, hp):
        super().__init__(pos_x, pos_y, hp)
        self.weapon = weapon

    def hit(self, target):
        if target.__class__.__name__ == 'MainHero':
            self.weapon.hit(self, target)
        else:
            print('Могу ударить только Главного героя')

    def __str__(self):
        return f'Враг на позиции ({self.pos_x}, {self.pos_y}) с оружием {self.weapon.name}'


class MainHero(BaseCharacter):
    def __init__(self, pos_x, pos_y, name, hp):
        super().__init__(pos_x, pos_y, hp)
        self.name = name
        self.weapons = []
        self.current_weapon = 0

    def hit(self, target):
        if self.weapons:
            if target.__class__.__name__ == 'BaseEnemy':
                self.weapons[self.current_weapon].hit(self, target)
            else:
                print('Могу ударить только Врага')
        else:
            print('Я безоружен')

    def add_weapon(self, weapon):
        if weapon.__class__.__name__ == 'Weapon':
            self.weapons.append(weapon)
            print(f'Подобрал {weapon}')
        else:
            print('Это не оружие')

    def next_weapon(self):
        if len(self.weapons) == 1:
            print('У меня только одно оружие')
        elif len(self.weapons) > 1:
            self.current_weapon += 1
            if self.current_weapon == len(self.weapons):
                self.current_weapon = 0
            print(f'Сменил оружие на {self.weapons[self.current_weapon]}')
        else:
            print('Я безоружен')

    def heal(self, amount):
        self.hp += amount
        if self.hp > 200:
            self.hp = 200
        print(f'Полечился, теперь здоровья {self.hp}')
