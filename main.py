import pygame

pygame.init()

background_color = (192, 71, 252)

color_value = 0

RED = (255, 0, 0)

screen = pygame.display.set_mode((500, 500))

screen.fill(background_color)

running = True



while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if color_value != 1:
        screen.fill(RED)
        color_value += 1
      else:
        screen.fill(background_color)
        color_value -= 1
  
  pygame.display.update()

pygame.quit()

