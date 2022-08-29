#Lin Chen
#Screensaver

import pygame, sys, random
from pygame import Vector2

pygame.init()
cell_size = 40
cell_num = 20
screen = pygame.display.set_mode((cell_size * cell_num*1.5, cell_size *cell_num))
clock = pygame.time.Clock()



class BLOCK:
    def __init__(self):
        self.randomize()
        self.block_surface = pygame.Surface((cell_size,cell_size))
        self.block_rect = self.block_surface.get_rect(center = (self.pos.x-1,self.pos.y-1))
        self.x_move = 2
        self.y_move = 2
    #draw block
    def draw_block(self):
        pygame.draw.rect(screen, pygame.Color('pink'),self.block_rect)

    #randomize where the block first starts from
    def randomize(self):
        self.x = random.randint(0,cell_size * cell_num-1)
        self.y = random.randint(0,cell_size * cell_num-1)
        self.pos = Vector2(self.x,self.y)
        
    #moves the block 
    def move(self):
        self.block_rect.x += self.x_move
        self.block_rect.y += self.y_move
         
    def collision(self):
        if self.block_rect.right >= cell_size * cell_num*1.5 or self.block_rect.left <= 0:
            self.x_move *= -1
        if self.block_rect.bottom >= cell_size * cell_num or self.block_rect.top <= 0:
            self.y_move *= -1
            
block = BLOCK()
block2 = BLOCK()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color('black'))
    block.draw_block()
    block.move()
    block.collision()
    block2.draw_block()
    block2.move()
    block2.collision()

    pygame.display.update()
    clock.tick(60)