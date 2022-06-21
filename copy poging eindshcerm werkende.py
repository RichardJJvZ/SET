# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 08:32:03 2022

@author: esmee
"""


import random
import pygame
import sys


amounts = ['1', '2', '3']
symbols = ['diamond', 'oval', 'squiggle']
colours = ['green', 'purple', 'red']
fillings = ['empty', 'shaded', 'filled']
eigenschappen = ['colours', 'symbols', 'fillings', 'amounts']

    
def computer_antwoord(lijst):
    if lijst == []:
        antwoord= False
    else:
        antwoord=lijst[0]
    return antwoord

class Card:
    """
    
    Attributes
    ----------
    
    
    Methods
    ----------
    """

    def __init__(self, colour, symbol, filling, amount):
        """ Deze methode initialiseert de kaarten met alle verschillende eigenschappen
        Parameters
        ----------
        colour : TYPE
            DESCRIPTION.
        symbol : TYPE
            DESCRIPTION.
        filling : TYPE
            DESCRIPTION.
        amount : TYPE
            DESCRIPTION.

        Returns
        -------
        None. Output wanneer er instances worden gemaakt, zoals in createdeck.

        """
        self.attributen = [colour,symbol,filling,amount]

    def isset(self, other1, other2):
        """Deze methode controleert of 3 kaarten een set vormen.
        
        Parameters
        ----------
        self: instantie van de klasse Card
         
        other1 : instantie van de klasse Card
         
        other2 : instantie van de klasse Card
         
        Returns
        -------
        bool.
        """
        
        samecounter = 0
        for i in range(4):
            if self.attributen[i] == other1.attributen[i] and self.attributen[i] == other2.attributen[i]:
                samecounter += 1
                pass
            elif self.attributen[i] != other1.attributen[i] and self.attributen[i] != other2.attributen[i] and other1.attributen[i] != other2.attributen[i]:
                pass
            else:
                return False
        if samecounter == 4: #voor als mensen willen valsspelen en zeggen dat 3 keer dezelfde kaart een set is
            return False
        else:
            return True

def createdeck():
    """ Maakt alle mogelijke 81 instances van de klasse Card.
    
    Returns
    -------
    mogelijke_kaarten : lijst
        combineert alle mogelijkheden in de attributen en maakt zo alle instances van de klasse Card.

    """
    mogelijke_kaarten = []

    for a in range(3):
        for s in range(3):
            for c in range(3):
                for f in range(3):
                    mogelijke_kaarten.append(Card(a,s,c,f))
    return mogelijke_kaarten

def makenumbers():
    """ Maakt alle getallen voor op de kaarten en blit deze op het scherm. Is meermaals nodig, dus vandaar de functie.
    
    Returns
    -------
    None. Wordt meermaals gebruikt dus is grotendeels ter besparing van ruimte.

    """
    getal1 = font.render('1', True, black)
    getal2 = font.render('2', True, black)
    getal3 = font.render('3', True, black)
    getal4 = font.render('4', True, black)
    getal5 = font.render('5', True, black)
    getal6 = font.render('6', True, black)
    getal7 = font.render('7', True, black)
    getal8 = font.render('8', True, black)
    getal9 = font.render('9', True, black)
    getal0 = font.render('0', True, black)
    getalmin = font.render('-', True, black)
    getalis =font.render('=', True, black)

    screen.blit(getal1, (30,195))
    screen.blit(getal2, (140,195))
    screen.blit(getal3, (250,195))
    screen.blit(getal4, (360,195))
    screen.blit(getal5, (30,405))
    screen.blit(getal6, (140,405))
    screen.blit(getal7, (250,405))
    screen.blit(getal8, (360,405))
    screen.blit(getal9, (30,615))
    screen.blit(getal0, (140,615))
    screen.blit(getalmin, (250,615))
    screen.blit(getalis, (360,615))




#nogteeds zelfde start commando
def starten():
    """ Pakt random 12 kaarten uit de deck.

    Returns
    -------
    sample : lijst
        12 willekeurige kaarten uit de deck.

    """
    sample = random.sample(deck, k=12)
    for stukje in sample:
        deck.remove(stukje)
    return sample


#als wij of de pc een set heeft gemaakt
def aanvullen(): 
    """ Vult 3 kaarten aan wanneer er een set is gevonden
    
    Returns
    -------
    trekken : TYPE
        DESCRIPTION.

    """
    trekken = random.sample(deck, k=3)
    for stukje in trekken:
        deck.remove(stukje)
    return trekken


#als er geen set te maken is
def vervangen():
        """
    Een andere functie die bijna hetzelfde doet als aanvullen.
    Nu kiezen we er alleen voor dat de kaarten die we weg halen op een andere stapel bewaren
    Dit zorgt ervoor dat altijd evenveel sets in het spel ziiten
    (tenzij natuurlijk bij het laatste speelbord geen set zit)
        """
        trekken = random.sample(deck, k=3)
        for stukje in trekken:
            aflegstapel.append(stukje)
            deck.remove(stukje)
        return trekken

def card_file(card):
    """ Haalt aan de hand van de attributen van de kaart de goede kaart uit de zip.
    
    Parameters
    ----------
    card : insantie van het type Card
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    out = ""
    attributen = card.attributen
    for i in range(4):
        out += (globals()[eigenschappen[i]])[attributen[i]]
    return "kaarten/"+out+".gif"

### Initialise screen
pygame.init()
window = (800,700)
screen = pygame.display.set_mode(window)
screen.fill((255, 255, 255))
done = False
pygame.display.set_caption("Set")
pink = (255,192,203)
darkpink = (170, 51, 106)
black = (0,0,0)
grey = (150,150,150)
gekozenniveau = 0
###

### card_file(card) geeft een string terug die de juiste kaart laadt
#test_kaart = Card(2,2,2,1)
#kaart = pygame.image.load(card_file(test_kaart))
#kaart = pygame.transform.scale(kaart, (100,200))
#kaartrect = kaart.get_rect()
#print(kaartrect)

### Add card to screen
#screen.blit(kaart,kaartrect)


#startscherm
font = pygame.font.SysFont('Roboto', 35)
text0 = font.render('Welkom bij Set!', True, darkpink)
text1 = font.render('Klik op een van de 3 niveaus', True, black)
text2 = font.render('Makkelijk', True, black)
text3 = font.render('Gemiddeld', True, black)
text4 = font.render('Moeilijk', True, black)

screen.blit(text0, (320,100))
screen.blit(text1, (250,150))


button2 = pygame.draw.rect(screen, pink, (330, 220, 150, 75))
screen.blit(text2, (350,240))

button3 = pygame.draw.rect(screen, pink, (330, 340, 150, 75))
screen.blit(text3, (340,360))

button4 = pygame.draw.rect(screen, pink, (330, 460, 150, 75))
screen.blit(text4, (360,480))

pygame.display.flip()
"""


   tijdelijk verplaatstnaar andere plek voor nieuwe definitie main
   
   
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 330 <= mouse[0] <= 480 and 220 <= mouse[1] <= 295:
                gekozenniveau = 1
                break
            elif 330 <= mouse[0] <= 480 and 340 <= mouse[1] <= 415:
                gekozenniveau = 2
                break
            elif 330 <= mouse[0] <= 480 and 460 <= mouse[1] <= 535:
                gekozenniveau = 3
                break
    if gekozenniveau != 0:
        screen.fill((255, 255, 255))
        break
#eind startscherm

"""

#begin code timer
clock = pygame.time.Clock()
counter = 0
pygame.time.set_timer(pygame.USEREVENT,100)
achtergrondbar = pygame.image.load("blackbar.png")
achtergrondbar = pygame.transform.scale(achtergrondbar,(50,300))
achtergrondscore = pygame.image.load("zwartblok.png")
achtergrondscore = pygame.transform.scale(achtergrondscore , (250,100))
#screen.blit(achtergrondbar, (450, 50))

#achtergrondbar = screen.blit(screen, 450, 50, 50, 300)

laadbar = pygame.draw.rect(screen, pink, pygame.Rect(0,0,0,0))
pygame.display.flip()


if gekozenniveau == 1:
    stukjeerbij = 0.9
elif gekozenniveau == 2:
    stukjeerbij = 1.8
elif gekozenniveau == 3:
    stukjeerbij = 5.4
    
#eind code timer

tabletop = pygame.image.load("tabletop.png")
tabletop = pygame.transform.scale(tabletop, (800,700))
screen.blit(tabletop, (0,0))
pygame.display.flip()



"""
Hier wordt de eerste keer het bord geladen
"""
"""
for j in range(3):
    for i in range(4):    
        laden = pygame.image.load(card_file(startset[i+4*j]))
        laden = pygame.transform.scale(laden, (100,200))
        screen.blit(laden, (i*110 + 20, j*210 + 20))

makenumbers()
"""
### Update display
pygame.display.flip()

keuze = []
"""
Total_cotrole kijkt naar de elementen die op het speelbord liggen, vervolgens gaat 
het in een driedubbele loop alle mogelijke combinaties af
Dit gebeurt in de volgorde [1,2,3] [1,2,4] t/m [1,2,12]
Daarna loopt het tweede element een stapje. Dan gaat controleren we dus [1,3,4]
De functie geeft alle verzamelingen terug waarvoor de functie isset True returnt
"""
def totale_controle():
    sets=[]
    for i in range(10):
        keuze1=i
        for j in range(i+1,11): #i+1 t/m 11
            keuze2=j
            for k in range(j+1,12): #j+1 t/m 12
                keuze3=k
                if speelbord[keuze1].isset(speelbord[keuze2], speelbord[keuze3]):
                    sets.append([i+1,j+1,k+1])
    return sets
def keuze_pc():
    #de functie neemt het eerste element uit de lijst lijsten die we hebben gekregen uit
    #totale_controle. In principe kan deze leeg zijn. Als dit voorkomt zorgen we dat we deze functie niet aanroepen
    keuze = totale_controle()[0]
    return keuze

#als de timer op is dan zeggen we True, dus we moeten eerst
#aangeven dat de timer nog niet klaar is
#hier komt de main code voor het spel
pygame.init()
def main():
    global score_speler , deck, aflegstapel, counter, keuze, gekozenniveau, speelbord
    
    
    

    window = (800,700)
    screen = pygame.display.set_mode(window)
    screen.fill((255, 255, 255))
    done = False
    pygame.display.set_caption("Set")
    pink = (255,192,203)
    darkpink = (170, 51, 106)
    black = (0,0,0)
    grey = (150,150,150)
    gekozenniveau = 0
    ###

    ### card_file(card) geeft een string terug die de juiste kaart laadt
    #test_kaart = Card(2,2,2,1)
    #kaart = pygame.image.load(card_file(test_kaart))
    #kaart = pygame.transform.scale(kaart, (100,200))
    #kaartrect = kaart.get_rect()
    #print(kaartrect)

    ### Add card to screen
    #screen.blit(kaart,kaartrect)


    #startscherm
    font = pygame.font.SysFont('Roboto', 35)
    text0 = font.render('Welkom bij Set!', True, darkpink)
    text1 = font.render('Klik op een van de 3 niveaus', True, black)
    text2 = font.render('Makkelijk', True, black)
    text3 = font.render('Gemiddeld', True, black)
    text4 = font.render('Moeilijk', True, black)

    screen.blit(text0, (320,100))
    screen.blit(text1, (250,150))


    button2 = pygame.draw.rect(screen, pink, (330, 220, 150, 75))
    screen.blit(text2, (350,240))

    button3 = pygame.draw.rect(screen, pink, (330, 340, 150, 75))
    screen.blit(text3, (340,360))

    button4 = pygame.draw.rect(screen, pink, (330, 460, 150, 75))
    screen.blit(text4, (360,480))

    pygame.display.flip()
    
    
    
    keuze = []
    score_speler= 0
    score_pc = 0
    deck = createdeck()
    aflegstapel=[]
    getallen=[]
    klaar = False
    window = (800,700)
    screen = pygame.display.set_mode(window)
    screen.fill((255, 255, 255))
    done = False
    pygame.display.set_caption("Set")
    pink = (255,192,203)
    darkpink = (170, 51, 106)
    black = (0,0,0)
    grey = (150,150,150)
    startset = starten()
    speelbord = startset
    gekozenniveau = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            gekozenniveau = 3   
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 330 <= mouse[0] <= 480 and 220 <= mouse[1] <= 295:
                    gekozenniveau = 1
                    break
                elif 330 <= mouse[0] <= 480 and 340 <= mouse[1] <= 415:
                    gekozenniveau = 2
                    break
                elif 330 <= mouse[0] <= 480 and 460 <= mouse[1] <= 535:
                    gekozenniveau = 3
                    break
        if gekozenniveau != 0:
            screen.fill((255, 255, 255))
            break
    #eind startscherm
    
    
    if gekozenniveau == 1:
        stukjeerbij = 0.9
    elif gekozenniveau == 2:
        stukjeerbij = 1.8
    elif gekozenniveau == 3:
        stukjeerbij = 5.4
        
        
    for j in range(3):
        for i in range(4):    
            laden = pygame.image.load(card_file(startset[i+4*j]))
            laden = pygame.transform.scale(laden, (100,200))
            screen.blit(laden, (i*110 + 20, j*210 + 20))
    
    makenumbers()
    
    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and not klaar:
                if counter == 0:
                    screen.blit(achtergrondbar, (600, 100))
                    """hier laden we de achtergrond nog een keer
                    anders krijgen we dat de getallen en de laadbar blijven
                    staan nadat deze hadden moeten resetten"""
    
    
                counter += 1 #de tijd verloopt een klein stukje, de clock tikt 
                #10x per seconde.
                laadbar = pygame.draw.rect(screen, black, pygame.Rect(610,115,30, counter*stukjeerbij))
                text_ss = font.render('jouw score : ' + str(score_speler), True, black)
                text_spc = font.render('computer score : ' + str(score_pc) , True, black)
                screen.blit(achtergrondscore , (500 , 440))
                screen.blit(text_ss, (510,450))
                screen.blit(text_spc, (510,500))
                pygame.display.flip() #hier pas de display flippen anders heb je een frame
                #waarin niet alles geladen is.
    
                if gekozenniveau == 1:
                    if counter >= 300:#30s. om een set te vinden
                        klaar = True
                        break
                elif gekozenniveau == 2:
                    if counter >= 150:#15seconde om een set te vinden
                        klaar = True
                        break
                elif gekozenniveau == 3:
                    #tijdens het testen van eindscherm naar 5 veranderd zodat je snel
                    #door het spel heen bent
                    if counter >= 5: #5 seconde om een set te vinden. Succes!
                        klaar = True
                        break
                    #lang stuk code dat alle keys afgaat
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    kaart1 = startset[0] #als we op "1" klikken dan keizen we de eerste kaart
                    keuze.append(kaart1) #deze wordt geplakt achteraan de verzameling keuze
                    getallen.append(0) #we moeten onthouden welke keuze we hebben gemaakt voor het aanvullen
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (20,20))
                    pygame.display.flip()
                elif event.key == pygame.K_2:
                    kaart2 = startset[1]
                    keuze.append(kaart2)
                    getallen.append(1)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd,(130,20))
                    pygame.display.flip()
                elif event.key == pygame.K_3:
                    kaart3 = startset[2]
                    keuze.append(kaart3)
                    getallen.append(2)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (240,20))
                    pygame.display.flip()
                elif event.key == pygame.K_4:
                    kaart4 = startset[3]
                    keuze.append(kaart4)
                    getallen.append(3)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (350,20))
                    pygame.display.flip()
                elif event.key == pygame.K_5:
                    kaart5 = startset[4]
                    keuze.append(kaart5)
                    getallen.append(4)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (20,230))
                    pygame.display.flip()
                elif event.key == pygame.K_6:
                    kaart6 = startset[5]
                    keuze.append(kaart6)
                    getallen.append(5)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (130,230))
                    pygame.display.flip()
                elif event.key == pygame.K_7:
                    kaart7 = startset[6]
                    keuze.append(kaart7)
                    getallen.append(6)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (240,230))
                    pygame.display.flip()
                elif event.key == pygame.K_8:
                    kaart8 = startset[7]
                    keuze.append(kaart8)
                    getallen.append(7)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (350,230))
                    pygame.display.flip()
                elif event.key == pygame.K_9:
                    kaart9 = startset[8]
                    keuze.append(kaart9)
                    getallen.append(8)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (20,440))
                    pygame.display.flip()
                elif event.key == pygame.K_0:
                    kaart10 = startset[9]
                    keuze.append(kaart10)
                    getallen.append(9)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (130,440))
                    pygame.display.flip()
                elif event.key == pygame.K_MINUS:
                    kaart11 = startset[10]
                    keuze.append(kaart11)
                    getallen.append(10)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (240,440))
                    pygame.display.flip()
                elif event.key == pygame.K_EQUALS:
                    kaart12 = startset[11]
                    keuze.append(kaart12)
                    getallen.append(11)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (350,440))
                    pygame.display.flip()
                #Deze moeten we denk ik eerst doen als de tijd om is en dan specifiek
                elif event.key == pygame.K_a:
                    print(totale_controle() , len(deck))
                    #deze vooral doen dus want dit vervangt de eerste drie kaarten (volgensmij op de goede manier)
                    if totale_controle() == []:
                       hand = vervangen()
                       getallen=[0,1,2] #deze zouden we kunnen evrvangen als we ze op een specifieke plek willen of evt zelf willekeurig
                       for i in range(3):
                           speelbord[getallen[i]] = hand[i]
                    #hier zet het ding de nieuwe kaarten op de goede plek   
                       for j in range(3):
                           for i in range(4):    
                               laden = pygame.image.load(card_file(speelbord[i+4*j]))
                               laden = pygame.transform.scale(laden, (100,200))
                               screen.blit(laden, (i*110 + 20, j*210 + 20))
                       makenumbers()
                       pygame.display.flip()
    #dit is de keuze die de computer maakt, nogmaals dit moet alleen gebeuren als er een keuze is maar dan doet ie het goed
    #Dit moet dus wel op een timer en niet op een keypress.
    #ook moeten we hier toevoegen dat de computer een punt krijgt, of dat er een punt van het totaal af gaat als dat makkelijker is                
            if klaar: #klaar betekent timer is klaar
                if totale_controle() == []: #als er geen keuze te maken is dan willen we vervangen
                    if deck == []: #als we niet kunnen vervangen dan kijken we of we kaarten opzij hebben gelegd
                        if aflegstapel==[]: #als ook de aflegstapel leeg is dan willen we stoppen
                            done = True
                        else:
                            deck = aflegstapel
                            aflegstapel = []
                    if not done:
                        hand = vervangen()
                        getallen=[0,1,2] #de plek waarop we vervangen zijn de eerste 3 kaarten
                        screen.blit(tabletop, (0,0))
                        for i in range(3):
                            speelbord[getallen[i]] = hand[i]
                #hier zet het ding de nieuwe kaarten op de goede plek   
                    for j in range(3):
                        for i in range(4):    
                           laden = pygame.image.load(card_file(speelbord[i+4*j]))
                           laden = pygame.transform.scale(laden, (100,200))
                           screen.blit(laden, (i*110 + 20, j*210 + 20))
                    #het scherm flipt hier nog niet anders is het lelijk omdat
                    #een deel van de elementen nog neit opnieuw geladen is
                    makenumbers()
                    counter = 0 #tijd reset
                    klaar = False #Boolean die aangeeft of de tijd om is reset
                else: #Als er wel een keuze te maken is kies dan de eerste optie
                    getallen= []
                    """
                    Hier eerst de plekken en de te controlleren kaarten resetten
                    Anders krijg je een probleem als de speler midden in een keuze zit
                    """
                    keuze = []
                    kaart10 = startset[keuze_pc()[0]-1]
                    keuze.append(kaart10)
                    getallen.append(keuze_pc()[0]-1)
                    kaart11 = startset[keuze_pc()[1]-1]
                    keuze.append(kaart11)
                    getallen.append(keuze_pc()[1]-1)
                    kaart12 = startset[keuze_pc()[2]-1]
                    keuze.append(kaart12)
                    getallen.append(keuze_pc()[2]-1)#hier maken we de drie keuzes van kaarten van de computer
                    
                    score_pc += 1 #de computer heeft een set maar dit gaan we ook nog controlleren
                    #we geven hier wel alvast de punten aan de computer want dan kunnen we nu naar
                    #hetzelfde loopje als een speler keuze
                    score_speler -= 1#er gaat een punt van de speler af zodat
                    #we dezelfde volgende stap kunnen doen van het controleren of het 
                    #een set is. Als het een set is krijgt de speler namelijk een punt
                    print(keuze_pc())#print commando dat nog weg kan
    
                    #probleem is nu nog wel dat, als we score gaan doen, dit niet hier al iets met score doet en er dus nog steeds Heel goed! geprint wordt.
                    #niet moeilijk op te lossen maar dat zit dus hier
            if len(keuze) == 3:  
                if keuze[0].isset(keuze[1], keuze[2]):
                    print('Heel goed!', len(deck))
                    #als er een set gekozen is dan reset de timer
                    counter = 0
                    klaar = False
                    if deck == []:
                        if aflegstapel==[]:
                            #print(score)
                            #hij print nu wel een score maar blijft doorlopen, verder makkelijk aan te passen maar ik ben klaar voor de dag
                            done = True
                            break
                            #hier willen we zeggen dat het spel stopt. Goed nieuws we mogen stoppen als deck leeg is en niet pas als er geen sets meer zijn.
                            #misschien kunnen we hier toevoegen iets van Print("Score :" + Score)
                            #dit moeten we dan waarschijnlijk wel weer inladen dus.
                            #ik weet nog niet of dit werkt eigenlijk want heb nog niet op dit punt gezeten
                            #ja het werkt
                        else:
                            deck = aflegstapel
                            aflegstapel = []
                    hand = aanvullen()         
                    for i in range(3):
                        speelbord[getallen[i]] = hand[i]
                    #weer nieuwe bord inladen
                    screen.blit(tabletop, (0,0))
                    for j in range(3):
                        for i in range(4):    
                            laden = pygame.image.load(card_file(speelbord[i+4*j]))
                            laden = pygame.transform.scale(laden, (100,200))
                            screen.blit(laden, (i*110 + 20, j*210 + 20))
                    makenumbers()
    #                pygame.display.flip()
                    score_speler += 1
    
                    keuze = []
                    getallen=[]
                else:
                    print('fout')
                    #als je een verkeerde set kiest dan gaat er een seconde van je denktijd af
                    counter += 10
                    #om de bar niet te lang te maken en de if statement bovenaan niet
                    #oneindig door te laten lopen hier terug zetten op de max
                    if gekozenniveau == 1:
                        if counter >= 300:
                            counter = 300
                    elif gekozenniveau == 2:
                        if counter >= 150:
                            counter = 150
                    elif gekozenniveau == 3:
                        if counter >= 50:
                            counter = 50   
                    keuze = []
                    getallen=[]
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
    
    while done: #eindscherm wordt wel gemaakt maar als we eruit gaan gaan we niet goed terug naar main
        screen.fill((255, 255, 255))
        button_aftiteling = pygame.draw.rect(screen, pink, (350, 240, 150, 75))
        aftiteling = font.render('Opnieuw spelen', True, black)
        screen.blit(aftiteling, (350,250))
        clock.tick(4)
        pygame.display.flip()
        
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            """mouse_aftiteling = pygame.mouse.get_pos()
            if 350 <= mouse_aftiteling[0] <= 500 and 240 <= mouse_aftiteling[1] <= 315:
                print('gehaald')
                #als het goed is moeten we done weer op False zetten
                done = False
                return 
            """
            main()
            done = False
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
# ga dit een keer af en kijk waar je eindigt        
main()