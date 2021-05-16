# -*- coding: utf-8 -*-
"""
Created on Wed May 1 18:29:09 2021

@author: shaur
"""
import random
from pygame.image import load
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame import Color
from pygame.font import Font

def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()
    
def wrap_position(position, surface): # if we reach the end of screen move it to opposite end
    x, y = position 
    w, h = surface.get_size()
    return Vector2(x % w, y % h)

def get_random_position(surface):
    return Vector2(
        random.randrange(surface.get_width()),
        random.randrange(surface.get_height()),
    )

def get_random_velocity(min_speed, max_speed):
    speed = random.randint(min_speed, max_speed)
    angle = random.randrange(0, 360)
    return Vector2(speed, 0).rotate(angle)

def load_sound(name):
    path = f"assets/sounds/{name}.wav"
    return Sound(path)

def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)

def score(surface, count):
    white = (255,255,255)
    font = Font('freesansbold.ttf', 30)
    text = font.render("Score: "+str(count), True, white)
    surface.blit(text, [10,10])
    
def Hscore(surface, count):
    white = (255,255,255)
    font = Font('freesansbold.ttf', 30)
    text = font.render("High score: "+str(count), True, white)
    surface.blit(text, [530,10])