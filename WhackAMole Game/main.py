# main.py

# setup
import pygame, config, sys, mole, player
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Whack-a-Mole")
pygame.mouse.set_visible(False)

# background
background = pygame.image.load(config.BACKGROUND_IMAGE).convert_alpha()
background = background.convert()

# text
font = pygame.font.Font(None, config.FONT_SIZE_MEDIUM)

#                    score
score = 0
scoretext = font.render(f"Score: {score}", True, config.BLACK)
scoreboard = scoretext.get_rect(x=10, y=10)

#                    instructions
text = font.render("Click the mole to score points", True, config.BLACK)
textFit = text.get_rect(centerx = background.get_width() / 2, y = 10)
background.blit(text, textFit)
restart = font.render("Press ENTER to restart", True, config.GRAY)
exitGame = font.render("or ESC to close game", True, config.GRAY)
restartRect = restart.get_rect(centerx = background.get_width()/2, y=config.SCREEN_HEIGHT-100)
exitRect = exitGame.get_rect(centerx = background.get_width()/2, y = restartRect.y + 30)

#                    timer
theTime = config.GAME_LENGTH
timerText = font.render(f"Time: {theTime}", True, config.BLACK)
timerRect = timerText.get_rect(x=670, y=10)

#                    game over
gameOver = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
gameOver.fill(config.WHITE)

overText = font.render(f"You won!  Your Score: {score}", True, config.BLACK)
overRect = overText.get_rect(centerx=background.get_width() / 2, centery= background.get_height() / 2 )
lostText = font.render(f"Time's up!  Your Score: {score}", True, config.BLACK)
lostRect = overText.get_rect(centerx=background.get_width() / 2, centery= background.get_height() / 2 )

# blit background
screen.blit(background, (0,0))
pygame.display.flip()

# game objects
whiff_sound = pygame.mixer.Sound(config.HAMMER_SOUND_MISS)
mole = mole.Mole()
hammer = player.Hammer()
all_players = pygame.sprite.RenderPlain(mole, hammer)
clock = pygame.time.Clock()

while True:
    clock.tick(config.FPS)
    keys = pygame.key.get_pressed()
    # to exit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)

        # game events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if hammer.smash(mole):
                score += config.POINTS_AWARD
                scoretext = font.render(f"Score: {score}", True, config.BLACK)

            else:
                whiff_sound.play()
        elif event.type == pygame.MOUSEBUTTONUP:
            hammer.nosmash()

        # update timer
        elif event.type == config.GAME_TIMER:
            if theTime > 0:
                theTime -= 1
                timerText = font.render(f"Time: {theTime}", True, config.BLACK)

    # lose and win conditions
    if theTime == 0:
        screen.blit(gameOver, (0, 0))
        lostText = font.render(f"Time's up!  Your Score: {score}", True, config.BLACK)
        screen.blit(lostText, lostRect)
        screen.blit(restart, restartRect)
        screen.blit(exitGame, exitRect)

        # restart game
        if keys[pygame.K_RETURN]:
            score = 0
            theTime = config.GAME_LENGTH

    elif score >= config.SCORE_GOAL:
        screen.blit(gameOver, (0, 0))
        overText = font.render(f"You Won!  Your Score: {score}", True, config.BLACK)
        screen.blit(overText, overRect)
        screen.blit(restart, restartRect)
        screen.blit(exitGame, exitRect)

        # restart game
        if keys[pygame.K_RETURN]:
            score = 0
            theTime = config.GAME_LENGTH

    # update game
    else:
        all_players.update()
        screen.blit(background, (0,0))
        all_players.draw(screen)
        screen.blit(timerText, timerRect)
        screen.blit(scoretext, scoreboard)

    pygame.display.flip()

