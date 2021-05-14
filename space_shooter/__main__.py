# -*- coding: utf-8 -*-
"""
Created on Wed May 12 18:03:16 2021

@author: shaur
"""

from game import SpaceShooter

if __name__ == "__main__":
    print('SELECT MODE: ')
    print('1. NORMAL GAME')
    print('2. SURVIVAL MODE')
    x = 2 #int(input())
    if x == 1:
        print('LEVEL - 1')
        space_rocks = SpaceShooter(1)
        space_rocks.main_loop()
        print('LEVEL - 2')
        space_rocks = SpaceShooter(2)
        space_rocks.main_loop()
        print('LEVEL - 3')
        space_rocks = SpaceShooter(3)    
        space_rocks.main_loop()
        # print("Congrates you completed the game\n  \
        #       Now you may try the survival mode without bullets try to stay\n \
        #       alive as long as you can to get high scores")
    if x == 2:
        space_rocks = SpaceShooter(2, True)
        space_rocks.main_loop()