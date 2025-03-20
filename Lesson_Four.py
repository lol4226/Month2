from random import randint, choice

class GameEntity:
    def __init__(self, name, hp, damage):
        self.__name = name
        self.__hp = hp
        self.__damage = damage

    @property
    def name(self):
        return self.__name
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, value):
        if type(value) == int:
            self.__hp = value
        else:
            raise ValueError("Wrong Type for hp, need int")
    
    @property
    def damage(self):
        return self.__hp
    
    @damage.setter
    def damage(self, value):
        if type(value) == int:
            self.__damage = value
        else:
            raise ValueError("Wrong Type for damage, need int")
        
    def __str__(self):
        return f"{self.__name}, health: {self.__hp}, damage: {self.__damage}"
    
class Boss(GameEntity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes_list):
        pass 
    
    def attack(self, heroes_list):
        for hero in heroes_list:
            hero.health -= self.damage

    def __str__(self):
        return "Boss " + super().__str__() + f", defence: {self.__defence}"
    
class Hero(GameEntity):
    def __init__(self, name, hp, damage, ability):
        super().__init__(name, hp, damage)
        self.__ability = ability
    
    @property
    def ability(self):
        return self.__ability
    
    def apply_super_power(self, boss, heroes_list):
        pass

    def attack(self, boss):
        boss.health -= self.damage

class Warrior(Hero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage, "CRITICAL_DAMAGE")

    def apply_super_power(self, boss, heroes_list):
        pass

class Magic(Hero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage, "BOOST")

    def apply_super_power(self, boss, heroes_list):
        pass

class Berserk(Hero):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage, "BLOCK_DAMAGE")

def start_game():
    boss = Boss("Minotovr", 2000, 50)
    warrior_one = Warrior("Asterix", 290, 20)
    warrior_two = Warrior("Abelix", 280, 25)
    magic = Magic("Aice", 270, 5)