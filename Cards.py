import Include as include
import pygame as pygame
import matplotlib as mpl
import time

pygame.init()
#pygame.font.init()
#testfont = pygame.font.SysFont("mono", 25)



class Template():
    def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
        self.name = "Template"
        self.id = 999
        self.description = "Put description here."
        self.cost = 1
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 150))
        self.AllowsNitrogenFixation = False
        self.CarbonAddSoil = 0
        self.NitrogenAddSoil = 0
        self.PhosAddSoil = 0
        self.NitrogenMultiplier = 1
        self.PhosphorusMultiplier = 1
        self.CarbonMultiplier = 1
        self.Duration = 1
        self.CardType = "Template"


class EnviromentCards:

    class MicrobeCard():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation, NitrogenMultiplier, Duration, CardType):
            self.id = 1
            self.name = "Soil Microbe"
            self.description = "Allows Nitrogen Fixation, lasts for a long time."
            self.cost = 1
            self.image = pygame.image.load("CardTextures/Microbe.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = True
            self.NitrogenMultiplier = 1
            self.Duration = 9999
            self.CardType = "Organism"

    class LightningCard():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation, NitrogenMultiplier, PhosphorusMultiplier, Duration, CardType):
            self.name = "Lightning Storm"
            self.id = 2
            self.description = "Weather event that boosts nitrogen fixation and phosphorus avalibility for a short time."
            self.cost = 3
            self.image = pygame.image.load("CardTextures/Lightning.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = True
            self.NitrogenMultiplier = 3
            self.PhosphorusMultiplier = 1.5
            self.Duration = 2
            self.CardType = "Event"
            
    class Decomposition():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, Pollution, CardType):
            self.name = "Decomposition"
            self.id = 3
            self.description = "Decomposes organic matter, releasing nutrients. Doubles all nutrient production for a short while."
            self.cost = 2
            self.image = pygame.image.load("CardTextures/Decomposition.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = True
            self.NitrogenMultiplier = 2
            self.PhosphorusMultiplier = 2
            self.CarbonMultiplier = 2
            self.Pollution = -2
            self.Duration = 5
            self.CardType = "Organism"

    class Photosynthesis():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation, CarbonAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Photosynthesis"
            self.id = 4
            self.description = "Plants convert Carbon Dioxide, Water, and Sunlight into Oxygen and Glucose. Adds carbon to the soil"
            self.cost = 2
            self.image = pygame.image.load("CardTextures/Photosynthesis.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 2
            self.Pollution = -2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class Weathering():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation, CarbonAddSoil, NitrogenAddSoil,PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Weathering and Erosion"
            self.id = 5
            self.description = "Rocks and minerals break down to release nutrients."
            self.cost = 3
            self.image = pygame.image.load("CardTextures/Weathering.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 3
            self.NitrogenAddSoil = 3
            self.PhosAddSoil = 3
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class AnimalWaste():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Animal Waste"
            self.id = 6
            self.description = "Animal waste adds nutrients to the soil."
            self.cost = 1
            self.image = pygame.image.load("CardTextures/AnimalWaste.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 0
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 3
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Organism"

    class CarbonUptake():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Carbon Uptake"
            self.id = 7
            self.description = "Plants and animals take up carbon either from the soil or carbon-rich food."
            self.cost = 2
            self.image = pygame.image.load("CardTextures/CarbonUptake.png")
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 2
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 0
            self.Pollution = -2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class Sequestration():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Carbon Sequestration"
            self.id = 8
            self.description = "Plants take up carbon from the atmosphere and store it in the soil."
            self.cost = 3
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 5
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 0
            self.Pollution = -2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1.2
            self.Duration = 3
            self.CardType = "Process"

    class NiceFertilizer():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Correct Fertilization"
            self.id = 9
            self.description = "Good fertilization techniques increase nitrogen and phosphorus in the soil."
            self.cost = 4
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 0
            self.NitrogenAddSoil = 4
            self.PhosAddSoil = 1
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class Methane():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Methane Release"
            self.id = 10
            self.description = "Animals release methane into the atmosphere but add carbon to the soil. Methane is a more potent greenhouse gas than CO2."
            self.cost = 2
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 3
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 0
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Organism"

EnviromentCardList = [
    EnviromentCards.MicrobeCard,
    EnviromentCards.LightningCard,
    EnviromentCards.Decomposition,
    EnviromentCards.Photosynthesis,
    EnviromentCards.Weathering,
    EnviromentCards.AnimalWaste,
    EnviromentCards.CarbonUptake,
    EnviromentCards.Sequestration,
    EnviromentCards.NiceFertilizer,
    EnviromentCards.Methane
]

class IndustryCards:

    class DenitrifyingBacteria():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Denitrifying Bacteria"
            self.id = 11
            self.description = "Denitrifying bacteria convert nitrates into nitrogen gas, reducing nitrogen in the soil."
            self.cost = 2
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 0
            self.NitrogenAddSoil = -2
            self.PhosAddSoil = 0
            self.NitrogenMultiplier = .75
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 3
            self.CardType = "Organism"

    class OverFertilizer():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Over-Fertilization"
            self.id = 12
            self.description = "Over-fertilization can lead to nutrient runoff and pollution."
            self.cost = 3
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = -2
            self.NitrogenAddSoil = 3
            self.PhosAddSoil = 0
            self.Pollution = 2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class NOxPollute():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "NOx Pollution"
            self.id = 13
            self.description = "Nox pollution from industry can lead to acid rain and other environmental issues."
            self.cost = 2
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = 0
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 0
            self.Pollution = 3
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class Deforestation():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Deforestation"
            self.id = 14
            self.description = "Deforestion reduces the ability of the ecosystem to sequester carbon and adds carbon to the atmosphere."
            self.cost = 1
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = -1
            self.NitrogenAddSoil = 0
            self.PhosAddSoil = 0
            self.Pollution = 2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 0.75
            self.Duration = 1
            self.CardType = "Process"

    class Extraction():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Extraction"
            self.id = 15
            self.description = "Extraction of natural resources leads to removal of carbon and nutrients from the soil."
            self.cost = 2
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = -1
            self.NitrogenAddSoil = -1
            self.PhosAddSoil = -1
            self.Pollution = 2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

    class Pesticides():
        def __init__(self, id, name, description, cost, image_path, AllowsNitrogenFixation,CarbonAddSoil,NitrogenAddSoil, PhosAddSoil, Pollution, CarbonMultiplier, NitrogenMultiplier, PhosphorusMultiplier, CardType):
            self.name = "Pesticide Use"
            self.id = 16
            self.description = "Overuse of pesticides leads to pollution and loss of resources."
            self.cost = 1
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (100, 150))
            self.AllowsNitrogenFixation = False
            self.CarbonAddSoil = -1
            self.NitrogenAddSoil = -1
            self.PhosAddSoil = -1
            self.Pollution = 2
            self.NitrogenMultiplier = 1
            self.PhosphorusMultiplier = 1
            self.CarbonMultiplier = 1
            self.Duration = 1
            self.CardType = "Process"

IndustryCardList = [
    IndustryCards.DenitrifyingBacteria,
    IndustryCards.OverFertilizer,
    IndustryCards.NOxPollute,
    IndustryCards.Deforestation,
    IndustryCards.Extraction,
    IndustryCards.Pesticides
    ]

print("Enviroment Card List: ", EnviromentCardList)
print("Industry Card List: ", IndustryCardList)
print("Enviroment Card List Length: ", len(EnviromentCardList))
print("Industry Card List Length: ", len(IndustryCardList))