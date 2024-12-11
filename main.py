import pygame

pygame.init()

color_value = 0

RED = (255, 0, 0)
ORANGE = (225, 126, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (192, 71, 252)

screen = pygame.display.set_mode((500, 500))

screen.fill(PURPLE)


running = True



while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if color_value == 0:
        screen.fill(RED)
        color_value += 1
      elif color_value == 1:
        screen.fill(ORANGE)
        color_value += 1
      elif color_value == 2:
        screen.fill(YELLOW)
        color_value += 1
      elif color_value == 3:
        screen.fill(GREEN)
        color_value += 1
      elif color_value == 4:
        screen.fill(BLUE)
        color_value += 1
      elif color_value == 5:
        screen.fill(PURPLE)
        color_value = 0
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RSHIFT:
        print("Why are you using Right Shift???")
        running = False
        
  pygame.display.update()

pygame.quit()

