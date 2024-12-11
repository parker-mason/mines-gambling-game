import pygame

import time

def color_advance(color_value, time_slept = 0.1):
  if color_value == 0:
    time.sleep(time_slept)
    screen.fill(RED)
    return color_value + 1
  if color_value == 1:
    time.sleep(time_slept)
    screen.fill(ORANGE)
    return color_value + 1
  if color_value == 2:
    time.sleep(time_slept)
    screen.fill(YELLOW)
    return color_value + 1
  if color_value == 3:
    time.sleep(time_slept)
    screen.fill(GREEN)
    return color_value + 1
  if color_value == 4:
    time.sleep(time_slept)
    screen.fill(BLUE)
    return color_value + 1
  if color_value == 5:
    time.sleep(time_slept)
    screen.fill(PURPLE)
    return 0

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

  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    color_value = color_advance(color_value)

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
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RSHIFT:
        print("Why are you using Right Shift???")
        running = False
        
  pygame.display.update()

pygame.quit()

