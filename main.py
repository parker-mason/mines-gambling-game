import pygame #fuck you andrew, you are demoted to my 5th favorite black person, you should give me sloppy slop in the bathroom to compensate for your errors, I will taste your insides. - Parker Ray Mason 

pygame.init()

class Sprite(pygame.sprite.Sprite):
  def __init__(self, image):
    super().__init__()
    self.image = pygame.image.load(image)

BACKGROUND_COLOR = (39, 48, 46)
GEM_WIDTH = 144
GEM_HEIGHT = 144
MAX_GEM_COUNT = 25
MAX_GEMS_TO_PRINT = 5

WINDOW_HEIGHT = 900
WINDOW_LENGTH = 1200
HORIZONTAL_PADDING = 80
VERTICAL_PADDING = 30

gem_counter = MAX_GEM_COUNT
gems_to_print = MAX_GEMS_TO_PRINT
can_print = True
x = 0
y = 0

gem = Sprite("Assets/Gem.png")

def load_sprite(sprite, x, y):
  screen.blit(sprite.image, (x, y))
  
screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

screen.fill(BACKGROUND_COLOR)

running = True

while running:

  if gems_to_print == MAX_GEMS_TO_PRINT:
    x += HORIZONTAL_PADDING
    y += VERTICAL_PADDING
    gems_to_print -= 1
    can_print = True
  elif gems_to_print > 0:
    x += GEM_WIDTH + HORIZONTAL_PADDING
    gems_to_print -= 1
  else:
    x = 0
    y += GEM_HEIGHT
    gems_to_print = MAX_GEMS_TO_PRINT
    can_print = False
  if gem_counter > 0 and can_print:
    load_sprite(gem, x, y)
    gem_counter -= 1

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

