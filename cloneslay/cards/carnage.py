from cloneslay.card import Card


class Carnage(Card):
    def __init__(self):
        super().__init__("Carnage", 20, "attack", "Ethereal. Deal 20 damage.", None)

    def activate(self, actor, goal):
        Card.attack(20, actor, goal)
