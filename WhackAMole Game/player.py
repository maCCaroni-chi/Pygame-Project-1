# player.py

import pygame, config

class Hammer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.HAMMER_IMAGE)
        self.rect = pygame.Rect(self.image.get_rect())
        self.offset = (-45, -20)
        self.smashing = False
        self.sound = pygame.mixer.Sound(config.HAMMER_SOUND_HIT)

    # move hammer with mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.offset)
        if self.smashing:
            self.rect.move_ip(10, 10)

    # hammer swings down
    def smash(self, target):
        if not self.smashing:
            self.smashing = True
            hitbox  = self.rect.inflate(-10, -10)
            self.image = pygame.image.load(config.HAMMER_IMAGE_HIT)
            self.sound.play()
            return hitbox.colliderect(target.rect)

    # return hammer to normal
    def nosmash(self):
        self.smashing = False
        self.image = pygame.image.load(config.HAMMER_IMAGE)