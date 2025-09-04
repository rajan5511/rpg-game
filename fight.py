import random

def role_and_fight(player1, player2):
    rounds = 10
    winner = "None"
    for i in range(rounds):
        attacker = player1 if i % 2 == 0 else player2
        defender = player2 if i % 2 == 0 else player1

        if attacker.health <= 0 or defender.health <= 0:
            break
        fight(attacker, defender, i)

    winner = "None"
    if player1.health > 0 and player2.health <= 0:
        winner = "1"
    elif player2.health > 0 and player1.health <= 0:
        winner = "2"
    print("Game Over! Winner is Player {}".format(winner))

def fight(attacker, defender, stage):
    print("Round " + str(stage + 1))
    damage = random.randint(10, max(10, attacker.attack))
    if random.randint(1, 100) > 90:
        damage = int(damage * 1.2)
        print("Critical Hit by Player {}".format(attacker.uid))

    defender.defend(damage)
    if defender.health > 0:
        print("Player {}: Defense {}, Health {}".format(defender.uid, defender.defense, defender.health))
    else:
        print("Player {} Died".format(defender.uid))

    if defender.health > 0:
        damage = random.randint(1, max(1, defender.attack))
        attacker.defend(damage)
        if attacker.health > 0:
            print("Player {}: Defense {}, Health {}".format(attacker.uid, attacker.defense, attacker.health))
        else:
            print("Player {} Died".format(attacker.uid))