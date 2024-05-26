class Hero:
    
    def __init__(self, name, health, deffense, damage):
        self.name = name
        self.health = health
        self.deffense = deffense
        self.damage = damage
    
    def get_status(self):
        print(f'Статус героя {self.name}:')
        print(f'Здоровье: {self.health}')
        print(f'Уровень защиты: {self.deffense}')
        print('Наносимый урон:', self.damage)

    def increase_deffense(self):
        if self.deffense * 1.5 <= 100:
            self.deffense *= 1.5 # self.deffense = self.deffense * 1.5
        else:
            print('Превышен лимит увеличения защиты')
    
    def attack_hero(self, enemy):
        block_damage = self.damage * enemy.deffense / 100
        final_damage = self.damage - block_damage
        enemy.health -= final_damage
        print(f'Герой {self.name} нанес удар по {enemy.name}')
        print(f'У {enemy.name} осталось {enemy.health} единиц здоровья')

        if enemy.health <= 0:
            print(f'Игра окончена. Проиграл {enemy.name}')
        
hero_1 = Hero('Саня', 300, 40, 60)
hero_2 = Hero('Олег', 260, 60, 40)

# hero_1.get_status()
# hero_2.get_status()

hero_1.increase_deffense()
# print(hero_1.deffense)

hero_1.attack_hero(hero_2)
hero_2.attack_hero(hero_1)
hero_1.attack_hero(hero_2)
hero_2.attack_hero(hero_1)
hero_2.attack_hero(hero_1)
hero_2.attack_hero(hero_1)
hero_2.attack_hero(hero_1)