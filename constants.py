# Constants for the Digifiz Dash
import pygame


#   Currently enables RPM to rise and fall with keyboard up and down presses.
#   Will potentially change this in future to have full gauge functionality.
#   testingStatus = False

testingStatus = False



#   Screen Size
WIDTH, HEIGHT = 1920, 1080 # use your screens display information/ use as informações de largura e altura da sua tela
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.DOUBLEBUF) # Tela normal
#WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.RESIZABLE) # Tela cheia
FPS = 60

# Title and Icon
ICON = "images/speedometer.png"
BG = "images/background.png"
programIcon = pygame.image.load(ICON)
project_name = "Digifiz Dashboard - "
digifiz_ver = "v. 0.5"

#   Colours
COR_WHITE = (255, 255, 255)   # Branco para o velocímetro
COR_WHITE1= (255, 255, 255)        # Branco para relógio e outros elementos
DARK_GREY = (9, 52, 50)         #   background of the digits (for the 7segment appearance)

#   Font Details
FONT_PATH = "fonts/DSEG7Classic-Bold.ttf"
FONT_LARGE = 174    #   Speedo size
FONT_MEDIUM = 94    #   Clock, MFA, Fuel size
FONT_SMALL = 67     #   Odo Size


#   Locations for gauge graphics, each has the same start XY but builds upon it, check images folder
RPM_XY = (135, 5)
COOLANT_XY = (1480, 105)
EGT_XY = (1460, 105)
OILPRESSURE_XY = (1520, 105)
BOOST_XY = (1580, 105)
CLOCK_XY = (555, 495)
FUEL_XY = (1100, 495)
ODO_XY = (60, 495)
ODO_L_XY = (450, 555)
MFA_XY = (1435, 536)
MFABG_XY = (1021, 432)
SPEEDO_XY = (1247, 305)





'''                         LOAD IMAGES                         '''

BACKGROUND = pygame.image.load(BG).convert_alpha()
MFA = pygame.image.load("images/indicators/MFA_temp.png").convert_alpha()
fuelresOn = pygame.image.load("images/indicators/fuelResOn.png").convert_alpha()
fuelresOff = pygame.image.load("images/indicators/fuelResOff.png").convert_alpha()
