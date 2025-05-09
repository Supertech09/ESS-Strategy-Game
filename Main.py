import pygame as pygame
import matplotlib as mpl
#import Include as include
import time

from sympy import false
from sympy import true
# from Include import Player
from Include import GameInit
from Include import TurnNumber
from Include import Turn
from Include import TurnCounter

class Player:
    def __init__(self, Team, Cards, Points):
        self.Team = Team
        self.Cards = Cards
        self.Points = Points
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
GameInit = GameInit()
global Game
Game = False

GameDisplay = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
Player1 = Player("Enviroment", 1,0)
Bot = Player("Industry", 0, 0)

testfont = pygame.font.SysFont('Monospaced', 25, ( 0, 0, 0))
TitleScreen = pygame.image.load('Title Screen Layout.png')
TitleScreen = pygame.transform.scale(TitleScreen, (1000, 750))
gamesurface = pygame.image.load('Background Test.png')
gamesurface = pygame.transform.scale(gamesurface, (1000, 750))

TurnNumber = TurnNumber  # Ensure TurnNumber is a callable function or class
Turn = Turn  # Ensure Turn is a callable function or class
TurnCounter = TurnCounter  # Ensure TurnCounter is a callable function or class

teambutton = pygame.Rect(323, 298, 288, 94)  #rect for the team area
playbutton = pygame.Rect(323, 413, 288, 100) #rect for the play area
cardbutton = pygame.Rect(323, 530, 288, 100) #rect for the card area

GameInit # type: ignore
while(True):
    if Game == False:
        GameDisplay.blit(TitleScreen, (0, 0))
        pygame.display.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button.
                        # Check if the rect collides with the mouse pos.
                        if teambutton.collidepoint(event.pos):
                            print('Team Select clicked.')


                        elif playbutton.collidepoint(event.pos):
                            print('Play clicked.')
                            Game = True

                        elif cardbutton.collidepoint(event.pos):
                            print('Cards clicked.')


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
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

    
    if Game == True:
        GameDisplay.blit(gamesurface, (0, 0))
        Player1Display = testfont.render( "You: %a" %Player1.Team, False, (0, 0, 0))
        Player2Display = testfont.render("Bot: %a" %Bot.Team, False, (0, 0, 0))
        TurnDisplay = testfont.render("Turn: %a" %Turn, False, (0, 0, 0))
        GameDisplay.blit(Player1Display, (10, 250))
        GameDisplay.blit(Player2Display, (10, 300))
        GameDisplay.blit(TurnDisplay, (10, 350))
        pygame.display.update()
        pygame.display.flip()
    GameDisplay.fill((255,255,255))
    TurnCounter()


