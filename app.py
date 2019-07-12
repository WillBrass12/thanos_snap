import random
import time

players = []


def thanos():
    player_id = 1
    #  Start
    num_player = int(input("How Many Players?\n"))
    for i in range(num_player):
        names = input(str("Name " + str(player_id) + ": "))
        players.append(names)
        player_id += 1
    start = input(str("\nAre You Ready to Snap? (y/n): "))
    if start == "y":
        round_num = 1
        while len(players) > 1:
            half = int(len(players) / 2)
            die = random.sample(players, half)
            for person in die:
                players.remove(person)
            time.sleep(1)
            print("\n*snap*")
            time.sleep(1)
            if len(players) == 1:
                print("\nFinal Survivor: \n")
            else:
                print("\nSnap " + str(round_num) + " Survivors: \n")
            print("  " + ", ".join(players))
            time.sleep(2)
            round_num += 1
            if len(players) == 2:
                input("\nPress 'a' for the Last Snap: ")
            elif len(players) == 1:
                break
            else:
                input("\nPress 'a' to Snap Again: ")


thanos()
