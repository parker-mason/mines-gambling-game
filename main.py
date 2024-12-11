import pygame

pygame.init()

background_color = (192, 71, 252)

color_value = 0

screen = pygame.display.set_mode((500, 500))

screen.fill(background_color)

running = True



while running:
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if color_value == 0:
        screen.fill((255,0,0))
        color_value = color_value + 1
      elif color_value == 1:
        screen.fill(background_color)
        color_value = color_value - 1

pygame.quit()

