import pygame

from cloneslay import  card
from cloneslay import deck
from main import *

import json

from pygame.math import Vector2
from pygame.transform import scale

from input_box import InputBox
from cloneslay.actor import Actor
from cloneslay.card import Card
from game.button import Button
from game.game import Game
from game.character import Character
from game.displayed_card import DisplayedCard

class DeckLab:
    def __init__(self):
        self.deck_lab_scene()
        self.started_cards = json.load(open("../assets/configuration_files/started_cards.json"))
        self.common_cards = json.load(open("../assets/configuration_files/common_cards.json"))
        self.uncommon_cards = json.load(open("../assets/configuration_files/uncommon_cards.json"))
        self.rare_cards = json.load(open("../assets/configuration_files/rare_cards.json"))
        self.group_cards = self.separate_cards(self.common_cards)
        self.showed_cards
        self.new_deck
        self.configuration_file = json.load(open("../assets/configuration_files/deck_lab_configuration.json"))


        def separate_cards(self, deck):
            if deck.size()<=15:
                return  deck
            counter = 0
            deck = []
            deck_part=[]
            for card in deck:
                counter +=1
                deck_part.append(card)
                if counter == 15:
                    deck.append(deck_part)
                    deck_part=[]
            return deck

        def deck_lab_scene(self):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load("assets/music2.ogg")
            # pygame.mixer.music.play(loops=-1)
            pygame.display.set_caption("Deck Lab")
            pygame.mouse.set_visible(False)
            self.screen = pygame.display.set_mode((1244, 700))
            self.background = Game.load_image("background")
            self.cursor = scale(pygame.image.load("assets/cursor/cursor.png"), (25, 25))
            self.left_button = Button(scale(pygame.image.load("assets/left_button.png"), (250, 150)),Vector2(1344, 350),"")
            self.right_button = Button(scale(pygame.image.load("assets/right_button.png"), (250, 150)),Vector2(100, 350), "")
            self.save_deck_name_button = Button(scale(pygame.image.load("assets/save_deck_name.png"), (250, 150)),Vector2(622, 70), "Save your Deck")
            Game.print_text(self.screen,"Cards: "+self.new_deck.size()+"/")

        def handle_input(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    quit()
                if event.type == pygame.MOUSEBUTTONUP and self.waiting:
                    self._handle_mouse_up()
            # when game in inconsistent state don't poll mouse
            if self.waiting:
                self._handle_mouse_over()

        def _handle_mouse_up(self):
            if self.left_button.rect.collidepoint(pygame.mouse.get_pos()):
                if self.showed_cards == self.group_cards[0]:
                    pass
                else:
                    self.showed_cards = self.group_cards[self.group_cards.find(self.showed_cards)-1]
            if self.right_button.rect.collidepoint(pygame.mouse.get_pos()):
                if self.showed_cards == self.group_cards[enumerate(self.showed_cards-1)]:
                    pass
                else:
                    self.showed_cards = self.group_cards[self.group_cards.find(self.showed_cards)+1]
            if self.save_deck_name_button.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw(InputBox.__init__(self,700,500,100,10,"Deck_name"))



        def draw_scene(self):
            self.screen.blit(self.background, (0, 0))
            if self.showed_cards:
                initial_position = int(1920 / 2 - 250 * len(self.showed_cards) / 2)
                counter = 0
                for i, card in enumerate(self.showed_cards):
                    counter+=1
                    card.draw(self.screen, Vector2(initial_position + 250 * i, 600))
            self.end_turn_button.draw(self.screen)
            self.screen.blit(self.cursor, pygame.mouse.get_pos())
            pygame.display.flip()

        def _handle_mouse_over(self):
            for card in self.active_card_deck:
                if not card.card.used and card.rect:
                    card.active = card.rect.collidepoint(pygame.mouse.get_pos())

