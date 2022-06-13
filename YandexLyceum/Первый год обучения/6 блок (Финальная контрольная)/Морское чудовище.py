class BaskingShark:
    def __init__(self, cnt_tooth, stmch_size, color):
        self.cnt_tooth = cnt_tooth
        self.stomatch_size = stmch_size
        self.color = color
        self.n_tooth = 0

    def __str__(self):
        return f'BaskingShark {self.cnt_tooth} - {self.color}'

    def eat_fish(self, amount):
        new_tooth = (self.n_tooth + amount) // 100
        self.n_tooth = (self.n_tooth + amount) % 100
        self.cnt_tooth += new_tooth

    def swallow_ships(self, ship_size):
        return ship_size > self.stomatch_size

    def gritting_its_teeth(self):
        return 'Creak' * (self.cnt_tooth // 50)

    def __eq__(self, other):
        if self.cnt_tooth == other.cnt_tooth and self.stomatch_size \
                == other.stomatch_size and len(self.color) == len(other.color) \
                and self.color == other.color:
            return True
        return False

    def __ne__(self, other):
        if self.cnt_tooth != other.cnt_tooth:
            return True
        if self.stomatch_size != other.stomatch_size:
            return True
        if len(self.color) != len(other.color):
            return True
        if self.color != other.color:
            return True
        return False

    def __lt__(self, other):
        """x < y"""
        if self.cnt_tooth < other.cnt_tooth:
            return True
        if self.cnt_tooth > other.cnt_tooth:
            return False
        if self.stomatch_size < other.stomatch_size:
            return True
        if self.stomatch_size > other.stomatch_size:
            return False
        if len(self.color) < len(other.color):
            return True
        if len(self.color) > len(other.color):
            return False
        if self.color < other.color:
            return True
        return False

    def __le__(self, other):
        return self.cnt_tooth <= other.cnt_tooth

    def __gt__(self, other):
        if self.cnt_tooth > other.cnt_tooth:
            return True
        if self.cnt_tooth < other.cnt_tooth:
            return False
        if self.stomatch_size > other.stomatch_size:
            return True
        if self.stomatch_size < other.stomatch_size:
            return False
        if len(self.color) > len(other.color):
            return True
        if len(self.color) < len(other.color):
            return False
        if self.color > other.color:
            return True
        return False

    def __ge__(self, other):
        return self.cnt_tooth >= other.cnt_tooth