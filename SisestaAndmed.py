import pygame

pygame.init()

# akna parameetrid
aken = pygame.display.set_mode([480, 720])
pygame.display.set_caption("Võlg")
taustaV = [255, 255, 255]
aken.fill(taustaV)

# kirja parameetrid
kirja_suurus = 20
kirjav = [0, 0, 0]
kiri = pygame.font.SysFont("Comic Sans", kirja_suurus)

# loo tühi tekstiliik
text = [""]


# teksti aknale lisamise funktsioon
def lisa_text(text, kiri, kirjav, x, y):
    pilt = kiri.render(text, True, kirjav)
    laius = pilt.get_width()
    aken.blit(pilt, (x - (laius / 2), y))


# toimuva püsivus
run = True
while run:

    # värskenda tausta
    aken.fill(taustaV)

    # näita sisestatud kirja
    for row, line in enumerate(text):
        lisa_text(line, kiri, kirjav, 480 / 2, 60 + (row * kirja_suurus))
        lisa_text("Sisesta võlgnike andmed (€):", kiri, kirjav, 145, 20)

    # sisendid
    for event in pygame.event.get():

        # teksti sisestamine
        if event.type == pygame.TEXTINPUT:
            text[-1] += event.text

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text[-1] = text[-1][:-1]
                if len(text[-1]) == 0:
                    if len(text) > 1:
                        text = text[:-1]
            elif event.key == pygame.K_RETURN:
                text.append("")

        # sulge programm
        if event.type == pygame.QUIT:
            run = False

    # uuenda vaatevälja
    pygame.display.flip()
