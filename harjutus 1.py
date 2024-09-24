import pygame
import sys
pygame.init()

class Sisend:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def liitmine(self):
        return self.x + " - " + self.y

while True:       # while tsukkel vale sisestuse jaoks
    def menuu():      # loob menuu funktsiooni
        markus = "\nKas soovid võlgniku nime ja võla sisestada? \n1 = jah, 2 = ei"
        print(markus)     # väljastab märkusele määratud teksti
    menuu()      # viitab menuu funktsioonile ja kutsub selle välja
    valitu = int(input("Avalda oma soov (1 v 2): "))     # kasutaja sisestab arvu, sisestatud arv on valituga võrdne
    valimatu = str("\nValitu ei vasta ühegi antud võimalusega!")
    valimatu2 = str("\nViimane võimalus 1 valikutest valida!")

    if valitu == 1:     # kui valitu on võrdeline arvuga 1
        x = input("\nSisesta võlgniku nimi: ")
        y = input("Ja temale kuuluv võlg: ")
        paber = Sisend(x, y)

        # määrab ekraani suuruse ning paneb sellele nime
        screen = pygame.display.set_mode([480, 720])
        pygame.display.set_caption("Võlg")
        taustaV = [255, 255, 255]
        screen.fill(taustaV)

        font = pygame.font.Font(pygame.font.match_font('Impact'), 20)  # määrab fondi ja suuruse
        ptekst = font.render("Võlgnik: " + str(paber.liitmine()), True, [0, 0, 0])  # määrab teksti ja värvi
        screen.blit(ptekst, [20, 20])  # määrab asukoha
        print("\nVõlgnik ja tema võlg: ", paber.liitmine())

        # sulgemine hiirega
        pygame.display.flip()

        while True:
            sisend = pygame.event.poll()
            if sisend.type == pygame.QUIT:
                sys.exit()

    if valitu == 2:
        break

    if valitu < 1 or valitu > 2:
        print(valimatu)
        valitu2 = int(input("Avalda oma soov (1 v 2): "))

        # määrab ekraani suuruse ning paneb sellele nime
        screen = pygame.display.set_mode([480, 720])
        pygame.display.set_caption("Võlg")
        taustaV = [255, 255, 255]
        screen.fill(taustaV)

        if valitu2 == 1:
            x = input("\nSisesta võlgniku nimi: ")
            y = input("Ja temale kuuluv võlg: ")
            paber = Sisend(x, y)

            font = pygame.font.Font(pygame.font.match_font('Futura'), 28)  # määrab fondi ja suuruse
            ptekst = font.render("Võlgnik: " + str(paber.liitmine()), True, [0, 0, 0])  # määrab teksti ja värvi
            screen.blit(ptekst, [20, 20])  # määrab asukoha
            print("\nVõlgnik ja tema võlg: ", paber.liitmine())

        if valitu == 2:
            break

        if valitu2 < 1 or valitu2 > 2:
            print(valimatu2)
            valitu3 = int(input("Avalda oma soov (1 v 2): "))

            # määrab ekraani suuruse ning paneb sellele nime
            screen = pygame.display.set_mode([480, 720])
            pygame.display.set_caption("Võlg")
            taustaV = [255, 255, 255]
            screen.fill(taustaV)

            if valitu3 == 1:
                x = input("\nSisesta võlgniku nimi: ")
                y = input("Ja temale kuuluv võlg: ")
                paber = Sisend(x, y)

                font = pygame.font.Font(pygame.font.match_font('Comic Sans'), 22)  # määrab fondi ja suuruse
                ptekst = font.render("Võlgnik: " + str(paber.liitmine()), True, [0, 0, 0])  # määrab teksti ja värvi
                screen.blit(ptekst, [20, 20])  # määrab asukoha
                print("\nVõlgnik ja tema võlg: ", paber.liitmine())

            if valitu3 < 1 or valitu3 > 1:
                break

    # sulgemine hiirega
    pygame.display.flip()

    while True:
        sisend = pygame.event.poll()
        if sisend.type == pygame.QUIT:
            sys.exit()