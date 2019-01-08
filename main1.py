#!/bin/python
# -*- coding: utf-8 -*-

import os
from string import ascii_uppercase
import random

def round(joueur, grid):
    print("Joueur", joueur, "joue")
    coord_valid = False

    while not coord_valid:
        coord_valid = True

        coord = input("Entrez les coordonées de votre coup : ")
        
        line = coord[0]
        col=coord[1]

        if line == 'a' or line == 'A':
            line = 0
        elif line == 'b' or line == 'B':
            line = 1
        elif line == 'c' or line == 'C':
            line = 2
        else:
            coord_valid = False

        if (coord[1] >= '1') and (coord[1] <= '3'):
            col = int(col)-1
        else:
            coord_valid = False
        
        if coord_valid and grid[line][col] != ' ':
            coord_valid = False
        
    grid[line][col]=joueur

def bot_round(joueur, grid):
    coord_valid = False
    
    while not coord_valid:
        line = random.randint(0, 2)
        col = random.randint(0, 2)
        
        if grid[line][col] == ' ':
            coord_valid = True
        
    grid[line][col]=joueur

def clear_grid():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_grid(grid):
    print("    1   2   3")
    print("  +---+---+---+")
    i = 0
    for line in grid:
        print(ascii_uppercase[i], '| ', end='')
        i += 1 # i = i + 1
        for element in line:
            print(element, '| ', end='')
        print("\n  +---+---+---+")

def is_end(grid):
    end=False
    winner=""

    for i in range(3):
        if grid[i][0] != ' ' and grid[i][0]==grid[i][1] and grid[i][0]==grid[i][2]:
            end=True
            winner=grid[i][0]

    for i in range(3):
        if grid[0][i] != ' ' and grid[0][i]==grid[1][i] and grid[0][i]==grid[2][i]:
            end=True
            winner=grid[0][i]
    
    if grid[0][0] != ' ' and grid[0][0] == grid[1][1] and grid[0][0] == grid[2][2]:
        end=True
        winner=grid[0][0]
    if grid[0][2] != ' ' and grid[0][2] == grid[1][1] and grid[0][2] == grid[2][0]:
        end=True
        winner=grid[0][2]

    empty_element = False
    for line in grid:
        for element in line:
            if element == ' ':
                empty_element = True
    
    if empty_element == False:
        end = True

    if end and winner != "":
        print ("Le gagnant est", winner)
    elif end:
        print("Ex aequo, pas de gagnant")

    return end
    
def switch_player(current_player):
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    
    return current_player

def main():
    grid = [ [' '] * 3 for i in range(3) ]
    end = False
    current_player = "X"

    valid_player_number = False
    
    while not valid_player_number :
        player_number = input("Nombre de joueurs ?: ")
        
        if (player_number >= '0') and (player_number <= '2'):
            player_number = int(player_number)
            valid_player_number = True

    #clear_grid()
    show_grid(grid)
    
    while not end:
        if (player_number<2 and current_player == "X") or (player_number<1 and current_player == "O"):
            bot_round(current_player, grid)
        else:
            round(current_player, grid)
        #clear_grid()
        show_grid(grid)
        end = is_end(grid)
        current_player = switch_player(current_player)

if __name__ == "__main__":
    main()
