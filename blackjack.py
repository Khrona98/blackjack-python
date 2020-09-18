"""The game logic tied together."""

from MainPackage import main_script, messages

# clears the terminal
print("\n" * 100)
# display the welcoming message
messages.welcome()
print()

# variable to determine if the game should start or not
start = "None"

# variable to determine if the game is on or not
game_on = True

# variable to store the current round
round = 0

# variable to store the threshold limit of the bank account to win the game
threshold = 0

print("Type 'help' to see the rules.")

while game_on:

    if start == "None":
        # asks the player what they want to do
        start = input("Would you like to start the game? (yes/no) ")

    # start the game
    if start.lower() in ("y", "yes"):
        print()

        # Configuration Phase:

        if round == 0:
            # create the player
            player = main_script.Player()

            # create the computer dealer (automatically creates the deck)
            dealer = main_script.Dealer()
            print()

            # create the bank account for the player asking for the intial balance
            bank = main_script.Bank(player.name)

            # account balance goal that will end the game if met
            # loop to verify if the player input is an integer
            while True:
                try:
                    threshold = int(
                        input(
                            "What's the balance goal to win the game? (Recommended "
                            f"{bank.balance * 20}) "
                        )
                    )

                    # raise an error if the threshold value is too low
                    if threshold < bank.balance * 10:
                        raise TypeError("Value is too low.")

                # warn the player that the threshold value is too low
                except TypeError:
                    print(f"Sorry, the goal cannot be lower than ${bank.balance * 10}.")
                    print()

                # warn the player that their input is invalid
                except ValueError:
                    print("Invalid input, plase try again!")
                    print()

                else:
                    print()
                    break

        # Play Phase:

        # variable to determine if the game is still going
        main_phase = True

        # variable to determine how much the player wants to bet
        bet = 0

        # list of Aces in hand
        aces_list = []

        # variable to store the value of cards in hand
        hand_value = 0

        # variable to store the value of cards with Aces in hand for the player
        player_ace_hand_val = 0

        # variable to store the value of cards with Aces in hand for the dealer
        dealer_ace_hand_val = 0

        # variable to get the player input to hit or stay
        hit_stay = "None"

        # variable to determine if someone hit a blackjack
        blackjack = False

        # variable to determine if someone hit a bust
        bust = False

        # variable to determine if a draw happened
        draw = False

        # variable to continue the game or not
        game_continue = "None"

        # shuffle the deck
        if round == 0:
            dealer.shuffle()

        # reset some needed variables and objects for the next round
        else:
            # give both the player's and dealer's hand back to the deck
            dealer.french_deck += player.hand + dealer.hand

            # shuffle the deck
            dealer.shuffle()

            # reset both the player's and dealer's hands
            player.hand = []
            dealer.hand = []

        # wish good luck on the player
        print(f"{dealer.name} shuffles the deck. The game is about to begin!")
        print("May lady luck smile your way!")
        print()

        # player input to continue to the game's main phase
        input("Press Enter to continue! ")
        print()

        # loop of the main play phase
        while main_phase:
            # cleans the terminal
            print("\n" * 100)

            # increase the round each time the main_phase loops
            round += 1

            # display the round for the player
            print(f"Round {round}")
            print()

            # display the bank account data to the player
            print(f"Bank owner: {bank.owner}")
            print(f"Current balance: {bank.balance}")
            print()

            # ask the player for a bet amount, storing it in the bet variable
            while True:
                # display a recommended amount if it is the first round
                if round == 1:
                    try:
                        bet = int(
                            input(
                                "How much would you like to bet? (Recommended: "
                                f"{int(bank.balance / 10)}) "
                            )
                        )

                    # warn the player that their input is invalid
                    except ValueError:
                        print("Invalid input, plase try again!")
                        print()

                        continue

                elif round > 1:
                    try:
                        bet = int(input("How much would you like to bet? "))

                    # warn the player that their input is invalid
                    except ValueError:
                        print("Invalid input, plase try again!")
                        print()

                        continue

                # warn the player that the bet value is too high
                if bet > bank.balance:
                    print(f"Sorry, the bet cannot be higher than ${bank.balance}.")
                    print()

                    continue

                if bet < 1:
                    print("Sorry, the bet cannot be lower than $1.")
                    print()

                    continue

                else:
                    # cleans the terminal
                    print("\n" * 100)

                    # display the round for the player
                    print(f"Round {round}")
                    print()

                    break

            # deals 2 cards if it is the beginning of a round
            while (len(player.hand) and len(dealer.hand)) < 2:
                # dealer deals a card to the player
                player.add_cards(dealer.deal())

                # dealing announce with correct grammar depending on the card
                if ("Ace" in main_script.Card.__str__(player.new_card)) or (
                    "Eight" in main_script.Card.__str__(player.new_card)
                ):
                    print(f"{dealer.name} deals an {player.new_card} to you.")

                else:
                    print(f"{dealer.name} deals a {player.new_card} to you.")

                # dealer deals a card to itself
                dealer.add_cards(dealer.deal())

                # hide the dealer's second card in hand
                if len(dealer.hand) == 2:
                    print(f"{dealer.name} deals a face down card to itself.")

                # dealing announce with correct grammar depending on the card
                elif ("Ace" in main_script.Card.__str__(dealer.new_card)) or (
                    "Eight" in main_script.Card.__str__(dealer.new_card)
                ):
                    print(f"{dealer.name} deals an {dealer.new_card} to itself.")

                else:
                    print(f"{dealer.name} deals a {dealer.new_card} to itself.")

                print()

            # otherwise deals and show hands normally
            else:
                # don't show the dealer's second card if it's hand length is < 3
                if len(dealer.hand) == 2:
                    print(
                        f"{dealer.name} current hand is: {dealer.hand[0]} and a "
                        "face down card."
                    )

                    # show first card's value in the dealers hand
                    print(f"Total card value: {dealer.hand[0].value}")
                    print()

                    # variable to compare to the player hand value
                    dealer_ace_hand_val = dealer.hand[0].value

                    # show the player's current hand
                    print(player)

                    # variable to store the value of cards in hand
                    hand_value = sum(card.value for card in player.hand)

                    # list of Aces in hand
                    aces_list = [
                        main_script.Card.__str__(card)
                        for card in player.hand
                        if "Ace" in main_script.Card.__str__(card)
                    ]

                    if len(aces_list) <= 1:
                        # variable to store the value of cards with Aces in hand
                        player_ace_hand_val = hand_value

                        if player_ace_hand_val > 21:
                            player_ace_hand_val = hand_value - (10 * (len(aces_list)))

                    elif len(aces_list) >= 2:
                        # variable to store the value of cards with Aces in hand
                        player_ace_hand_val = hand_value - (10 * (len(aces_list) - 1))

                        if player_ace_hand_val > 21:
                            player_ace_hand_val = hand_value - (10 * (len(aces_list)))

                    # show the current player hand value
                    print("Total card value: " f"{player_ace_hand_val}")
                    print()

                    if player_ace_hand_val == 21:
                        print("IT'S A BLACKJACK!")
                        print()

                        input("Press Enter to continue! ")

                        # change hit_stay to 's' so the computer deals to itself
                        # (needed, because a draw can happen with 2 blackjacks)
                        hit_stay = "s"

                # check for a blackjack or a bust
                while True:
                    if hit_stay == "None":
                        # ask the player to hit or stay
                        hit_stay = input("Choose: (Hit/Stay) ")

                    if hit_stay.lower() in ("h", "hit"):
                        # cleans the terminal
                        print("\n" * 100)

                        # display the round for the player
                        print(f"Round {round}")
                        print()

                        # dealer deals a card to the player
                        player.add_cards(dealer.deal())

                        # deal announce with correct grammar depending on the card
                        if ("Ace" in main_script.Card.__str__(player.new_card)) or (
                            "Eight" in main_script.Card.__str__(player.new_card)
                        ):
                            print(f"{dealer.name} deals an {player.new_card} to you.")

                        else:
                            print(f"{dealer.name} deals a {player.new_card} to you.")

                        print()

                        # don't show the dealer's second card if it's hand length is < 3
                        print(
                            f"{dealer.name} current hand is: {dealer.hand[0]} and "
                            "a face down card."
                        )

                        # show first card's value in the dealers hand
                        print(f"Total card value: {dealer.hand[0].value}")
                        print()

                        # show the player's current hand
                        print(player)

                        # variable to store the value of cards in hand
                        hand_value = sum(card.value for card in player.hand)

                        # list of Aces in hand
                        aces_list = [
                            main_script.Card.__str__(card)
                            for card in player.hand
                            if "Ace" in main_script.Card.__str__(card)
                        ]

                        if len(aces_list) <= 1:
                            # variable to store the value of cards with Aces in hand
                            player_ace_hand_val = hand_value

                            if player_ace_hand_val > 21:
                                player_ace_hand_val = hand_value - (
                                    10 * (len(aces_list))
                                )

                        elif len(aces_list) >= 2:
                            # variable to store the value of cards with Aces in hand
                            player_ace_hand_val = hand_value - (
                                10 * (len(aces_list) - 1)
                            )

                            if player_ace_hand_val > 21:
                                player_ace_hand_val = hand_value - (
                                    10 * (len(aces_list))
                                )

                        # print the total card value of the player
                        print("Total card value: " f"{player_ace_hand_val}")
                        print()

                        # reset hit_stay so it asks for player input every time
                        hit_stay = "None"

                        if player_ace_hand_val == 21:
                            print("IT'S A BLACKJACK!")
                            print()

                            input("Press Enter to continue! ")

                            # change hit_stay to 's' so the computer deals to itself
                            # (needed, because a draw can happen with 2 blackjacks)
                            hit_stay = "s"

                        elif player_ace_hand_val > 21:
                            print("BUST!")
                            print()

                            input("Press Enter to continue! ")

                            # cleans the terminal
                            print("\n" * 100)

                            # display the round for the player
                            print(f"Round {round}")
                            print()

                            # readjust the player balance
                            bank.balance -= bet
                            print("THE DEALER WINS THE ROUND!")
                            print()

                            # display the player's loss and new balance
                            print(f"{player.name} loses ${bet}.")
                            print(f"Your new balance is: ${bank.balance}.")
                            print()

                            break

                    elif hit_stay.lower() in ("s", "stay"):
                        while dealer_ace_hand_val < 18:
                            # cleans the terminal
                            print("\n" * 100)

                            # display the round for the player
                            print(f"Round {round}")
                            print()

                            # reveal the face down card
                            if len(dealer.hand) == 2:
                                print(f"{dealer.name} reveals the face down card.")

                                # check for an Ace
                                if (
                                    "Ace" in main_script.Card.__str__(dealer.hand[1])
                                ) or (
                                    "Eight" in main_script.Card.__str__(dealer.hand[1])
                                ):
                                    print(
                                        "It's an "
                                        f"{main_script.Card.__str__(dealer.hand[1])}"
                                    )

                                else:
                                    print(
                                        "It's a "
                                        f"{main_script.Card.__str__(dealer.hand[1])}"
                                    )

                                print()

                                # show the dealer's current hand
                                print(dealer)

                                # variable to store the value of cards in hand
                                hand_value = sum(card.value for card in dealer.hand)

                                # list of Aces in hand
                                aces_list = [
                                    main_script.Card.__str__(card)
                                    for card in dealer.hand
                                    if "Ace" in main_script.Card.__str__(card)
                                ]

                                if len(aces_list) <= 1:
                                    # variable to store value of cards with Aces in hand
                                    dealer_ace_hand_val = hand_value

                                    if dealer_ace_hand_val > 21:
                                        dealer_ace_hand_val = hand_value - (
                                            10 * (len(aces_list))
                                        )

                                elif len(aces_list) >= 2:
                                    # variable to store value of cards with Aces in hand
                                    dealer_ace_hand_val = hand_value - (
                                        10 * (len(aces_list) - 1)
                                    )

                                    if dealer_ace_hand_val > 21:
                                        dealer_ace_hand_val = hand_value - (
                                            10 * (len(aces_list))
                                        )

                                # print the total card value of the dealer
                                print("Total card value: " f"{dealer_ace_hand_val}")
                                print()

                                if dealer_ace_hand_val == 21:
                                    print("IT'S A BLACKJACK!")
                                    print()

                                # show the player's current hand
                                print(player)

                                # print the total card value of the player
                                print("Total card value: " f"{player_ace_hand_val}")
                                print()

                                if player_ace_hand_val == 21:
                                    print("IT'S A BLACKJACK!")
                                    print()

                                # asks input from the player
                                if (
                                    dealer_ace_hand_val < 18
                                    and player_ace_hand_val > dealer_ace_hand_val
                                ):
                                    input("Press Enter to continue! ")

                                else:
                                    break

                                # cleans the terminal
                                print("\n" * 100)

                                # display the round for the player
                                print(f"Round {round}")
                                print()

                            # dealer deals a card to itself
                            dealer.add_cards(dealer.deal())

                            # deal announce with correct grammar depending on the card
                            if ("Ace" in main_script.Card.__str__(dealer.new_card)) or (
                                "Eight" in main_script.Card.__str__(dealer.new_card)
                            ):
                                print(
                                    f"{dealer.name} deals an {dealer.new_card} "
                                    "to itself."
                                )

                            else:
                                print(
                                    f"{dealer.name} deals a {dealer.new_card} "
                                    "to itself."
                                )

                            print()

                            # show the dealer's current hand
                            print(dealer)

                            # variable to store the value of cards in hand
                            hand_value = sum(card.value for card in dealer.hand)

                            # list of Aces in hand
                            aces_list = [
                                main_script.Card.__str__(card)
                                for card in dealer.hand
                                if "Ace" in main_script.Card.__str__(card)
                            ]

                            if len(aces_list) <= 1:
                                # variable to store the value of cards with Aces in hand
                                dealer_ace_hand_val = hand_value

                                if dealer_ace_hand_val > 21:
                                    dealer_ace_hand_val = hand_value - (
                                        10 * (len(aces_list))
                                    )

                            elif len(aces_list) >= 2:
                                # variable to store the value of cards with Aces in hand
                                dealer_ace_hand_val = hand_value - (
                                    10 * (len(aces_list) - 1)
                                )

                                if dealer_ace_hand_val > 21:
                                    dealer_ace_hand_val = hand_value - (
                                        10 * (len(aces_list))
                                    )

                            # print the total card value of the player
                            print("Total card value: " f"{dealer_ace_hand_val}")
                            print()

                            if dealer_ace_hand_val == 21:
                                print("IT'S A BLACKJACK!")
                                print()

                                blackjack = True

                            elif dealer_ace_hand_val > 21:
                                print("BUST!")
                                print()

                                bust = True

                            # show the player's current hand
                            print(player)

                            # variable to store the value of cards in hand
                            hand_value = sum(card.value for card in player.hand)

                            # list of Aces in hand
                            aces_list = [
                                main_script.Card.__str__(card)
                                for card in player.hand
                                if "Ace" in main_script.Card.__str__(card)
                            ]

                            if len(aces_list) <= 1:
                                # variable to store the value of cards with Aces in hand
                                player_ace_hand_val = hand_value

                                if player_ace_hand_val > 21:
                                    player_ace_hand_val = hand_value - (
                                        10 * (len(aces_list))
                                    )

                            elif len(aces_list) >= 2:
                                # variable to store the value of cards with Aces in hand
                                player_ace_hand_val = hand_value - (
                                    10 * (len(aces_list) - 1)
                                )

                                if player_ace_hand_val > 21:
                                    player_ace_hand_val = hand_value - (
                                        10 * (len(aces_list))
                                    )

                            # print the total card value of the player
                            print("Total card value: " f"{player_ace_hand_val}")
                            print()

                            if player_ace_hand_val == 21:
                                print("IT'S A BLACKJACK!")
                                print()

                                blackjack = True

                            elif player_ace_hand_val > 21:
                                print("BUST!")
                                print()

                                bust = True

                            # ask for playing input
                            if dealer_ace_hand_val < 18:
                                input("Press Enter to continue! ")

                        # check for the round winner after both hands are shown
                        if (
                            player_ace_hand_val == dealer_ace_hand_val
                            and dealer_ace_hand_val >= 18
                            and dealer_ace_hand_val <= 21
                        ):
                            # readjust the player balance
                            print("DRAW!")
                            print()

                            draw = True

                            input("Press Enter to continue! ")

                            # cleans the terminal
                            print("\n" * 100)

                            # display the round for the player
                            print(f"Round {round}")
                            print()

                            # display the player's loss and new balance
                            print(f"{player.name} gets the bet back.")
                            print(f"Your balance is: ${bank.balance}.")
                            print()

                        elif (
                            player_ace_hand_val < dealer_ace_hand_val
                            and dealer_ace_hand_val <= 21
                        ):

                            input("Press Enter to continue! ")

                            # cleans the terminal
                            print("\n" * 100)

                            # display the round for the player
                            print(f"Round {round}")
                            print()

                            # readjust the player balance
                            bank.balance -= bet
                            print("THE DEALER WINS THE ROUND!")
                            print()

                            # display the player's loss and new balance
                            print(f"{player.name} loses ${bet}.")
                            print(f"Your new balance is: ${bank.balance}.")
                            print()

                        elif (
                            player_ace_hand_val > dealer_ace_hand_val
                            and dealer_ace_hand_val >= 18
                            and dealer_ace_hand_val <= 21
                        ):

                            input("Press Enter to continue! ")

                            # cleans the terminal
                            print("\n" * 100)

                            # display the round for the player
                            print(f"Round {round}")
                            print()

                            # readjust the player balance
                            bank.balance += bet * 2
                            print("THE PLAYER WINS THE ROUND!")
                            print()

                            # display the player's loss and new balance
                            print(f"{player.name} wins ${bet * 2}.")
                            print(f"Your new balance is: ${bank.balance}.")
                            print()

                        elif blackjack is True:
                            if dealer_ace_hand_val < 21 or dealer_ace_hand_val > 21:
                                input("Press Enter to continue! ")

                                # cleans the terminal
                                print("\n" * 100)

                                # display the round for the player
                                print(f"Round {round}")
                                print()

                                # readjust the player balance
                                bank.balance += bet * 2
                                print("THE PLAYER WINS THE ROUND!")
                                print()

                                # display the player's loss and new balance
                                print(f"{player.name} wins ${bet * 2}.")
                                print(f"Your new balance is: ${bank.balance}.")
                                print()

                            elif player_ace_hand_val < 21 or player_ace_hand_val > 21:
                                input("Press Enter to continue! ")

                                # cleans the terminal
                                print("\n" * 100)

                                # display the round for the player
                                print(f"Round {round}")
                                print()

                                # readjust the player balance
                                bank.balance -= bet
                                print("THE DEALER WINS THE ROUND!")
                                print()

                                # display the player's loss and new balance
                                print(f"{player.name} loses ${bet}.")
                                print(f"Your new balance is: ${bank.balance}.")
                                print()

                        elif bust is True:
                            if dealer_ace_hand_val > 21:
                                input("Press Enter to continue! ")

                                # cleans the terminal
                                print("\n" * 100)

                                # display the round for the player
                                print(f"Round {round}")
                                print()

                                # readjust the player balance
                                bank.balance += bet * 2
                                print("THE PLAYER WINS THE ROUND!")
                                print()

                                # display the player's loss and new balance
                                print(f"{player.name} wins ${bet * 2}.")
                                print(f"Your new balance is: ${bank.balance}.")
                                print()

                            elif player_ace_hand_val > 21:
                                input("Press Enter to continue! ")

                                # cleans the terminal
                                print("\n" * 100)

                                # display the round for the player
                                print(f"Round {round}")
                                print()

                                # readjust the player balance
                                bank.balance -= bet
                                print("THE DEALER WINS THE ROUND!")
                                print()

                                # display the player's loss and new balance
                                print(f"{player.name} loses ${bet}.")
                                print(f"Your new balance is: ${bank.balance}.")
                                print()

                        break

                    elif hit_stay.lower() not in ("h", "hit", "s", "stay"):
                        print("Invalid input, please try again!")
                        print()

                        # reset the variable to avoid an infinite loop
                        hit_stay = "None"

                        continue

                while True:
                    # check for the threshold to end the game
                    if bank.balance >= threshold:
                        input("Press Enter to continue! ")

                        # cleans the terminal
                        print("\n" * 100)

                        # display winning message
                        messages.win()
                        print()

                        if bank.balance == threshold:
                            print(
                                "CONGRATULATIONS, YOU HIT THE TRESHOLD OF "
                                f"${threshold} AND WON THE GAME!"
                            )
                            print()

                        elif bank.balance > threshold:
                            print(
                                "CONGRATULATIONS, YOU SURPASSED THE TRESHOLD OF "
                                f"${threshold} WITH A BALANCE OF ${bank.balance} "
                                "AND WON THE GAME!"
                            )

                        # set the continue to no, so it instantly ends the game
                        game_continue = "n"

                    elif bank.balance <= 0:
                        input("Press Enter to continue! ")

                        # cleans the terminal
                        print("\n" * 100)

                        # display losing message
                        messages.lose()
                        print()

                        if bank.balance == 0:
                            print(f"YOUR BALANCE HIT 0!")

                        # set the continue to no, so it instantly ends the game
                        game_continue = "n"

                    # check if there is already something assigned to game_continue
                    if game_continue == "None":
                        # ask the player if the game should continue or not
                        game_continue = input(
                            "Would you like to continue playing? (Yes/No) "
                        )

                    if game_continue.lower() in ("y", "yes"):
                        print("\n" * 100)
                        print(f"Round {round + 1}")

                        main_phase = False
                        break

                    elif game_continue.lower() in ("n", "no"):
                        game_on = False
                        main_phase = False
                        break

                    elif game_continue.lower() not in ("y", "yes", "n", "no"):
                        print("Invalid input, please try again!")
                        print()

                        # reset the variable to avoid an infinite loop
                        game_continue = "None"

                        continue

    # end the game
    elif start.lower() in ("n", "no"):
        game_on = False

    # show the rules
    elif start.lower() in ("h", "help"):
        # clears the terminal
        print("\n" * 100)
        messages.rules()

        # reset the variable to avoid an infinite loop
        start = "None"

        # clears the terminal
        print("\n" * 100)
        # display the welcoming message
        messages.welcome()
        print()
        print("Type 'help' to see the rules.")

    # invalid input warning
    elif start.lower() not in ("y", "yes", "n", "no", "h", "help"):
        print("Invalid input, please try again!")
        print()

        # reset the variable to avoid an infinite loop
        start = "None"

        continue
