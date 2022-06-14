class Human():
    def __init__(self,first_name, last_name, hitpoints=10,strength=1,inventory=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.hitpoints = hitpoints
        self.strength = strength
        self.inventory = inventory

    def get_full_name(self):
        return(self.first_name + " " + self.last_name)

    def attack(self, target):
        target.damage(self.strength)

    def damage(self, damage):
        self.hitpoints = self.hitpoints - damage
        if self.hitpoints <= 0:
            print(self.get_full_name() + " has died")
            del self

    def pick_up_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item_index):
        self.inventory.pop(item_index)

    def use_item(self, target, item_index):
        self.inventory[item_index].use(target)
        self.inventory.pop(item_index)

    def print_inventory(self):
        for item in self.inventory:
            print(item)

    def __str__(self):
        return self.get_full_name()

class Wizard(Human):
    def __init__(self, first_name, last_name, hitpoints = 10, strength = 1, inventory = [], mana=0, spells=[]):
        super().__init__(first_name, last_name, hitpoints = hitpoints, strength = strength, inventory = inventory)
        self.mana=mana
        self.spells = spells

    def learn_spell(self, spell):
        self.spells.append()

    def cast_spell(self, targets, spell_index):
        self.spells[spell_index].cast(self,targets)

    def print_spells(self):
        for spell in self.spells:
            print(spell)

    def __str__(self):
        return self.get_full_name()


class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def use(self, target):
        pass

    def __str__(self):
        return(self.name)


class Health_Potion(Item):
    def __init__(self):
        super().__init__("Health Potion","Heal 10 hitpoints")

    def use(self, target):
        target.hitpoints = target.hitpoints+10

class Strength_Potion(Item):
    def __init__(self):
        super().__init__("Strength Potion","Increase strength by 1")

    def use(self, target):
        target.strength = target.strength+1


class Spell():
    def __init__(self, name, description, mana_cost):
        self.name = name
        self.description = description
        self.mana_cost = mana_cost

    def cast(self, caster, targets):
            pass


    def __str__(self):
        return(self.name)

class Fireball(Spell):
    def __init__(self):
        super().__init__("Fireball", "Shoot a fireball at several targets. Costs 5 mana",5)

    def cast(self, caster, targets):
        if caster.mana >= self.mana_cost:
            for target in targets:
                target.hitpoints = target.hitpoints - 5
            caster.mana = caster.mana - self.mana_cost
        else:
            print("Not enough mana")

class Heal_Zone(Spell):
    def __init__(self):
        super().__init__("Heal Zone", "Heal several targets at once. Costs 3 mana",3)

    def cast(self, caster, targets):
        if caster.mana >= self.mana_cost:
            for target in targets:
                target.hitpoints = target.hitpoints + 3
            caster.mana = caster.mana - self.mana_cost
        else:
            print("Not enough mana")

def main():
    player1 = Wizard("Harry", "Potter", hitpoints = 10, strength = 0, inventory = [Health_Potion()], mana=9, spells=[Fireball(),Heal_Zone()])
    player2 = Human("Dwayne", "Johnson", hitpoints = 100, strength = 10, inventory = [Strength_Potion(),Health_Potion(),Health_Potion()])
    player3 = Human("Mario", "Mario", hitpoints=50, strength=15, inventory=[Strength_Potion()])
    player4 = Human("Luigi", "Mario", hitpoints=40, strength=12, inventory=[Strength_Potion()])
    player5 = Human("Shopkeep", "Err", hitpoints=10, strength=1, inventory=[Health_Potion(),Strength_Potion()])


    print(player3.get_full_name() +": " + str(player3.hitpoints))
    print(player2.get_full_name() +": " + str(player2.hitpoints))
    print(player3.get_full_name() +" attacks " + player2.get_full_name())
    player3.attack(player2)
    print(player3.get_full_name() + ": " + str(player3.hitpoints))
    print(player2.get_full_name() + ": " + str(player2.hitpoints))

    print()

    print(player2.get_full_name() +" Display Inventory:")
    player2.print_inventory()

    print(player2.get_full_name() +" Picks up another Strength Poition")
    player2.pick_up_item(Strength_Potion())
    print()
    print(player2.get_full_name() + " Display Inventory:")
    player2.print_inventory()
    print()

    print(player2.get_full_name() +": " + str(player2.hitpoints))
    print(player2.get_full_name() + " Drinks Health Poition")
    player2.use_item(player2,1)
    print(player2.get_full_name() +": " + str(player2.hitpoints))
    print()

    print(player2.get_full_name() +": " + str(player2.hitpoints))
    print(player1.get_full_name() + " Gives " + player2.get_full_name() + " a Health Poition")
    player1.use_item(player2,0)
    print(player2.get_full_name() +": " + str(player2.hitpoints))
    print()

    print(player1.get_full_name() +" Spell List: ")
    player1.print_spells()
    print()

    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    print(player1.get_full_name() + " casts Fireball on everyone")
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    player1.cast_spell([player2,player3,player4,player5],0)
    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))

    print()

    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    print(player1.get_full_name() + " casts Heal Zone on everyone")
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    player1.cast_spell([player2,player3,player4,player5],1)
    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))

    print()

    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    print(player1.get_full_name() + " tries to cast Heal Zone on everyone again")
    player1.cast_spell([player2,player3,player4,player5],1)
    print(player1.get_full_name() + "'s mana: " + str(player1.mana))
    print(player2.get_full_name() + ": " + str(player2.hitpoints))
    print(player3.get_full_name() + ": " + str(player2.hitpoints))
    print(player4.get_full_name() + ": " + str(player2.hitpoints))
    print(player5.get_full_name() + ": " + str(player2.hitpoints))



if __name__ == "__main__":
    main()
