import pygame #fuck you andrew, you are demoted to my 5th favorite black person, you should give me sloppy slop in the bathroom to compensate for your errors, I will taste your insides. - Parker Ray Mason 

pygame.init()

class Sprite(pygame.sprite.Sprite):
  def __init__(self, image):
    super().__init__()
    self.image = pygame.image.load(image)

BACKGROUND_COLOR = (39, 48, 46)
WINDOW_HEIGHT = 900
WINDOW_LENGTH = 1200

screen = pygame.display.set_mode((WINDOW_LENGTH, WINDOW_HEIGHT))

gems = []

gem = Sprite("Assets/Gem.png")

GEM_WIDTH = 144
GEM_HEIGHT = 144
MAX_GEM_COUNT = 25
MAX_GEMS_TO_PRINT = 5
HORIZONTAL_PADDING = 80
VERTICAL_PADDING = 30
gem_counter = MAX_GEM_COUNT
x = 0
y = 0

def process_click():
  print("a gem was clicked")

def get_clicked(events):
  for event in events:
    if event.type == pygame.MOUSEBUTTONUP:
      for i in range(0, 25):
        if gems[i].collidepoint(event.pos):
          process_click()

def load_sprite(sprite, x, y):
  screen.blit(sprite.image, (x, y))
  gems.append(sprite.image.get_rect())
  gems[-(gem_counter-25)].x = x
  gems[-(gem_counter-25)].y = y

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
        load_sprite(gem, x, y)
        gem_counter -= 1
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
        
  get_clicked(events)

  pygame.display.update()

pygame.quit()