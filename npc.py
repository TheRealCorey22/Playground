class NPC:
    def __init__(self, 
                 name: str, 
                 health: int, 
                 attack: int, 
                 defense: int):
        
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
    def display_stats(self):
        print(f"Health: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}")



bestiary = {
    'Dragon': {
        'health': 1000,
        'attack': 73,
        'defense': 56
    },
    'Skeleton': {
        'health': 10,
        'attack': 4,
        'defense': 2
    }
}