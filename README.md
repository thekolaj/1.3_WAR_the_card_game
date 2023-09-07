# WAR: The Card Game
1. ### Create deck of 52 cards
    - Store cards in a `list`.
    - Card rank from 2 (lowest) to Ace (highest)
    - Cards have fours suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
    - Each card represented by a `tuple` of rank and suit
    - ranks are stored as `int` of 2 to 14 for easy comparison
    - When printed out, replace `int` 11 to 14 with 'J', 'Q', 'K', 'A' using a `dictionary`

1. ### Prepare gameplay loop
    - Shuffle the deck and divide it in two.
    - Create `list` of captured cards for each player
    - Create Players with those lists
    - Create a while loop that hosts the game

1. ### Create printout for the state of play. It should contain:
    - Number of cards in the decks
    - Number of cards captured
    - Current top card of the deck.
    - Top card is the last card in deck `list`

1. ### Resolve comparisons
    - Await user input before making a comparison. Any input progresses the game.
    - Compare top card by its first `tuple` value.
        - Resolve WAR at this point later.
    - use `list.pop()` to remove top cords from decks and them to temporary list
    - `print` out the result. Who won, how many cards were taken (using `len(temp_list)`)
    - use `list.extend()` to add cards to winners captured deck

1. ### Resolve WAR scenario (equal cards)
    - During war, 3 card are removed from each deck face down
    - Remove to 4 cards (original shown + 3 face down) using list slicing
        - Handle lists with only 4 cards properly
    - `list.extend()` removed cards to a temporary holding list
    - restart comparison loop

1. ### Handle captured cards
    - At the end of every loop, check if the deck is empty
    - If empty, shuffle captured card deck and replace main deck with it
    - Replace captured with empty list
    - During a war. If deck has less than 4 cards:
        - Shuffle captured, 
        - `extend()` deck to it
        - replace deck with captured
        - create empty captured list
    
1. ### Handle Game ending
    - At the end of every loop, when checking if deck is empty
    - Check if captured cards deck is also empty
    - During war, before shuffling captured, check if both decks have at least 5 cards
    - Once triggered, `print` out the winning player and congratulate them for their "Skill".
    - End game loop
