import pygame as pygame
import time
import random
from Include import GameInit, TurnNumber, Turn, TurnCounter
import Cards



class Player:
    def __init__(self, Team, Cards, Points):
        self.Team = Team
        self.Cards = Cards
        self.Points = Points
    def GetCards(self):
        if Team == "Enviroment":
            for draw in range(3):
                Card = random.randint(1, 10)




            

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
pygame.font.init()  # Ensure font module is initialized

GameInit = GameInit()  # Initialize the game (ensure this doesn't conflict with pygame.init())
global Game
Game = False
global TeamSelect
TeamSelect = False

GameDisplay = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
Player1 = Player("None", 1, 0)
Bot = Player("None", 0, 0)


testfont = pygame.font.SysFont("mono", 20)


# Load and scale images
TitleScreen = pygame.image.load('Title Screen Layout.png')
TitleScreen = pygame.transform.scale(TitleScreen, (1000, 750))
TeamSelectScreen = pygame.image.load('TeamSelect.png')
TeamSelectScreen = pygame.transform.scale(TeamSelectScreen, (1000, 750))
gamesurface = pygame.image.load('Background Test.png')
gamesurface = pygame.transform.scale(gamesurface, (1000, 750))

# Buttons
teambutton = pygame.Rect(323, 298, 288, 94)  # Rect for the team area
playbutton = pygame.Rect(323, 413, 288, 100)  # Rect for the play area
cardbutton = pygame.Rect(323, 530, 288, 100)  # Rect for the card area
exitbutton = pygame.Rect(990, 730, 50, 50)  # Rect for the exit area
EnviromentTeam = pygame.Rect(0, 0, 500, 750)  # Rect for the Enviroment team
IndustryTeam = pygame.Rect(500, 0, 1000, 750)  # Rect for the Industry team

while True:
    if not Game and not TeamSelect:
        GameDisplay.blit(TitleScreen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if teambutton.collidepoint(event.pos):
                        print('Team Select clicked.')
                        TeamSelect = True
                    elif playbutton.collidepoint(event.pos):
                        print('Play clicked.')
                        if Player1.Team == "None":
                            Team = random.randint(1, 2)
                            if Team == 1:
                                Player1.Team = "Enviroment"
                                Bot.Team = "Industry"
                            elif Team == 2:
                                Player1.Team = "Industry"
                                Bot.Team = "Enviroment"
                        Game = True
                    elif cardbutton.collidepoint(event.pos):
                        print('Cards clicked.')

    if TeamSelect:
        GameDisplay.fill(WHITE)
        GameDisplay.blit(TeamSelectScreen, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if EnviromentTeam.collidepoint(event.pos):
                        print('Enviroment Team selected.')
                        Player1.Team = "Enviroment"
                        Bot.Team = "Industry"
                        Game = True
                        TeamSelect = False
                    elif IndustryTeam.collidepoint(event.pos):
                        print('Industry Team selected.')
                        Player1.Team = "Industry"
                        Bot.Team = "Enviroment"
                        Game = True
                        TeamSelect = False
    if Game:
        GameDisplay.fill(WHITE)  # Clear the screen before rendering
        GameDisplay.blit(gamesurface, (0, 0))
        Player1Display = testfont.render(f"You: {Player1.Team}", True, BLACK)
        Player2Display = testfont.render(f"Bot: {Bot.Team}", True, BLACK)
        TurnDisplay = testfont.render(f"Turn: {Turn}", True, BLACK)
        GameDisplay.blit(Player1Display, (5, 250))
        GameDisplay.blit(Player2Display, (5, 300))
        GameDisplay.blit(TurnDisplay, (5, 350))
        pygame.draw.rect(GameDisplay, RED, exitbutton)
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
                    if exitbutton.collidepoint(event.pos):
                        print('Exit clicked.')
                        Game = False
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()



