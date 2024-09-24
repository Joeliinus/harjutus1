import pygame
pygame.init()

# define screen size
ekraan = pygame.display.set_mode([480, 720])
pygame.display.set_caption("Võlg")
taustaV = [255, 255, 255]
kirjaV = [0, 0, 0]
ekraan.fill(taustaV)

# kehtesta kirja suurus
kirja_suurus = 20
kiri = pygame.font.SysFont("Comic Sans", kirja_suurus)

# loo tühi tekstiliik
text = [""]

# teksti ekraanile lisamise funktsioon
def lisa_text(text, kiri, kirjaV, x, y):
  pilt = kiri.render(text, True, kirjaV)
  laius = pilt.get_width()
  ekraan.blit(pilt, (x - (laius / 2), y))

# toimuva püsivus
run = True
while run:

  # värskenda tausta
  ekraan.fill(taustaV)

  # näita sisestatud kirja
  for row, line in enumerate(text):
    lisa_text(line, kiri, kirjaV, 480 / 2, 60 + (row * kirja_suurus))
    lisa_text("Sisesta võlgnike andmed (€):", kiri, kirjaV, 145, 20)

  # tegemised
  for event in pygame.event.get():
    # teksti sisestamine
    if event.type == pygame.TEXTINPUT:
      text[-1] += event.text

    # handle special keys
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