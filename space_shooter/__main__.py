# -*- coding: utf-8 -*-
"""
Created on Wed May 1 18:03:16 2021

@author: shaur
"""

from game import SpaceShooter
import pygame 
from utils import load_sprite, get_random_position
from models import Asteroid

pygame.init()
pygame.display.set_caption("Space Shooter/Survival")
clock = pygame.time.Clock()
clock.tick(120)
        
def message_to_screen(message, textfont, color):
    my_font = textfont
    my_message = my_font.render(message, 0, color)

    return my_message
    
screen = pygame.display.set_mode((800, 600))
background = load_sprite('space',False)
asteroids = []
asteroids = [Asteroid(get_random_position(screen), None) for _ in range(8)]
    
if __name__ == "__main__":
    menu = True
    selected = "Level Game"
    while menu:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "Level Game"
                    elif event.key == pygame.K_DOWN:
                        selected = "Survival Mode"
                    if event.key == pygame.K_RETURN:
                        if selected == "Level Game" or selected == "Survival Mode":
                            menu = False
                    if event.key == pygame.K_ESCAPE:
                        quit()
        
        screen.blit(background,(-400,-100))
        for game_object in asteroids:
            game_object.draw(screen)
            game_object.move(screen)
            
        title = message_to_screen("SPACE SHOOTER", pygame.font.Font(None, 100), pygame.Color('tomato'))
        controls = message_to_screen("Use The 3 arrow keys to move and SPACE to shoot,", \
                                       pygame.font.Font(None, 30), pygame.Color('tomato'))
        General = message_to_screen("Press R to replay and Esc to escape", \
                                    pygame.font.Font(None, 30), pygame.Color('tomato'))
        
        if selected == "Level Game":
            play = message_to_screen("Level Game", pygame.font.Font('freesansbold.ttf', 64), pygame.Color('white'))
        else:
            play = message_to_screen("Level Game", pygame.font.Font(None, 64), pygame.Color('tomato'))
        if selected == "Survival Mode":
            game2 = message_to_screen("Survival Mode", pygame.font.Font('freesansbold.ttf', 64), pygame.Color('white'))
        else:
            game2 = message_to_screen("Survival Mode", pygame.font.Font(None, 64), pygame.Color('tomato'))
        
        title_rect = title.get_rect()
        controls_1_rect = controls.get_rect()
        controls_2_rect = General.get_rect()
        play_rect = play.get_rect()
        quit_rect = game2.get_rect()
        display_width = 800
    
        screen.blit(title, (display_width/2 - (title_rect[2]/2), 40))
        screen.blit(controls, (display_width/2 - (controls_1_rect[2]/2), 120))
        screen.blit(General, (display_width/2 - (controls_2_rect[2]/2), 140))
        screen.blit(play, (display_width/2 - (play_rect[2]/2), 200))
        screen.blit(game2, (display_width/2 - (quit_rect[2]/2), 260))
        pygame.display.update()
        pygame.display.flip()
        
    x = 1 if selected == "Level Game" else 2
    if x == 1:
        print('LEVEL - 1',end = "")
        space_rocks = SpaceShooter(1)
        space_rocks.main_loop()
        print('Completed!')
        print('LEVEL - 2',end = "")
        space_rocks = SpaceShooter(2)
        space_rocks.main_loop()
        print('Completed!')
        print('LEVEL - 3')
        space_rocks = SpaceShooter(3)    
        space_rocks.main_loop()
        print('Congratualtion You Completed the game ')
    if x == 2:
        space_rocks = SpaceShooter(2, True)
        space_rocks.main_loop()