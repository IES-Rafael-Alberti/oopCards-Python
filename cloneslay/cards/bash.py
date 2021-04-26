from cloneslay.card import Card


class Bash(Card):
    def __init__(self):
        super().__init__("Bash", 2, "attack", "Deal 8 damage. Apply 2 Vulnerable. ", None)

    def activate(self, actor, goal):
        Card.attack(8, actor, goal)
        Card.add_vulnerable(2, goal)