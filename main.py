import pygame #fuck you andrew, you are demoted to my 5th favorite black person, you should give me sloppy slop in the bathroom to compensate for your errors, I will taste your insides. - Parker Ray Mason 
import time
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

mines_input = 5
randmine = random.randint(1,25)

board = []
clicked_tiles = [0] * 25

gem = Sprite("Assets/Gem.png")
mine = Sprite("Assets/Mine.png")
blank_tile = Sprite("Assets/Blank Tile.png")
mine_lost = Sprite("Assets/Mine-lost.png")
lose_screen = Sprite("Assets/Lose Screen.png")
win_screen = Sprite("Assets/Win Screen.png")

GEM_WIDTH = 144
GEM_HEIGHT = 144
MAX_GEM_COUNT = 25
MAX_GEMS_TO_PRINT = 5
HORIZONTAL_PADDING = 80
VERTICAL_PADDING = 30

number_of_clicked_gems = 0
gem_counter = 0
x = 0
y = 0

def get_clicked(events):
  global clicked_tiles
  global number_of_clicked_gems
  for event in events:
    if event.type == pygame.MOUSEBUTTONUP:
      for i in range(0, 25):
          if board[i].collidepoint(event.pos) and clicked_tiles[i] != 1 and not has_won():
            for j in range(0,mines_input)
              if j+1 = mines [j]
                mine_blink(mine, board[i].x, board[i].y, 0.25)
                mine_blink(mine_lost, board[i].x, board[i].y, 0.25)
                mine_blink(mine, board[i].x, board[i].y, 0.25)
                reload_sprite(lose_screen, 0, 390)
                clicked_tiles[i] = 1
            else:
              reload_sprite(gem, board[i].x, board[i].y)
              clicked_tiles[i] = 1
              number_of_clicked_gems += 1

def load_sprite(sprite, x, y):
  global board
  screen.blit(sprite.image, (x, y))
  board.append(sprite.image.get_rect())
  board[gem_counter-1].x = x
  board[gem_counter-1].y = y

def mine_blink(sprite, x, y, time_slept):
  reload_sprite(sprite, x, y)
  time.sleep(time_slept)

def generate_mine(number_of_mines):
  mines_unused = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
  possible_mines = 25
  mines = []
  for i in range(1, number_of_mines+1):
    mine_generated = random.randint(1,possible_mines)
    mines.append(mines_unused[mine_generated-1])
    mines_unused.pop(mine_generated-1)
    possible_mines -= 1
  return mines
  
mines = generate_mine(mines_input)

def  reload_sprite(sprite, x, y):
  screen.blit(sprite.image, (x, y))
  pygame.display.update()

def has_won():
  for i in range(0, 25):
    if clicked_tiles[i] == 0 and i+1 != randmine:
      return False
  return True


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
      elif event.key == pygame.K_r:
        if True:#clicked_tiles[randmine-1]:
          board.clear()
          randmine = random.randint(1,25)
          displayed_gems = False
          gem_counter = 0
          screen.fill(BACKGROUND_COLOR)
          clicked_tiles = [0]*25
          print(f"you clicked {number_of_clicked_gems} gems!")
          print(mines)
          mines = generate_mine(mines_input)
          number_of_clicked_gems = 0
          x = 0
          y = 0
        else:
          running = False

  if not clicked_tiles[randmine-1] and displayed_gems:
    get_clicked(events)

  pygame.display.update()
  
  if has_won() and displayed_gems:
    reload_sprite(win_screen, 0, 390)


pygame.quit()
