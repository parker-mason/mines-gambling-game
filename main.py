import pygame

pygame.init()

background_color = (192, 71, 252)

screen = pygame.display.set_mode((500, 500))

screen.fill(background_color)

running = True

while running:
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

pygame.quit()