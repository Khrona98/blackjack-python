"""Main script with all the needed functionalities for the game."""

# needed import to shuffle the deck
import random

# variable to store the suits of the cards
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# variable to store the ranks of the cards
ranks = [
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
]

# dictionary to store the numeric values of each rank
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}


class Card:
    """A single card."""

    def __init__(self, suit, rank):
        """Take a given rank and suit."""
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        """Display the given card."""
        return self.rank + " of " + self.suit


class Deck:
    """Deck with all the cards."""

    def __init__(self):
        """Make a full deck of cards."""
        # empty variable that will store all the cards in a deck
        self.french_deck = []

        # for the given suit in the available suits list
        for suit in suits:
            # for the given rank in the available ranks list
            for rank in ranks:
                # create a card
                new_card = Card(suit, rank)
                # append the new card to the deck
                self.french_deck.append(new_card)

    def shuffle(self):
        """Shuffle the newly created deck with the imported random function."""
        random.shuffle(self.french_deck)

    def deal(self):
        """Deal one card."""
        return self.french_deck.pop(0)

    def __str__(self):
        """Display a full standard french deck of cards."""
        # NOTE: part of the code below must be within brackets to work properly
        return (
            "French Deck: "
            f"{', '.join([Card.__str__(cards) for cards in self.french_deck])}"
        )


class Bank:
    """Bank account of the player."""

    def __init__(self, owner):
        """Account owner and balance."""
        self.owner = owner

        # loop to verify if the player input is an integer
        while True:
            try:
                self.balance = int(
                    input(
                        "How many chips would you like to deposit? "
                        "(Recommended: 250) "
                    )
                )

                # raise an error if the threshold value is too low
                if self.balance < 20:
                    raise TypeError("Value is too low.")

            except TypeError:
                print("Sorry, the balance cannot be lower than $20.")
                print()

            except ValueError:
                print("Invalid input, plase try again!")
                print()

            else:
                break

    def deposit(self, deposit):
        """Make a deposit to the account."""
        self.balance += deposit

    def withdraw(self, withdraw):
        """Make a withdraw on the account."""
        self.balance += withdraw

    def __str__(self):
        """Bank account information."""
        return f"Owner: {self.owner}\nBalance: ${self.balance}"


class Player:
    """The person that will play the game."""

    def __init__(self):
        """Player starts with an empty hand."""
        # loop to ensure a name is given (round check is used to not reset the name)
        while True:
            self.name = input("What is the player's name? ")

            if self.name not in ("", " "):
                break

        # player's starting hand
        self.hand = []

    def add_cards(self, new_card):
        """Add a card to the player's hand."""
        # top of the deck card that will be added to the player's hand
        self.new_card = new_card

        # append the new card to the player's hand
        self.hand.append(new_card)

    def __str__(self):
        """Display information about the player."""
        # NOTE: part of the code below must be within brackets to work properly
        return (
            f"{self.name} current hand is: "
            f"{', '.join([Card.__str__(cards) for cards in self.hand])}."
        )


class Dealer(Deck):
    """Computer Dealer of the game."""

    def __init__(self):
        """Dealer starts with a full deck and empty hand."""
        # loop to ensure a name is given (round check is used to not reset the name)
        while True:
            self.name = input("What is the dealer's name? ")

            if self.name not in ("", " "):
                break

        # dealer's starting hand
        self.hand = []

        # create the deck by inheriting from the parent class
        Deck.__init__(self)

    def add_cards(self, new_card):
        """Add a card to the dealer's hand."""
        # top of the deck card that will be added to the dealer's hand
        self.new_card = new_card

        # append the new card to the dealer's hand
        self.hand.append(new_card)

    def __repr__(self):
        """Correctly print the objects inside the self.hand list."""
        pass

    def __str__(self):
        """Display information about the dealer."""
        # NOTE: part of the code below must be within brackets to work properly
        return (
            f"{self.name} current hand is: "
            f"{', '.join([Card.__str__(cards) for cards in self.hand])}."
        )
