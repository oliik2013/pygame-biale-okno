import pygame

s = pygame.display.set_mode((550, 400))
class play():
  def __init__(self):
    self.x = 0
while True:
  s.fill((255,255,255))
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()