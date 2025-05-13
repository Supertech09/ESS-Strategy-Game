import pygame as pygame
import time
import random
from Include import GameInit, TurnNumber, TurnCounter
import Cards
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init()


class Player:
    def __init__(self, Team, Cards, Points):
        self.Team = Team
        self.Cards = Cards
        self.Points = Points

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize pygame and font module


print("Pygame initialized:", pygame.get_init())
print("Font module initialized:", pygame.font.get_init())

# Create font object
testfont = pygame.font.SysFont("mono", 20) 
print("Font object created:", testfont)
# Initialize game display
GameDisplay = pygame.display.set_mode((1000, 750), pygame.RESIZABLE)
pygame.display.set_caption("Earth Strategy")

# Initialize players
Player1 = Player("None", 1, 0)

# Initialize turn counter
Turn = 1
Bot = Player("None", 0, 0)
EnviromentCardList = Cards.EnviromentCardList

# Load and scale images
TitleScreen = pygame.image.load('Title Screen Layout.png')
TitleScreen = pygame.transform.scale(TitleScreen, (1000, 750))
TeamSelectScreen = pygame.image.load('TeamSelect.png')
TeamSelectScreen = pygame.transform.scale(TeamSelectScreen, (1000, 750))
gamesurface = pygame.image.load('Background Test.png')
gamesurface = pygame.transform.scale(gamesurface, (1000, 750))

# Buttons
teambutton = pygame.Rect(323, 298, 288, 94)
playbutton = pygame.Rect(323, 413, 288, 100)
cardbutton = pygame.Rect(323, 530, 288, 100)
exitbutton = pygame.Rect(950, 10, 50, 50)
EnviromentTeam = pygame.Rect(0, 0, 500, 750)
IndustryTeam = pygame.Rect(500, 0, 1000, 750)

# Game states
Game = False
TeamSelect = False

# Main game loop
while True:
    for event in pygame.event.get():
        # Handle quit events
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        # Handle mouse button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if not Game and not TeamSelect:
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
                elif TeamSelect:
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
                elif Game:
                    if exitbutton.collidepoint(event.pos):
                        print('Exit clicked.')
                        Game = False

    # Render the appropriate screen
    if not Game and not TeamSelect:
        GameDisplay.blit(TitleScreen, (0, 0))
    elif TeamSelect:
        GameDisplay.fill(WHITE)
        GameDisplay.blit(TeamSelectScreen, (0, 0))
    elif Game:
        GameDisplay.fill(WHITE)
        GameDisplay.blit(gamesurface, (0, 0))
        Player1Display = testfont.render(f"You: {Player1.Team}", True, BLACK)
        Player2Display = testfont.render(f"Bot: {Bot.Team}", True, BLACK)
        TurnDisplay = testfont.render(f"Turn: {Turn}", True, BLACK)
        GameDisplay.blit(Player1Display, (5, 250))
        GameDisplay.blit(Player2Display, (5, 300))
        GameDisplay.blit(TurnDisplay, (5, 350))
        pygame.draw.rect(GameDisplay, RED, exitbutton)

    pygame.display.update()


