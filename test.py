import pygame as pygame
import time
import random
from Include import GameInit, TurnNumber, Turn, TurnCounter

class Player:
    def __init__(self, Team, Cards, Points):
        self.Team = Team
        self.Cards = Cards
        self.Points = Points

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()  # Ensure font module is initialized

GameInit = GameInit()  # Initialize the game (ensure this doesn't conflict with pygame.init())
global Game
Game = False

GameDisplay = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
Player1 = Player("Enviroment", 1, 0)
Bot = Player("Industry", 0, 0)

# Correct font initialization
testfont = pygame.font.SysFont("Arial", 25)
print(f"Font initialized: {testfont}")  # Debugging output

# Load and scale images
TitleScreen = pygame.image.load('Title Screen Layout.png')
TitleScreen = pygame.transform.scale(TitleScreen, (1000, 750))
gamesurface = pygame.image.load('Background Test.png')
gamesurface = pygame.transform.scale(gamesurface, (1000, 750))

# Buttons
teambutton = pygame.Rect(323, 298, 288, 94)  # Rect for the team area
playbutton = pygame.Rect(323, 413, 288, 100)  # Rect for the play area
cardbutton = pygame.Rect(323, 530, 288, 100)  # Rect for the card area

while True:
    if not Game:
        GameDisplay.blit(TitleScreen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if teambutton.collidepoint(event.pos):
                        print('Team Select clicked.')
                    elif playbutton.collidepoint(event.pos):
                        print('Play clicked.')
                        Game = True
                    elif cardbutton.collidepoint(event.pos):
                        print('Cards clicked.')

    if Game:
        GameDisplay.fill(WHITE)  # Clear the screen before rendering
        GameDisplay.blit(gamesurface, (0, 0))
        Player1Display = testfont.render(f"You: {Player1.Team}", True, BLACK)
        Player2Display = testfont.render(f"Bot: {Bot.Team}", True, BLACK)
        TurnDisplay = testfont.render(f"Turn: {Turn}", True, BLACK)
        GameDisplay.blit(Player1Display, (10, 250))
        GameDisplay.blit(Player2Display, (10, 300))
        GameDisplay.blit(TurnDisplay, (10, 350))
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    TurnCounter()  # Update the turn counter