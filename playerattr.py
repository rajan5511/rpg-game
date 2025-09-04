class Player:

    def __init__(self, uid, attack, defense, health):
        self.uid = uid
        self.attack = attack
        self.defense = defense
        self.health = health

    def defend(self, damage):
        if self.defense > 0:
            reduced = min(self.defense, damage)
            self.defense -= reduced
            damage -= reduced
        self.health = max(0, self.health - damage)