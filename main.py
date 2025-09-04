from playerattr import Player
import fight

def run():
    player1 = Player(1, 100, 100, 100)
    player2 = Player(2, 100, 100, 100)

    fight.role_and_fight(player1, player2)

if __name__ == "__main__":
    run()