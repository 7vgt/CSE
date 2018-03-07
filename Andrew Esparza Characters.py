class Character(object):
    def __init__(self, name, move, inventory, abilities, health, status, physique, description, attack, take_damage,
                 eat, regeneration, controller):
        self.name = name
        self.move = move
        self.inventory = inventory
        self.abilities = abilities
        self.health = health
        self.status = status
        self.physique = physique
        self.description = description
        self.eat = eat
        self.regeneration = regeneration
        self.take_damage = take_damage

    def talk_to_person(self):
        global yu

    def interaction(self):
        global ye

