# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def big_bonk(self, opponent):
        pass


    # Add your shield block method here
    def shield_block(self):
        pass


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here (modifies attack function to use spells, and a damage tick of 1hp per turn for 3 turns. At which point, text appears that the spell has worn off.)
    def cast_spell(self, opponent):
        pass


    # Add life steal method here, which allows the Mage to heal for a portion of the damage dealt
    def life_steal(self, opponent):
        pass


    # Add fireball method here, which allows the Mage to deal a large amount of damage to the opponent, but at the cost of some of their own health
    def fireball(self, opponent):
        pass


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)  # Boost health and attack power

    # Add arrow shot method here (allows the Archer to attack from a distance, dealing damage without taking damage in return).The quiver # can hold a limited number of arrows, and the Archer must not attack in order to replenish their arrows.
    def arrow_shot(self, opponent):
        pass


    # Add quick shot method here (allows the Archer to attack quickly, dealing less damage but not using an arrow from the quiver)
    def quick_shot(self, opponent):
        pass


    # Add dodge method here (allows the Archer to avoid an attack, reducing damage taken by half for one turn. The Archer must not attack in order to replenish their dodge ability) 
    def dodge(self):
        pass


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=15)  # Boost health

    # Add shield block method here
    def shield_block(self):
        pass


    # Add divine retribution method here (allows the Paladin to reflect a portion of the damage taken back to the attacker, healing themselves for the same amount)
    def divine_retribution(self, opponent):
        pass


# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer - Unavailable")  # Add Archer
    print("4. Paladin - Unavailable")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        print("Archer class is not implemented yet. please try another class.")
        # Add Archer class here
        pass
    elif class_choice == '4':
        print("Paladin class is not implemented yet. please try another class.")
        # Add Paladin class here
        pass
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    


# Battle function with user menu for actions
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            # Call the special ability here
            pass  # Implement this
        elif choice == '3':
            # Call the heal method here
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()