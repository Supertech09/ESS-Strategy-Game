import Include as include
import pygame as pygame
import matplotlib as mpl
import time

pygame.init()

class EnvironmentCards:

    class MicrobeCard:
        id = 1
        name = "Soil Microbe"
        description = "Allows Nitrogen Fixation, lasts for a long time."
        cost = 1
        image_path = "CardTextures/Microbe.png"
        AllowsNitrogenFixation = True
        NitrogenMultiplier = 1
        Duration = 9999
        CardType = "Organism"

    class LightningCard:
        id = 2
        name = "Lightning Storm"
        description = "Weather event that boosts nitrogen fixation and phosphorus avalibility for a short time."
        cost = 3
        image_path = "CardTextures/Lightning.png"
        AllowsNitrogenFixation = True
        NitrogenMultiplier = 3
        PhosphorusMultiplier = 1.5
        Duration = 2
        CardType = "Event"

    class Decomposition:
        id = 3
        name = "Decomposition"
        description = "Decomposes organic matter, releasing nutrients. Doubles all nutrient production for a short while."
        cost = 2
        image_path = "CardTextures/Decomposition.png"
        AllowsNitrogenFixation = True
        NitrogenMultiplier = 2
        PhosphorusMultiplier = 2
        CarbonMultiplier = 2
        Pollution = -2
        Duration = 5
        CardType = "Organism"

    class Photosynthesis:
        id = 4
        name = "Photosynthesis"
        description = "Plants convert Carbon Dioxide, Water, and Sunlight into Oxygen and Glucose. Adds carbon to the soil"
        cost = 2
        image_path = "CardTextures/Photosynthesis.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 2
        Pollution = -2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class Weathering:
        id = 5
        name = "Weathering and Erosion"
        description = "Rocks and minerals break down to release nutrients."
        cost = 3
        image_path = "CardTextures/Weathering.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 3
        NitrogenAddSoil = 3
        PhosAddSoil = 3
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class AnimalWaste:
        id = 6
        name = "Animal Waste"
        description = "Animal waste adds nutrients to the soil."
        cost = 1
        image_path = "CardTextures/AnimalWaste.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 2
        NitrogenAddSoil = 0
        PhosAddSoil = 3
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Organism"

    class CarbonUptake:
        id = 7
        name = "Carbon Uptake"
        description = "Plants and animals take up carbon either from the soil or carbon-rich food."
        cost = 2
        image_path = "CardTextures/CarbonUptake.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 2
        NitrogenAddSoil = 0
        PhosAddSoil = 0
        Pollution = -2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class Sequestration:
        id = 8
        name = "Carbon Sequestration"
        description = "Plants take up carbon from the atmosphere and store it in the soil."
        cost = 3
        image_path = "CardTextures/Sequestration.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 5
        NitrogenAddSoil = 0
        PhosAddSoil = 0
        Pollution = -2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1.2
        Duration = 3
        CardType = "Process"

    class NiceFertilizer:
        id = 9
        name = "Correct Fertilization"
        description = "Good fertilization techniques increase nitrogen and phosphorus in the soil."
        cost = 4
        image_path = "CardTextures/GoodFertilizer.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 0
        NitrogenAddSoil = 4
        PhosAddSoil = 1
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class Methane:
        id = 10
        name = "Methane Release"
        description = "Animals release methane into the atmosphere but add carbon to the soil. Methane is a more potent greenhouse gas than CO2."
        cost = 2
        image_path = "CardTextures/MethaneRelease.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 3
        NitrogenAddSoil = 0
        PhosAddSoil = 1
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Organism"

EnvironmentCardList = [
    EnvironmentCards.MicrobeCard,
    EnvironmentCards.LightningCard,
    EnvironmentCards.Decomposition,
    EnvironmentCards.Photosynthesis,
    EnvironmentCards.Weathering,
    EnvironmentCards.AnimalWaste,
    EnvironmentCards.CarbonUptake,
    EnvironmentCards.Sequestration,
    EnvironmentCards.NiceFertilizer,
    EnvironmentCards.Methane
]

class IndustryCards:

    class DenitrifyingBacteria:
        id = 11
        name = "Denitrifying Bacteria"
        description = "Denitrifying bacteria convert nitrates into nitrogen gas, reducing nitrogen in the soil."
        cost = 2
        image_path = "CardTextures/DeNitBacteria.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 0
        NitrogenAddSoil = -2
        PhosAddSoil = 0
        NitrogenMultiplier = .75
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 3
        CardType = "Organism"

    class OverFertilizer:
        id = 12
        name = "Over-Fertilization"
        description = "Over-fertilization can lead to nutrient runoff and pollution."
        cost = 3
        image_path = "CardTextures/OverFertilizer.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = -2
        NitrogenAddSoil = 3
        PhosAddSoil = 0
        Pollution = 2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class NOxPollute:
        id = 13
        name = "NOx Pollution"
        description = "Nox pollution from industry can lead to acid rain and other environmental issues."
        cost = 2
        image_path = "CardTextures/NOxPollute.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = 0
        NitrogenAddSoil = 0
        PhosAddSoil = 0
        Pollution = 3
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class Deforestation:
        id = 14
        name = "Deforestation"
        description = "Deforestion reduces the ability of the ecosystem to sequester carbon and adds carbon to the atmosphere."
        cost = 1
        image_path = "CardTextures/Deforestation.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = -1
        NitrogenAddSoil = 0
        PhosAddSoil = 0
        Pollution = 2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 0.75
        Duration = 1
        CardType = "Process"

    class Extraction:
        id = 15
        name = "Extraction"
        description = "Extraction of natural resources leads to removal of carbon and nutrients from the soil."
        cost = 2
        image_path = "CardTextures/Extraction.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = -1
        NitrogenAddSoil = -1
        PhosAddSoil = -1
        Pollution = 2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

    class Pesticides:
        id = 16
        name = "Pesticide Use"
        description = "Overuse of pesticides leads to pollution and loss of resources."
        cost = 1
        image_path = "CardTextures/Pesticides.png"
        AllowsNitrogenFixation = False
        CarbonAddSoil = -1
        NitrogenAddSoil = -1
        PhosAddSoil = -1
        Pollution = 2
        NitrogenMultiplier = 1
        PhosphorusMultiplier = 1
        CarbonMultiplier = 1
        Duration = 1
        CardType = "Process"

IndustryCardList = [
    IndustryCards.DenitrifyingBacteria,
    IndustryCards.OverFertilizer,
    IndustryCards.NOxPollute,
    IndustryCards.Deforestation,
    IndustryCards.Extraction,
    IndustryCards.Pesticides
    ]

print("Environment Card List: ", EnvironmentCardList)
print("Industry Card List: ", IndustryCardList)
print("Environent Card List Length: ", len(EnvironmentCardList))
print("Industry Card List Length: ", len(IndustryCardList))