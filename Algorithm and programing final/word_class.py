import pygame

from sideways_falling_typing_game import  active_string, font
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode([WIDTH, HEIGHT])
class Word:
    def __init__(self, text, speed, x_position, y_position):
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.speed = speed
    def draw(self):
        color = 'black'
        screen.blit(font.render(self.text, True, color), (self.x_position, self.y_position))
        active_len = len(active_string)
        if active_string == self.text[:active_len]:
            screen.blit(font.render(active_string, True, 'green'), (self.x_position, self.y_position))

    def update(self):
        self.x_position -= self.speed #the porition of the word goes from right to left by decreasing it with the speed which is random