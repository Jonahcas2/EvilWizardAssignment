import random
# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.shielded = False
        self.spell_ticks = 0
        self.arrows = 5
        self.can_dodge = True
        self._was_cursed = False

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if hasattr(opponent, 'shielded') and opponent.shielded:
            damage = damage // 2
            opponent.shielded = False
            print(f"{opponent.name} blocks the attack! Damage reduced to {damage}.")

        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):   
        if self.health < self.max_health:
            amount = self.max_health // 2
            self.health = min(self.health + amount, self.max_health)
            print(f"{self.name} heals for {amount} health! Current health: {self.health}")
        else:
            print(f"{self.name} is already at max health!")



# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here
    def big_bonk(self, opponent):
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Big Bonk! Deals {damage} damage to {opponent.name}.")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")


    # Add your shield block method here
    def shield_block(self):
        self.shielded = True
        print(f"{self.name} is now shielded! Next incoming attack will deal half damage.")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    # Add your cast spell method here (modifies attack function to use spells, and a damage tick of 1hp per turn for 3 turns. At which point, text appears that the spell has worn off.)
    def cast_spell(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        opponent.spell_ticks = 3
        opponent._was_cursed = True
        print(f"{self.name} casts a spell for {damage} damage!")
        print(f"{opponent.name} is cursed and will take 1 damage for the next 3 turns!")


    # Add life steal method here, which allows the Mage to heal for a portion of the damage dealt
    def life_steal(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        heal_amount = damage // 2
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} drains {heal_amount} health from {opponent.name}!")


    # Add fireball method here, which allows the Mage to deal a large amount of damage to the opponent, but at the cost of some of their own health
    def fireball(self, opponent):
        damage = self.attack_power * 2
        self_damage = 10
        opponent.health -= damage
        self.health -= self_damage
        print(f"{self.name} casts Fireball! {opponent.name} takes {damage} damage. {self.name} takes {self_damage} recoil.")


# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)  # Boost health and attack power

    # Add arrow shot method here (allows the Archer to attack from a distance, dealing damage without taking damage in return).The quiver # can hold a limited number of arrows, and the Archer must not attack in order to replenish their arrows.
    def arrow_shot(self, opponent):
        if self.arrows > 0:
            self.arrows -= 1
            opponent.health -= self.attack_power
            print(f"{self.name} shoots an arrow for {self.attack_power} damage! {self.arrows} arrows left.")
        else:
            print(f"{self.name} has no arrows! Must skip a turn to replenish.")


    # Add quick shot method here (allows the Archer to attack quickly, dealing less damage but not using an arrow from the quiver)
    def quick_shot(self, opponent):
        damage = self.attack_power // 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot for {damage} damage!")


    # Add dodge method here (allows the Archer to avoid an attack, reducing damage taken by half for one turn. The Archer must not attack in order to replenish their dodge ability) 
    def dodge(self):
        pass


# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=15)  # Boost health

    # Add shield block method here
    def shield_block(self):
        self.shielded = True
        print(f"{self.name} is now shielded! Next incoming attack will deal half damage.")


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
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)
    


# Battle function with user menu for actions
def battle(player, wizard):
    turn = 1
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")
        
        choice = input("Choose an action: ")

        if choice == '1':
            if isinstance(player, Archer):
                player.arrow_shot(player, wizard)
            elif isinstance(player, Mage):
                player.cast_spell(player, wizard)
            else:
                player.attack(wizard)

        elif choice == '2':
            if isinstance(player, Warrior):
                print("1. Big Bonk")
                print("2. Shield Block")
                ability_choice = input("Choose a Warrior ability: ")
                if ability_choice == '1':
                    player.big_bonk(wizard)
                elif ability_choice == '2':
                    player.shield_block()
                else:
                    print("Invalid choice.")
            
            elif isinstance(player, Archer):
                print("1. Quick Shot")
                print("2. Dodge")
                ability_choice = input("Choose an Archer ability: ")
                if ability_choice == '1':
                    player.quick_shot(wizard)
                elif ability_choice == '2':
                    player.dodge()
                else:
                    print("Invalid choice")
            
            elif isinstance(player, Mage):
                print("1. Life Steal")
                print("2. Fireball")
                ability_choice = input("Choose a Mage ability: ")
                if ability_choice == '1':
                    player.cast_spell(wizard)
                elif ability_choice == '2':
                    player.life_steal(wizard)
                elif ability_choice == '3':
                    player.fireball(wizard)
                else:
                    print("Invalid choice.")

            elif isinstance(player, Paladin):
                print("1. Shield Block")
                print("2. Divine Retribution")
                ability_choice = input("Choose a Paladin ability: ")
                if ability_choice == '1':
                    player.shield_block()
                elif ability_choice == '2':
                    player.divine_retribution(wizard)
                else:
                    print("Invalid choice.")
            else:
                print("No special abilities available for this class.")

        elif choice == '3':
            # Call the heal method here
            pass  # Implement this
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice, try again.")
            continue
        
        for character in [player, wizard]:
            if character.spell_ticks > 0:
                character.health -= 1
                character.spell_ticks -= 1
                print(f"{character.name} suffers 1 damage from a lingering spell! ({character.spell_ticks} turns left)")
                if character.health <= 0:
                    print(f"{character.name} has been defeated!")
            
            if character.spell_ticks == 0 and hasattr(character, "_was_cursed") and character._was_cursed:
                print(f"The spell affecting {character.name} has worn off.")
                character._was_cursed = False

        # Evil Wizard's turn to attack and regenerate
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")
    
    turn += 1

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