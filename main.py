import pygame #fuck you andrew, you are demoted to my 5th favorite black person, you should give me sloppy slop in the bathroom to compensate for your errors, I will taste your insides. - Parker Ray Mason 

import random

pygame.init()

class Sprite(pygame.sprite.Sprite):
  def __init__(self, image):
    super().__init__()
    self.image = pygame.image.load(image)

BACKGROUND_COLOR = (39, 48, 46)
WINDOW_HEIGHT = 900
WINDOW_LENGTH = 1200

screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

randmine = random.randint(1,25)

board = []
clicked_tiles = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0]

gem = Sprite("Assets/Gem.png")
mine = Sprite("Assets/Mine.png")
blank_tile = Sprite("Assets/Blank Tile.png")

GEM_WIDTH = 144
GEM_HEIGHT = 144
MAX_GEM_COUNT = 25
MAX_GEMS_TO_PRINT = 5
HORIZONTAL_PADDING = 80
VERTICAL_PADDING = 30
gem_counter = 0
x = 0
y = 0

def get_clicked(events):
  global clicked_tiles
  for event in events:
    if event.type == pygame.MOUSEBUTTONUP:
      for i in range(0, 25):
          if board[i].collidepoint(event.pos) and clicked_tiles[i] != 1:
            if i+1 == randmine:
              reload_sprite(mine, board[i].x, board[i].y)
              clicked_tiles[i] = 1
              print("you clicked a mine stupidface")
            else:
              reload_sprite(gem, board[i].x, board[i].y)
              clicked_tiles[i] = 1
              print(f"You clicked gem number {i+1}")

def load_sprite(sprite, x, y):
  global board
  screen.blit(sprite.image, (x, y))
  board.append(sprite.image.get_rect())
  board[gem_counter-1].x = x
  board[gem_counter-1].y = y

def  reload_sprite(sprite, x, y):
  screen.blit(sprite.image, (x, y))

screen.fill(BACKGROUND_COLOR)

running = True

displayed_gems = False

while running:

  if not displayed_gems:
    for i in range(0, MAX_GEMS_TO_PRINT):
      y += VERTICAL_PADDING
      for j in range(0, MAX_GEMS_TO_PRINT):
        if j == 0:
          x += HORIZONTAL_PADDING
        else:
          x += HORIZONTAL_PADDING + GEM_WIDTH
        gem_counter += 1
        load_sprite(blank_tile, x, y)
      y += GEM_HEIGHT
      x = 0
    displayed_gems = True

  keys = pygame.key.get_pressed()
  events = pygame.event.get()

  for event in events:
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RSHIFT:
        print("quit shortcut key pressed\nexiting program...")
        running = False

  if not clicked_tiles[randmine-1]:
    get_clicked(events)

  pygame.display.update()

pygame.quit()