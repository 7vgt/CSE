class Character(object):
    def __init__(self, name, move, inventory, abilities, health, status, physique, description, take_damage,
                 eat):
        self.name = name
        self.move = move
        self.inventory = inventory
        self.abilities = abilities
        self.health = 100
        self.status = status
        self.physique = physique
        self.description = description
        self.eat = eat
        self.take_damage = health -1



    def talk_to_person(self):
        if self.talk:
            self.talk = True
            print("Hi how are you")
        else:
            print("No response")


    def interaction(self):
        if self.interaction:
            self.interaction = True
            print("You: how are you")
            print("Random: Oh... good... bye")


    def attack_punch(self):
        if self.attack_punch:
            self.attack_punch = False
            print("You thought")
            attack = self.health - 1


My_Character = Character('Drew', None, ["Diamond sword,64 stone blocks", "64 Notch apples"], "levitation, strength"
                         "speed", 100, None, "dresses to impress", "6,6, blue eyes, bulked body,brown with blond in "
                         "hair, medium tan skin tone", -1, "god apple")


