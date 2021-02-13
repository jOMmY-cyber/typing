import pygame
class Keycap:
    def __init__(self, screen, left, top, width, height, text, color,font):
        self.cap = pygame.key.key_code(text)
        self.screen = screen
        self.left = left
        self.top = top
        self.width = width
        self.height = height   
        self.text = text
        self.color = color
        self.font = font
    def draw(self):
        pygame.draw.rect(self.screen,self.color, (self.left, self.top, self.width, self.height))
        char = self.font.render(self.text, False, (0,0,0))
        self.screen.blit(char, (self.left+5, self.top+2))
    def is_key(self, keys):
        return keys[self.cap]

    def active(self):
        self.color = (0,0,255)
    
    def inactive(self):
        self.color = (255,0,0)
    
    def correct(self):
        self.color = (0,255,255)