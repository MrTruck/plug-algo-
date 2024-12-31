import pygame
import random
import time

pygame.init()




WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Typer")
surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
timer = pygame.time.Clock()
fps = 60
# load assets like fonts, sound fx and music
header_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',35)
pause_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',38)
banner_font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',28)
font = pygame.font.Font('Algorithm and programing final/assets/Fonts/1up.ttf',48)



def draw_screen():
    # draw background, boxes for text, score, etc.
    pygame.draw.rect(screen, (32,42,68), [0, HEIGHT - 100, WIDTH, 100])
    pygame.draw.rect(screen,'white', [0,0, WIDTH, HEIGHT], 5)
    pygame.draw.line(screen,'white',(250, HEIGHT - 100), (250, HEIGHT), 2)
    pygame.draw.line(screen,'white',(700, HEIGHT - 100), (700, HEIGHT), 2)
    pygame.draw.line(screen,'white',(0, HEIGHT - 100), (WIDTH, HEIGHT - 100), 2)

    # text for showing the current level, player's current input, high score, score, lives, and pause



    #pause button
    


    screen.blit(banner_font.render(f'Score:', True, 'black'), (250, 10))
    screen.blit(banner_font.render(f'Best:', True, 'black'), (550, 10))
    screen.blit(banner_font.render(f'Lives:', True, 'black'), (10, 10))






run = True
while run:
    screen.fill('gray')
    timer.tick(fps)
    draw_screen()
    
    


    pygame.display.update()  

pygame.quit()          