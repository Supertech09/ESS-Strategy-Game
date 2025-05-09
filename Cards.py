import Include as include
import pygame
import matplotlib as mpl
import time

testfont = pygame.font.SysFont('Monospaced', 25, ( 0, 0, 0))


class MicrobeCard():
    def __init__(self, name, description, cost, image_path, AllowsNitrogenFixation, NitrogenMultiplier, Duration, CardType):
        self.name = "Soil Microbe"
        self.description = "Allows Nitrogen Fixation, lasts for a long time."
        self.cost = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.AllowsNitrogenFixation = True
        self.NitrogenMultiplier = 1
        self.Duration = 9999
        self.CardType = "Organism"

class LightningCard():
    def __init__(self, name, description, cost, image_path, AllowsNitrogenFixation, NitrogenMultiplier, PhosphorusMultiplier, Duration, CardType):
        self.name = "Lightning Storm"
        self.description = "Weather event that boosts nitrogen fixation and phosphorus avalibility for a short time."
        self.cost = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.AllowsNitrogenFixation = True
        self.NitrogenMultiplier = 3
        self.PhosphorusMultiplier = 1.5
        self.Duration = 2
        self.CardType = "Event"
        
class Decomposition():
    def __init__(self, name, description, cost, image_path, AllowsNitrogenFixation, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
        self.name = "Decomposition"
        self.description = "Decomposes organic matter, releasing nutrients. Doubles all nutrient production for a short while."
        self.cost = 0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.AllowsNitrogenFixation = True
        self.NitrogenMultiplier = 2
        self.PhosphorusMultiplier = 2
        self.CarbonMultiplier = 2
        self.Duration = 5
        self.CardType = "Organism"