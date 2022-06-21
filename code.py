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

def main():
    """
    geaccepteerde input definieren zodat we dit als tweede eis kunnen stellen
    aan de kaart selectie zodat het programma daar geen bug vertoont
    """
    geaccepteerde_input = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,
                           pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,
                           pygame.K_9,pygame.K_0,pygame.K_MINUS,
                           pygame.K_EQUALS]
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
            
            for i in range(4):
                if self.attributen[i] == other1.attributen[i] and self.attributen[i] == other2.attributen[i]:
                    pass
                elif self.attributen[i] != other1.attributen[i] and self.attributen[i] != other2.attributen[i] and other1.attributen[i] != other2.attributen[i]:
                    pass
                else:
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
    

    score_speler = 0
    """
    Score_speler en score_pc worden voor het spel op 0 gezet zodat nog een keer
    spelen goed werkt en neit door score door laat tellen
    """
    score_pc = 0
    deck = createdeck()
    aflegstapel=[] #een aflegstapel wordt gedefinieerd zodat het spel wat
    #langer duurt als er vaak geen set is
    
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
            trekken = random.sample(deck, k=3)
            """
            vult 3 kaarten aan als er geen set te maken is met de kaarten op
            het speelveld. Als dit het geval is willen we wel de eerste 3
            kaarten bewaren zodat we op het einde nog kunnen aanvullen
            """
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
    #naam van kleuren de bijbehorende waarde gegeven voor gemak later bij kiezen van een kleur
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
    
    pygame.display.flip() #hier wordt het startscherm geprojecteert op het scherm
    
    while True:
        """
        Er wordt over het startscherm heen geprint zodra er een keuze is gemaakt
        voor het niveau. Hiervoor wordt gekeken naar de positie van de muis.
        Zodra de keuze is gemaakt krijgt gekozen niveau de bijbehorende waarde
        en gaan we uit deze loop met een break commando
        """
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
    
    #begin code timer
    clock = pygame.time.Clock()
    counter = 0
    pygame.time.set_timer(pygame.USEREVENT,100)
    achtergrondbar = pygame.image.load("blackbar.png")
    achtergrondbar = pygame.transform.scale(achtergrondbar,(50,300))
    achtergrondscore = pygame.image.load("zwartblok.png")
    achtergrondscore = pygame.transform.scale(achtergrondscore , (250,100))
    
    
    laadbar = pygame.draw.rect(screen, pink, pygame.Rect(0,0,0,0))
    pygame.display.flip()
    
# lengte van het increment gekozen zodat een volle laadbar overeen komt met een
# timer die klaar is    
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
    
    
    startset = starten()
    speelbord = startset
    
    def herladen():
        """
        Een korte definitie voor het herladen van de kaarten die op dit moment
        op het speelveld liggen zodat deze later aangeroepen kan worden voor
        beter overzicht

        """        
        for j in range(3):
            for i in range(4):    
                laden = pygame.image.load(card_file(startset[i+4*j]))
                laden = pygame.transform.scale(laden, (100,200))
                screen.blit(laden, (i*110 + 20, j*210 + 20))
        
        makenumbers()
    herladen() #flip    
        ### Update display
    pygame.display.flip()
    
    keuze = []
    def totale_controle():
        sets=[]
        for i in range(10):#moet dus 1t/m 10 zijn
            keuze1=i
            for j in range(i+1,11): #i+1 t/m 11
                keuze2=j
                for k in range(j+1,12): #j+1 t/m 12
                    keuze3=k
                    if speelbord[keuze1].isset(speelbord[keuze2], speelbord[keuze3]):
                        sets.append([i+1,j+1,k+1])
        return sets
    def keuze_pc():
        keuze = totale_controle()[0]
        return keuze
    
    getallen=[]
    klaar = False #de timer die op is
    eindscherm = True
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT and not klaar:
                if counter == 0:
                    screen.blit(achtergrondbar, (600, 100))
    
    
                counter += 1
                laadbar = pygame.draw.rect(screen, black, pygame.Rect(610,115,30, counter*stukjeerbij))
                text_ss = font.render('jouw score : ' + str(score_speler), True, black)
                text_spc = font.render('computer score : ' + str(score_pc) , True, black)
                screen.blit(achtergrondscore , (500 , 440))
                screen.blit(text_ss, (510,450))
                screen.blit(text_spc, (510,500))
                pygame.display.flip()
    #            if counter == 0:
    #                screen.blit(achtergrondbar, (450, 50))
    
                if gekozenniveau == 1:
                    if counter >= 300:
                        klaar = True
                        break
                elif gekozenniveau == 2:
                    if counter >= 150:
                        klaar = True
                        break
                elif gekozenniveau == 3:
                    if counter >= 50:
                        klaar = True
                        break
            elif event.type == pygame.KEYDOWN and event.key in geaccepteerde_input:
                if event.key == pygame.K_1:
                    nr = 0
                elif event.key == pygame.K_2:
                    nr = 1
                elif event.key == pygame.K_3:
                    nr = 2
                elif event.key == pygame.K_4:
                    nr = 3
                elif event.key == pygame.K_5:
                    nr = 4
                elif event.key == pygame.K_6:
                    nr = 5
                elif event.key == pygame.K_7:
                    nr = 6
                elif event.key == pygame.K_8:
                    nr = 7
                elif event.key == pygame.K_9:
                    nr = 8
                elif event.key == pygame.K_0:
                    nr = 9
                elif event.key == pygame.K_MINUS:
                    nr = 10
                elif event.key == pygame.K_EQUALS:
                    nr = 11
                #Deze moeten we denk ik eerst doen als de tijd om is en dan specifiek
       
                kaart1 = speelbord[nr]
                if kaart1 in keuze:
                    keuze.remove(kaart1)
                    getallen.remove(nr)
                    kaartje = pygame.image.load(card_file(speelbord[nr]))
                    screen.blit(kaartje, (20 + 110 * (nr%4), 20 + 210 * (nr//4)))
                    pygame.display.flip()
                else:    
                    keuze.append(kaart1)
                    getallen.append(nr)
                    geselecteerd = pygame.image.load('selectedcard.png')
                    geselecteerd = pygame.transform.scale(geselecteerd, (100,200))
                    screen.blit(geselecteerd, (20 + 110 * (nr%4), 20 + 210 * (nr//4)))
                pygame.display.flip()
                #elif event.key == pygame.K_s:
    #dit is de keuze die de computer maakt, nogmaals dit moet alleen gebeuren als er een keuze is maar dan doet ie het goed
    #Dit moet dus wel op een timer en niet op een keypress.
    #ook moeten we hier toevoegen dat de computer een punt krijgt, of dat er een punt van het totaal af gaat als dat makkelijker is                
            if klaar:
                print(totale_controle())
                if totale_controle() == []:
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
                            """
                            hand = vervangen()
                            getallen=[0,1,2] #deze zouden we kunnen evrvangen als we ze op een specifieke plek willen of evt zelf willekeurig
                            screen.blit(tabletop, (0,0))
                            for i in range(3):
                                speelbord[getallen[i]] = hand[i]
                            """
                    else:
                        hand = vervangen()
                        getallen=[0,1,2] #deze zouden we kunnen evrvangen als we ze op een specifieke plek willen of evt zelf willekeurig
                        screen.blit(tabletop, (0,0))
                        for i in range(3):
                            speelbord[getallen[i]] = hand[i]
                    
                #hier zet het ding de nieuwe kaarten op de goede plek   
                    herladen()
    #                pygame.display.flip()
                    counter = 0
                    klaar = False
                else:
                    getallen= []
                    keuze = []
                    kaart10 = startset[keuze_pc()[0]-1]
                    keuze.append(kaart10)
                    getallen.append(keuze_pc()[0]-1)
                    kaart11 = startset[keuze_pc()[1]-1]
                    keuze.append(kaart11)
                    getallen.append(keuze_pc()[1]-1)
                    kaart12 = startset[keuze_pc()[2]-1]
                    keuze.append(kaart12)
                    getallen.append(keuze_pc()[2]-1)
                    score_pc += 1
                    score_speler -= 1
                    print(keuze_pc())
    
                    #probleem is nu nog wel dat, als we score gaan doen, dit niet hier al iets met score doet en er dus nog steeds Heel goed! geprint wordt.
                    #niet moeilijk op te lossen maar dat zit dus hier
            if len(keuze) == 3:  
                if keuze[0].isset(keuze[1], keuze[2]):
                    print('Heel goed!', len(deck))
                    #als er een set gekozen is dan reset de timer
                    counter = 0
                    klaar = False
                    score_speler += 1
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
                    herladen()
    #                pygame.display.flip()
                    
    
                    keuze = []
                    getallen=[]
                else:
                    print('fout')
                    counter += 10
                    #zodat de bar niet te lang wordt
                    if gekozenniveau == 1:
                        if counter >= 300:
                            counter = 300
                    elif gekozenniveau == 2:
                        if counter >= 150:
                            counter = 150
                    elif gekozenniveau == 3:
                        if counter >= 50:
                            counter = 50
                            
                    # kaarten terug blitten
                    herladen()
                    keuze = []
                    getallen=[]
                    #ik weet ook niet of we hier nog iets mee moeten met punt/tijdsaftrek. (1sec eraf?)
                    #maar dat is misschien onnodig moeilijk
        #hier nieuw keuze scherm
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                sys.exit()
    
    while done:
        screen.fill((255, 255, 255))
        button_eindscore = pygame.draw.rect(screen, pink, (150, 40, 500, 75))
        eindscore = font.render('score computer :' + str(score_pc) + '     score speler :' + str(score_speler), True, black)
        screen.blit(eindscore, (190,50))
        button_aftiteling = pygame.draw.rect(screen, pink, (200, 240, 400, 75))
        aftiteling = font.render('Opnieuw spelen', True, black)
        screen.blit(aftiteling, (300,270))
        stop_knop = pygame.draw.rect(screen, pink, (200, 440, 400, 75))
        stoppen = font.render('Spel afsluiten', True, black)
        screen.blit(stoppen, (300,470))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_aftiteling = pygame.mouse.get_pos()
                if 200 <= mouse_aftiteling[0] <= 600 and 240 <= mouse_aftiteling[1] <= 315:
                    return main()
                elif 200 <= mouse_aftiteling[0] <= 600 and 440 <= mouse_aftiteling[1] <= 515:
                    pygame.quit()
                    sys.exit()
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
        
while True:
    main()