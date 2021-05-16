# -*- coding: utf-8 -*-
"""
Created on Wed May 1 17:58:36 2021

@author: shaur
"""
import pygame
import time
from utils import get_random_position, load_sprite, print_text, score, Hscore
from models import GameObject
from models import Asteroid, Spaceship
from pygame.math import Vector2

class SpaceShooter:
    MIN_ASTEROID_DISTANCE = 250 # distance the asteroid must leave in between them to save the 
                                # ship from destroyed the very instance the game is turned on.
    def __init__(self, level, survival = False, highscore = -1):
        self._init_pygame()
        
        self.flag = True
        self.survival = survival
        self.highscore = highscore
        self.score = 0
        self.level = level
        
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        
        self.screen = pygame.display.set_mode((800, 600)) # width 800 pixels and height 600 
        self.background = load_sprite('space',False)
        self.clock = pygame.time.Clock()
        
        #self.asteroids = [Asteroid((0, 0)) for _ in range(6)]
        self.asteroids = [] #[Asteroid(get_random_position(self.screen)) for _ in range(6)]
        self.bullets = []
        self.Destruct = GameObject((400,300), load_sprite("explosion"), Vector2(0))
        self.spaceship = Spaceship((400, 300), self.bullets.append)
        
        if level == 1: 
            n = 6
        elif level == 2:
            n = 8
        else:
            n = 10
        for _ in range(n):
            while True:
                position = get_random_position(self.screen)
                if (position.distance_to(self.spaceship.position)> self.MIN_ASTEROID_DISTANCE):
                    break
            self.asteroids.append(Asteroid(position, self.asteroids.append))
        
        # self.asteroid = GameObject(
        #     (400, 300), load_sprite("asteroid"), (1, 0)
        # )

    def main_loop(self):
        while self.flag:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            
    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption("Space Shooter/Survival")

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN ## to check input is from keyboard
                                             and event.key == pygame.K_ESCAPE):
                quit()
                
            is_key_pressed = pygame.key.get_pressed()
            if is_key_pressed[pygame.K_r]:
                if self.survival == True:
                    self.__init__(2,True,highscore=self.highscore)
                else:
                    self.__init__(self.level)
            pygame.key.set_repeat(20)
            if self.spaceship:
                if is_key_pressed[pygame.K_RIGHT]:
                    self.spaceship.rotate(clockwise=True)    
                elif is_key_pressed[pygame.K_LEFT]:
                    self.spaceship.rotate(clockwise=False)
                if is_key_pressed[pygame.K_UP]:
                    pygame.key.set_repeat(120)
                    self.spaceship.accelerate()
                elif self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE \
                    and not self.survival:
                    pygame.key.set_repeat() 
                    self.spaceship.shoot()
                    
              
    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            game_object.move(self.screen)
        #self.spaceship.move(self.screen)
        #self.asteroid.move()
        if self.spaceship:
            for asteroid in self.asteroids:
                if asteroid.collides_with(self.spaceship):
                    self.Destruct.position = self.spaceship.position
                    self.spaceship = None
                    self.message = "You lost!"
                    break
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    asteroid.split()
                    break
        
        for bullet in self.bullets[:]:
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)
        
        if not self.asteroids and self.spaceship:
            self.message = "You won!"

    def _draw(self):
        #self.screen.fill((0, 0, 255))
        self.screen.blit(self.background,(-400,-100))
        
        # self.spaceship.draw(self.screen)
        # #self.asteroid.draw(self.screen)
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        
        if self.spaceship:
                self.score += 0.5
                if self.score > self.highscore:
                    self.highscore = self.score
        
        if self.message:
            if self.message == "You lost!":
                self.Destruct.draw(self.screen)
                for game_object in self._get_game_objects():
                    game_object.velocity = Vector2(0)
                    game_object.draw(self.screen)
                print_text(self.screen, self.message, self.font)
            if self.message == 'You won!':
                print_text(self.screen, self.message, self.font)
                pygame.display.update()  
                time.sleep(2)
                if self.level == 3:
                    self.screen.blit(self.background,(-400,-100))
                    print_text(self.screen, 'Thank You Now Try Survival Mode',self.font)
                    pygame.display.update() 
                    time.sleep(5)
                    self.flag = False
                    return 
                    
                for i in range(5):
                    self.screen.blit(self.background,(-400,-100))
                    print_text(self.screen, 'Next Level in {}'.format(5-i)+' seconds',self.font)
                    pygame.display.update()  
                    time.sleep(1)
                    
                self.flag = False
        
        if self.survival:
            score(self.screen ,self.score)
            Hscore(self.screen, self.highscore)
        pygame.display.flip()
        self.clock.tick(80)
        #print("Collides:", self.spaceship.collides_with(self.asteroid))
        
    def _get_game_objects(self):
        #return [*self.asteroids, self.spaceship] adding collision case below:
        game_objects = [*self.asteroids, *self.bullets]
        
        if self.spaceship:
            game_objects.append(self.spaceship)
        return game_objects
    
    