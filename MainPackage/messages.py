"""Messages used in the code that can or can't be used repeatedly."""


def welcome():
    """Welcoming message of the game."""
    print("BLACKJACK IN PYTHON!")
    print()

    print("┌─────────┐   ┌─────────┐")
    print("│ A       │   │ J       │")
    print("│         │   │         │")
    print("│         │   │         │")
    print("│    ♠    │   │    ♠    │")
    print("│         │   │         │")
    print("│         │   │         │")
    print("│       A │   │       J │")
    print("└─────────┘   └─────────┘")


def rules():
    """Rules of the game."""
    # title
    print("RULES OF THE GAME")
    print()

    # brief description
    print(
        "In this simplified version of a game of blackjack you will play against "
        "a computer Dealer."
    )
    print()

    # overview
    print(
        "When you start the game, you will begin with $200 and you'll need to place a "
        "bet so the computer can start dealing the cards. After that you can choose "
        "at each round to either 'Hit' to receive another card or 'Stay' to stop "
        "receiving more cards."
    )
    print()

    # quick note
    print(
        "NOTE: If you choose to 'Stay', the computer will only deal cards to itself "
        "as long as it's total value in hand is lower than 18."
    )
    print()

    # win/lose/tie conditions
    print(
        "You win a round by having the closest value in cards to the number 21, "
        "receiving double the betted amount."
    )
    print(
        "You lose if the dealer ends up with a higher value in cards than you, "
        "losing the betted amount."
    )
    print(
        "A tie can also happen if both player and dealer have the same value in "
        "cards, returning your original betted amount to you."
    )
    print()

    # value of cards
    print("The value of the cards are as follows, from lower to higher:")
    print()
    print("Two = 2")
    print("Three = 3")
    print("Four = 4")
    print("Five = 5")
    print("Six = 6")
    print("Seven = 7")
    print("Eight = 8")
    print("Nine = 9")
    print("Ten = 10")
    print("Jack = 10")
    print("Queen = 10")
    print("King = 10")
    print("Ace = 1 or 11 (depending on what is best for the player to hit 21)")
    print()

    # ask the player for input to continue the game
    input("Please, press Enter to continue! ")


def win():
    """Win message."""
    print("┌─┐   ┌─┐ ┌───────┐ ┌─┐   ┌─┐    ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌───────┐ ┌─┐ ┌─┐ ┌─┐")
    print("│ └───┘ │ │ ┌───┐ │ │ │   │ │    │ │ │ │ │ │ │ │ │ ┌───┐ │ │ │ │ │ │ │")
    print("└──┐ ┌──┘ │ │   │ │ │ │   │ │    │ │ │ │ │ │ │ │ │ │   │ │ │ │ │ │ │ │")
    print("   │ │    │ │   │ │ │ │   │ │    │ │ │ │ │ │ │ │ │ │   │ │ └─┘ └─┘ └─┘")
    print("   │ │    │ └───┘ │ │ └───┘ │    │ └─┘ └─┘ │ │ │ │ │   │ │ ┌─┐ ┌─┐ ┌─┐")
    print("   └─┘    └───────┘ └───────┘    └─────────┘ └─┘ └─┘   └─┘ └─┘ └─┘ └─┘")


def lose():
    """Lose message."""
    print("┌─┐   ┌─┐ ┌───────┐ ┌─┐   ┌─┐    ┌─┐       ┌───────┐ ┌───────┐ ┌───────┐")
    print("│ └───┘ │ │ ┌───┐ │ │ │   │ │    │ │       │ ┌───┐ │ │ ┌─────┘ │ ┌─────┘")
    print("└──┐ ┌──┘ │ │   │ │ │ │   │ │    │ │       │ │   │ │ │ └─────┐ │ └─────┐")
    print("   │ │    │ │   │ │ │ │   │ │    │ │       │ │   │ │ └─────┐ │ │ ┌─────┘")
    print("   │ │    │ └───┘ │ │ └───┘ │    │ └─────┐ │ └───┘ │ ┌─────┘ │ │ └─────┐")
    print("   └─┘    └───────┘ └───────┘    └───────┘ └───────┘ └───────┘ └───────┘")
