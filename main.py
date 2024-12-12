import pygame

pygame.init()

class Sprite(pygame.sprite.Sprite):
  def __init__(self, image):
    super().__init__()
    self.image = pygame.image.load(image)

BACKGROUND_COLOR = (39, 48, 46)
GEM_WIDTH = 144
GEM_HEIGHT = 144
MAX_GEM_COUNT = 5
MAX_GEM_NEWLINE_COUNT = 4
WINDOW_HEIGHT = 900
WINDOW_LENGTH = 1200

HORIZONTAL_PADDING = 80
VERTICAL_PADDING = 30

gem_newline = 0
gem_counter = 5
x = 0
y = 0

gem = Sprite("Assets/Gem.png")

def load_sprite(sprite, x, y):
  screen.blit(sprite.image, (x, y))
  
screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

screen.fill(BACKGROUND_COLOR)

running = True

while running:

  if gem_counter == 5:
    x += HORIZONTAL_PADDING
    load_sprite(gem, x, y)
    gem_counter -= 1
  if gem_counter > 0:
    x += GEM_WIDTH + HORIZONTAL_PADDING
    load_sprite(gem, x, y)
    gem_counter -= 1
    if gem_counter == 0:
      gem_counter = MAX_GEM_COUNT
      x = 0
      y += GEM_HEIGHT + VERTICAL_PADDING
      gem_newline += 1
    if gem_newline > MAX_GEM_NEWLINE_COUNT:
      gem_counter = 0
      gem_newline = 0

  keys = pygame.key.get_pressed()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RSHIFT:
        print("quit shortcut key pressed\nexiting program...")
        running = False
        
  pygame.display.update()

pygame.quit()

