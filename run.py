import time

a = 2


def start():
    # Storyline prompts
    print("\n WELCOME TO GRANNY'S GARDEN\n")
    print("\n Granny was in the garden picking apples....")
    time.sleep(a)
    print("\n when the wicked witch from across the mountain kidnapped her!")
    time.sleep(a)
    print("\n Granny needs to be rescued...")
    time.sleep(a)
    print("\n DO YOU WANT TO SAVE GRANNY? (y or n) ")
    # convert the player's input to lower_case
    answer = input(">").lower()
    if answer == "y":
        # take player to cross_roads
        cross_roads()
    elif answer == "n":
        # take player to play_again()
        print("\n Sorry to see you go")
        print("\n Granny hopes you will be back to rescue her")
        play_again()
    else:
        # else return player to start()
        start()


def cross_roads():
    # Storyline prompts
    print("\n Thank you for coming to Granny's rescue.")
    time.sleep(a)
    print("\n You are at a crossroad with 2 doors.")
    time.sleep(a)
    print("\n Will you take the left or right door? (L or R)")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "left" or "l" lead him to bear_den()
    if answer == "l":
        bear_den()
    # else if player typed "right" or "r" lead him to monster_den()
    elif answer == "r":
        monster_den()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            # take player to cross_roads
            cross_roads()
        elif answer == "2":
            # allow player to exit
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            # take player to play_again()
            play_again()


def bear_den():
    # Storyline prompts
    print("\n You have entered the bear's den")
    time.sleep(a)
    print("\n You see two doors.")
    time.sleep(a)
    print("\n Door 1 is guarded by a pot of honey")
    time.sleep(a)
    print("\n Door 2 is guarded by the sleeping bear")
    time.sleep(a)
    print("\n Which door will you choose to take (1 or 2)")
    print("\n 1. Door guarded by the honey jar.")
    print("\n 2. Door guarded by the sleeping bear")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" lead him to dungeon_den()
    elif answer == "2":
        dungeon_den()
    else:
        # wrong key typed user to return to bear_den() to continue or exit
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            bear_den()
        elif answer == "2":
            # allow player to exit
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            # take player to play_again()
            play_again()



def monster_den():
    # Storyline prompts
    print("\n You have entered the monster den")
    time.sleep(a)
    print("\n The monster is eating lunch...")
    time.sleep(a)
    print("\n you just have a few seconds to get through..")
    time.sleep(a)
    print("\n You see two windows.")
    time.sleep(a)
    print("\n window 1 is open but very small")
    time.sleep(a)
    print("\n Door 2 is closed but big enough for you to fit through")
    time.sleep(a)
    print("\n Which door will you choose to take (1 or 2)")
    print("\n 1. Squeeze through the small window")
    print("\n 2. Open the bigger window and comfortably slide through")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" dungeon_den()
    if answer == "1":
        dungeon_den()
    # else if player typed "2" lead him to game_over()
    elif answer == "2":
        game_over()  
    else:
        # if wrong key typed take give player option to get back to bear_den() or exit game
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            monster_den()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n Granny hopes you will return to rescue her")
            exit()
        else:
            play_again()


def dungeon_den():
    # give some prompts.
    print("\n Well done! ")
    time.sleep(a)
    print("\n You have now entered the witch's dungeon den.")
    time.sleep(a)
    print("\n Again you see two doors")
    time.sleep(a)
    print("Door 1 will lead you through a room with a sleeping snake")
    time.sleep(a)
    print("Door 2 will lead you through a room with a starving tiger")
    time.sleep(a)
    print("Which door will you choose to take (1 or 2)")
    print("1. Door leading to room with a sleeping snake.")
    print("2. Door leading to room with starving tiger")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" game_win()
    elif answer == "2":
        game_win()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            bear_den()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n You were so close to rescuing her!!!")
            exit()
        else:
            exit()


def dungeon_den():
    # give some prompts.
    print("\nWell done! You escaped the sleeping bear.")
    time.sleep(a)
    print("\n You have entered the witch's dungeon den.")
    time.sleep(a)
    print("\n Again you see two doors")
    time.sleep(a)
    print("Door 1 will lead you through a room with a sleeping snake")
    time.sleep(a)
    print("Door 2 will lead you through a room with a starving tiger")
    time.sleep(a)
    print("Which door will you choose to take (1 or 2)")
    print("1. Door leading to room with a sleeping snake.")
    print("2. Door leading to room with starving tiger")
    # convert the player's input() to lower_case
    answer = input(">").lower()
    # if player typed "1" game over()
    if answer == "1":
        game_over()
    # else if player typed "2" game_win()
    elif answer == "2":
        game_win()
    # else return to start()
    else:
        print("\n Incorrect Answer")
        print("\n To continue playing press 1 or press 2 to quit the game")
        # convert the player's input() to lower_case
        answer = input(">").lower()
        if answer == "1":
            bear_den()
        elif answer == "2":
            print("\n Sorry to see you go!")
            print("\n You almost rescued her !!! ")
            print("\n Granny really hopes you will be back soon")
            exit()
        else:
            exit()


def game_over():
    # print the "reason" in a new line (\n)
    print("\n Sorry there was nothing beyond ...")
    print("\n you fell down the cliff!")
    print("\n Game Over!")
    # ask player to play again or not by activating play_again() function
    play_again()


def game_win():
    # print the "reason" in a new line (\n)
    print("\n By the time you came into the room ..")
    print("\n ...the tiger had been starving for 2 years and died!")
    print("\n You could walk through the door..")
    print("\n And exit out into the garden where Granny was kept")
    print("\n Well done on rescuing Granny!")
    # ask player to play again or not by activating play_again() function
    play_again()


def play_again():
    print("\nDo you want to play again? (y or n)")
    # convert the player's input to lower_case
    answer = input(">").lower()
    if answer == "y":
        # take player to start()
        start()
    elif answer == "n":
        # exit() the program
        exit("\n Sorry to see you go.")
    else:
        # return to start()
        start()


# start the game
start()
