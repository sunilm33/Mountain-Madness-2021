import pygame, sys
from pygame.locals import *
import random, time
import dimensions
#start in the middle of the screen
#jumps up and always is falling down
#tilts up and down
#with going up it goes 45 degrees
#with going down it goes 45 degrees down 


class Player(pygame.sprite.Sprite):

  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("ASSETS/YellowFish.png")
    self.surf = pygame.Surface((40,40))
    self.rect = self.surf.get_rect(center = (dimensions.SCREEN_WIDTH / 4, dimensions.SCREEN_HEIGHT / 2))
  
  def move(self, g, v):

    keyPress = pygame.key.get_pressed()
    if keyPress[K_SPACE]:
      v += g
      self.rect.centry += v
      self.rect.move_ip(0,-10)





