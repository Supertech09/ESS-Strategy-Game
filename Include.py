import pygame as pygame
import matplotlib as mpl
  # Initialize TurnNumber
global TurnNumber
TurnNumber = 0
global Turn
Turn = 1
def GameInit():
    global GameDisplay
    global Titlefont
    pygame.init()
    pygame.font.init()
    pygame.mixer.init()
    pygame.display.init()
    GameDisplay = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
    pygame.display.set_caption("Earth Strategy")
    pygame.font.init()
    Titlefont = pygame.font.SysFont('Arial', 50, (0, 0, 0))
def TurnCounter():
    global TurnNumber
    global Turn
    TurnNumber = TurnNumber + 1
    if TurnNumber%2 == 0:
        Turn = 2
    else:
        Turn = 1


