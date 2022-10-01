"""EX06 - Choose your own adventure: simple RPG."""
import random
author = "730614632"


points: int = 0
turn: int = 0
# Switches
end: bool = False
final_boss: bool = False
death_check: bool = False
cheat_check: bool = False
# Player Information
player: str = ""
attack: int = 2
defense: int = 1
max_health: int = 10
current_health: int = 10
# CONSTANT VARIABLES - emojis 
DAGGER: str = "\U0001F5E1"
SHIELD: str = "\U0001F6E1"
SHOE: str = "\U0001F45E"


def greet() -> None:
    """Welcomes the player and prompts for the player's name."""
    global player
    print(("\n----------WELCOME!----------\n"))
    print("\nWelcome to [Simple Python Themed RPG].\nYour goal is to achieve the highest score possible and beat the Final Boss.\nThe decisions you make will either increase/decrease your total score or result in no changes.\n")
    player = input("What is your name?\n")


def character_selection() -> None:
    """Player selects their character's class and perks."""
    global points, attack, defense, max_health, current_health, disable_random
    select_1: bool = False
    select_2: bool = False 
    select_3: bool = False 
    print(("\n----------SELECT CLASS----------\n"))
    while select_1 is False:
        char_class: int = int(input("\nPlease choose a class.\nClass options:\n(1)Beserker (+2 attack)\n(2)Knight (+3 defense)\n(3)Monk (+8 health)\n"))
        if char_class < 1 or char_class > 3:
            print("\nPlease choose one of the listed options.")
        elif char_class == 1:
            attack += 2
            print(f"\n{player} is now a Beserker")
            select_1 = True
        elif char_class == 2:
            defense += 3
            print(f"\n{player} is now a Knight")
            select_1 = True
        else:
            max_health += 8
            current_health += 8
            print(f"\n{player} is now a Monk")
            select_1 = True
    print(("\n----------SELECT PERK----------\n"))
    while select_2 is False:
        char_perk: int = int(input("\nPerk options:\n(1)Strength Potion (+2 attack)\n(2)Jack of all trades (+1 attack, +1 defense, and +3 health)\n(3)Suspicious potion (+3 attack OR +2 defense OR +7 health)\n(4)None (+10 to total score)\n"))
        if char_perk < 1 or char_class > 4:
            print("\nPlease choose one of the listed options.")
        elif char_perk == 1:
            attack += 2
            select_2 = True
        elif char_perk == 2:
            attack += 1
            defense += 1
            max_health += 3
            current_health += 3
            select_2 = True
        elif char_perk == 3:
            rand: int = random.randint(0, 2)
            if rand == 0:
                attack += 2
            elif rand == 1:
                defense += 2
            else:
                max_health += 6
                current_health += 6
            select_2 = True
        else:
            points += 10
            select_2 = True
    print(("\n----------SELECT ADDITIONAL PERK----------\n"))
    while select_3 is False:
        char_add_perk: int = int(input("\nAdditional perk options:\n*** Note: taking any of the following perks will lower your final score by 10 or more points.\n(1)Reinforced armor (+2 defense AND -10 points)\n(2)Whetstone (+2 attack AND -15 points)\n(3)A normal rock (-10 max health, +5 attack, AND -100 points)\n*** Note: taking the rock may cause instant death.\n(4)None\n"))
        if char_add_perk < 1 or char_class > 4:
            print("\nPlease choose one of the listed options.")
        elif char_add_perk == 1:
            defense += 2
            points -= 10
            select_3 = True
        elif char_add_perk == 2:
            attack += 2
            points -= 15
            select_3 = True
        elif char_add_perk == 3:
            max_health -= 10
            current_health -= 10
            attack += 5
            points -= 100
            select_3 = True
        else:
            select_3 = True
    if current_health <= 0:
        end_sequence()


def check_stats() -> None:
    """Allows the player to check their current stats."""
    print(("\n----------PLAYER INFORMATION----------\n"))
    print(f"\nName: {player}\nAttack: {attack}\nDefense: {defense}\nHealth: {current_health}/{max_health}")
    select_1: bool = False
    while select_1 is False:
        temp: int = int(input("\nMore info?\n(1)Yes\n(2)No\n"))
        if temp < 1 or temp > 2:
            print("\nPlease choose one of the listed options.")
        elif temp == 1:
            print("\nAttack: damage = enemy defense - (\u00B12 attack)\nDefense: damage received = defense - (\u00B12 enemy attack)")
            select_1 = True
        else:
            select_1 = True


def initiate_combat(entity: str, e_attack: int, e_defense: int, e_health: int) -> bool: 
    """Begins combat between player and entity."""
    global death_check, current_health
    combat_end: bool = False
    while combat_end is False:
        defend_check: bool = False
        p_choice: int = int(input(f"\nOptions:\n(1)Attack{DAGGER} | (2)Defend{SHIELD} | (3)Run{SHOE}\n"))
        if p_choice < 1 or p_choice > 3:
            print("\nPlease choose one of the listed options.")
        elif p_choice == 1:
            print(("\n----------PLAYER'S TURN----------\n"))
            crit: int = random.randint(1, 5)
            damage: int = random.randint(attack - 2, attack + 2)
            if crit == 1:
                damage_dealt: int = round(damage * 1.2) - e_defense
                print(f"\nCritical! {player} hits {entity} for bonus ({damage}*1.2 rounded) damage!")
                print(f"{entity} blocks {e_defense} damage.")
            else:
                damage_dealt: int = damage - e_defense
                print(f"\n{player} deals {damage} damage to {entity}.")
                print(f"{entity} blocks {e_defense} damage.")
            if damage_dealt <= 0:
                print(f"{entity} takes no damage!")
            else:
                print(f"{entity} takes {damage_dealt} damage.")
                e_health -= damage_dealt
            print(f"{entity} has {e_health} health remaining.")
        elif p_choice == 2:
            print(("\n----------PLAYER'S TURN----------\n"))
            defend_check = True
            print(f"\n{player} defends!\n{entity}'s next attack will be blocked by ({defense}*1.3 rounded) damage.")
        else:
            print(("\n----------PLAYER'S TURN----------\n"))
            print(f"{player} runs away!")
            if final_boss is True:
                print(f"\n{entity} overwhelms you as you run!\n{player} takes 9999 damage.")
                death_check = True
            return False
        if e_health <= 0:
            print(f"\n{player} is victorious!")
            combat_end = True
        # Enemy Turn Below.
        if combat_end is False:
            e_crit: int = random.randint(1, 5)
            damage: int = random.randint(e_attack - 2, e_attack + 2)
            print(("\n----------ENEMY'S TURN----------\n"))
            if e_crit == 1:
                if defend_check is True:
                    defend: int = round((defense * 1.3))
                    damage_dealt: int = round(damage * 1.2) - defend
                else:
                    defend: int = defense
                    damage_dealt: int = round(damage * 1.2) - defend
                print(f"\nCritical! {entity} hits {player} for bonus ({damage}*1.2 rounded) damage!")
                print(f"{player} blocks {defend} damage.")
                if damage_dealt <= 0:
                    print(f"{player} takes no damage!")
                else:
                    current_health -= damage_dealt
                    print(f"{player} takes {damage_dealt} damage.")
                print(f"{player} has {current_health} health remaining.")
            else:
                if defend_check is True:
                    defend: int = round((defense * 1.3))
                    damage_dealt: int = damage - defend
                else:
                    defend: int = defense
                    damage_dealt: int = damage - defend
                print(f"\n{entity} deals {damage} damage to {player}.")
                print(f"{player} blocks {defend} damage.")
                if damage_dealt <= 0:
                    print(f"{player} takes no damage!")
                else:
                    current_health -= damage_dealt
                    print(f"{player} takes {damage_dealt} damage.") 
                print(f"{player} has {current_health} health remaining.")
        if current_health <= 0:
            print(f"{player}'s health has reached 0!")
            death_check = True
            return False 
    return True


def reward() -> None:
    """Rewards given after a successful encounter."""
    global attack, defense, max_health, current_health, cheat_check
    select_1: bool = False
    print(("\n----------SELECT REWARD----------\n"))
    if turn == 0:
        while select_1 is False:
            reward: int = int(input("\nPlease choose a [minor] reward:\n(1)Minor stone of attack (+2 attack AND +3 max health)\n(2)Minor stone of defense (+2 defense AND +3 max health)\n(3)Minor stone of health (+8 max health)\n"))
            if reward < 1 or reward > 3:
                print("\nPlease choose one of the listed options.")
            elif reward == 1:
                attack += 2
                max_health += 3
                current_health += 3
                select_1 = True
            elif reward == 2:
                defense += 2
                max_health += 3
                current_health += 3
                select_1 = True
            else:
                max_health += 8
                current_health += 8
                select_1 = True
    elif turn == 1:
        while select_1 is False:
            reward: int = int(input("\nPlease choose a [mediant] reward:\n(1)Orange gem (+2 attack AND +2 defense)\n(2)Purple Gem (+3 defense AND +7 max health)\n(3)Crimson gem(+4 attack))\n(4)Lemonade (Restores all health)\n"))
            if reward < 1 or reward > 4:
                print("\nPlease choose one of the listed options.")
            elif reward == 1:
                attack += 2
                defense += 2
                select_1 = True
            elif reward == 2:
                defense += 3
                max_health += 7
                current_health += 7
                select_1 = True
            elif reward == 3:
                attack += 4
                select_1 = True
            else:
                current_health = max_health
                select_1 = True
    else:
        while select_1 is False:
            reward: int = int(input("\nPlease choose a [major] reward:\n***Note: All your health will be restored before the Final Boss.\n(1)Boolean Sword (+4 attack and +5 max health OR +3 defense and +7 max health)\n(2)Apparatus of the Kernel (+2 attack, +2 defense, AND +4 max health)\n(3)Prism of balance (+6 attack AND -2 defense)\n(4)Orb of balance (+5 defense AND -2 attack)\n(5)Bag of infinite loops (+999 attack, +999 defense, AND -999 points)\n"))
            if reward < 1 or reward > 5:
                print("\nPlease choose one of the listed options.")
            elif reward == 1:
                rand: int = random.randint(0, 1)
                if rand == 0:
                    attack += 4
                    max_health += 5
                    current_health += 5
                else:
                    defense += 3
                    max_health += 7
                    current_health += 7
                select_1 = True
            elif reward == 2:
                attack += 2
                defense += 2
                max_health += 4
                current_health += 4
                select_1 = True
            elif reward == 3:
                attack += 6
                defense -= 2
                select_1 = True
            elif reward == 4:
                defense += 5
                attack -= 2
                select_1 = True
            else:
                attack += 999
                defense += 999
                cheat_check = True
                select_1 = True


def enc_1(player_points: int) -> int:
    """First encounter."""
    global points
    select_1: bool = False
    print(("\n----------A BUGGY ENCOUNTER----------\n"))
    while select_1 is False:
        choose: int = int(input(f"\n{player} encounters [byte-sized_bug]!\n(1)Fight (Success: +10 points AND reward)\n(2)Run (-10 points)\n"))
        if choose < 1 or choose > 2:
            print("\nPlease choose one of the listed options.")
        elif choose == 1:
            win: bool = initiate_combat("[byte-sized_bug]", 4, 2, 10)
            if death_check is True:
                if points < 0:
                    return round(player_points * 1.25)
                else:
                    return round(player_points * 0.75)
            if win is True:
                player_points += 10
                reward()
            else:
                player_points -= 10
            select_1 = True
        else: 
            print("\nYou've ran away! (-10 points)")
            player_points -= 10
            select_1 = True
    return player_points
    

def enc_2(player_points: int) -> int:
    """Second encounter."""
    global points
    select_1: bool = False
    print(("\n----------A SLITHERING ENCOUNTER----------\n"))
    while select_1 is False:
        choose: int = int(input(f"\n{player} encounters [snake_case]!\n(1)Fight (Success: +20 points AND reward)\n(2)Run (-10 points)\n"))
        if choose < 1 or choose > 2:
            print("\nPlease choose one of the listed options.")
        elif choose == 1:
            win: bool = initiate_combat("[snake_case]", 6, 3, 15)
            if death_check is True:
                if points < 0:
                    return round(player_points * 1.25)
                else:
                    return round(player_points * 0.75)
            if win is True:
                player_points += 20
                reward()
            else:
                player_points -= 10
            select_1 = True
        else: 
            print("\nYou've ran away! (-10 points)")
            player_points -= 10
            select_1 = True
    return player_points


def enc_3(player_points: int) -> int:
    """Third encounter."""
    global points
    select_1: bool = False
    print(("\n----------A WRONG ENCOUNTER----------\n"))
    while select_1 is False:
        choose: int = int(input(f"\n{player} encounters [boule_(plebe)ian]!\n(1)Fight (Success: +30 points AND reward)\n(2)Run (-10 points)\n"))
        if choose < 1 or choose > 2:
            print("\nPlease choose one of the listed options.")
        elif choose == 1:
            win: bool = initiate_combat("[boule_(plebe)ian]", 8, 5, 20)
            if death_check is True:
                if points < 0:
                    return round(player_points * 1.25)
                else:
                    return round(player_points * 0.75)
            if win is True:
                player_points += 30
                reward()
            else:
                player_points -= 10
            select_1 = True
        else: 
            print("\nYou've ran away! (-10 points)")
            player_points -= 10
            select_1 = True
    return player_points


def final(player_points: int) -> int:
    """Final boss encounter."""
    global points, final_boss, current_health
    print(("\n----------ENCOUNTER_ERROR----------\n"))
    print(f"\n{player}'s health has been restored.")
    current_health = max_health
    final_boss = True
    select_1: bool = False
    while select_1 is False:
        choose: int = int(input(f"\n{player} encounters Final Boss [Literal_ValueError]!\n(1)Fight (Success: +50 points)\n(2)Run\n"))
        if choose < 1 or choose > 2:
            print("\nPlease choose one of the listed options.")
        elif choose == 1:
            win: bool = initiate_combat("[Literal_ValueError]", 12, 7, 25)
            if cheat_check is True:
                player_points -= 999
            if death_check is True:
                if points < 0:
                    return round(player_points * 1.25)
                else:
                    return round(player_points * 0.75)
            if win is True:
                player_points += 50
            select_1 = True
        else: 
            print("\nYou can't run from this encounter!")
    return player_points


def end_sequence() -> None:
    """Says goodbye to the player."""
    print("\n----------GAME OVER!----------\n")
    if end is False:
        print("\nYou have perished.")
    if final_boss is True and death_check is False:
        print("\nCongratulations on beating the final boss!")
    if final_boss is True and death_check is True:
        print("\nYou have fallen to the Final Boss.\nNow you will spend the rest of your life debugging code.")
    print(f"\nI hoped that you enjoyed your experience!\nFinal Score: {points}\n")
    quit()


def main() -> None: 
    """Main gameplay loop."""
    global end, points, turn
    greet()
    character_selection()
    print("\n----------GAME START!----------\n")
    while end is False:
        print(("\n----------MENU----------\n"))
        p_choice: int = int(input("\nOptions:\n(1)Go Forward | (2)Check Stats | (3)Quit\n"))
        if p_choice < 1 or p_choice > 3:
            print("\nPlease choose one of the listed options.")
        elif p_choice == 1:
            if turn == 0:
                points = enc_1(points)
                if death_check is True:
                    end_sequence()
                turn += 1
            elif turn == 1:
                points = enc_2(points)
                if death_check is True:
                    end_sequence()
                turn += 1
            elif turn == 2:
                points = enc_3(points)
                if death_check is True:
                    end_sequence()
                turn += 1
            else:
                points = final(points)
                if death_check is True:
                    end_sequence()
                end = True
        elif p_choice == 2:
            check_stats()
        else:
            end = True
    end_sequence()


if __name__ == "__main__":
    main()