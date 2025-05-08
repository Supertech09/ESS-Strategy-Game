import pygame as pygame
import matplotlib as mpl
import pyglet as pyglet
import Include as include
import time
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
GameInit = include.GameInit()
GameDisplay = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
Player1 = include.Player("Enviroment", 1)
Player2 = include.Player("Industry", 2)
testfont = pygame.font.SysFont('Monospaced', 25, ( 0, 0, 0))
bg_image = pygame.image.load('Background Test.png')
bg_image = pygame.transform.scale(bg_image, (1000, 750))
TurnNumber = include.TurnNumber  # Ensure TurnNumber is a callable function or class
Turn = include.Turn  # Ensure Turn is a callable function or class
TurnCounter = include.TurnCounter()  # Ensure TurnCounter is a callable function or class

GameInit # type: ignore
while(True):
    GameDisplay.blit(bg_image, (0, 0))
    Player1Display = testfont.render( "You: %a" %Player1.Team, False, (0, 0, 0))
    Player2Display = testfont.render("Player 2: %a" %Player2.Team, False, (0, 0, 0))
    TurnDisplay = testfont.render("Turn: %a" %Turn, False, (0, 0, 0))
    GameDisplay.blit(Player1Display, (10, 250))
    GameDisplay.blit(Player2Display, (10, 300))
    pygame.display.update()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                print("Left mouse button clicked at", event.pos)
            elif event.button == 3:  # Right mouse button
                print("Right mouse button clicked at", event.pos)
    GameDisplay.fill((255,255,255))
    time.sleep(100)
    TurnCounter() # type: ignore


