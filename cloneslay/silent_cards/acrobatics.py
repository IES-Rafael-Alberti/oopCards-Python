from cloneslay.card import Card
import random

class Acrobatics (Card):
    def __init__(self):
        super().__init__("Acrobatics", 1, "Skill", "Draw 3 cards.Discard 1 card", "defense.png",
                         rarity="starter")

    # activate must have 2 arguments, you can make goal optional with default: goal=None
    def activate(self, actor, goal=None):
        for i in range (0,2):
            actor.hand.add_card(random.choice(actor.deck))

        actor.hand.delete_card(random.choice(actor.hand.cards))