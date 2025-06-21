# mole.py

import pygame, config, random


class Mole(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(config.MOLE_SPRITES)
        self.image = pygame.transform.scale(self.image, (config.MOLE_WIDTH, config.MOLE_HEIGHT))
        self.rect = pygame.Rect(self.image.get_rect())
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = (300 + self.rect.w/2), (250+ self.rect.h/2)
        self.move = 1
        self.smushed = False
        self.changeloc = False

        self.spawn_sound = pygame.mixer.Sound(config.MOLE_SPAWN_SOUND)

    # update mole
    def update(self):
        if self.smushed:
            self._ow()
        else:
            self._fine()

    # random spawn locations
    def _fine(self):
        randomx = [100, 300, 500]
        randomy = [100, 250, 400]
        spawn_interval = range(1, 1000)
        if random.choice(spawn_interval) > 980:
            self.changeloc = True
            self.rect.x = random.choice(randomx) + self.rect.w/2
            self.rect.y = random.choice(randomy) + self.rect.h/2
            self.spawn_sound.play()
        else:
            self.changeloc = False


    # visuals for mole contact
    def _ow(self):
        self.image = pygame.image.load(config.MOLE_SPRITES_OW)
        self.image = pygame.transform.scale(self.image, (config.MOLE_WIDTH, config.MOLE_HEIGHT))

    def smack(self):
        if not self.smushed:
            self.smushed = True
            self.original = self.image