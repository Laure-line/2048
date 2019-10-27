#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2017, march

ON PEUT CHOISIR SAUVEGARDE OU PAS, THEME, TAILLE

"""

from game_2048 import *

commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down", "S" : "save" }
answers = {"N" : "new", "L" : "load" }
end_game = {"Y" : "yes", "N" : "no"}
les_themes= {"C": 'chimie', "2048" : "2048" }
themes=['chimie','2048']

def read_next_move():
    """
    read a new move
    valeur renvoyée : l'action à effectuer

    CU: /
    """
    res=False
    while res==False:
        entree=input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight), (S)ave ')
        if entree.upper() in commands:
            res=True
    return entree.upper()

def start ():
    """
    détermine la grille de départ
    valeur renvoyée : (list) la grille de jeu
    CU : /
    """
    res=False
    while res==False:
        entree=input('Do you want to start a new party or load an old one ? (N)ew, (L)oad ')
        if entree.upper() in answers:
            res=True
    if res==True :
        if entree.upper()=='L':
            fname=input("Please enter grid file's name :")
            grid,theme,score,taille_grid=grid_load(fname)
            print("score jeu = ",score)
            print("score attendu = ",grid_score(grid))
        else:
            score=0
            res=False
            while res==False:
                entree=input('Voulez vous jouer à (C)himie ou à (2048) ? ')
                if entree.upper() in les_themes :
                    res=True
            test=False
            inter_grid = list(range(2,100))
            interv_grid = [str(j) for j in inter_grid]
            while test==False :
                entree_taille=input("""Please choose the size of the grid you want to play on : (2, 3, 4, ..., infini)
remarque : une grille trop volumineuse ne permettra pas une bonne visibilité : """)
                if entree_taille in interv_grid :
                    test=True
            if int(entree_taille) > 1 :
                taille_grid=int(entree_taille)
                    
            if res==True:
                grid = grid_init(taille_grid)
                if entree.upper() == 'C':
                    theme=themes[0]
                else:
                    theme=themes[1]
    return grid , theme, score, taille_grid

def play():
    """
    main game procedure
    
    """

    grid, theme,score, taille_grid = start()
    if theme==themes[0]:
        grid_print_atomes(atomes(grid), taille_grid)
    else :
        grid_print(grid, taille_grid)
    while not is_grid_over(grid, score, taille_grid) and grid_get_max_value(grid) < 2048:
        move = read_next_move()
        if move.upper() == 'S':
            name = input("Please give a name with the extension '.txt' to your file (ex : mygame.txt) : ")
            grid_frame(grid,name,theme,score, taille_grid)
            res = False
            while res == False :
                end = input("Do you want to keep playing ? (Y)es , (N)o ")
                if end.upper() in end_game :
                    res = True
            if end.upper() == "N":
                print("It was a pleasure to play with you, see you later !")
                break
            else :
                print("Nice to see you'll still be with us for now, here is a recall of your game ")
                if theme==themes[0]:
                    grid_print_atomes(atomes(grid), taille_grid)
                else :
                    grid_print(grid, taille_grid)
                print("score jeu = ",score)
                print("score attendu = ",grid_score(grid))
        else:
            test=(grid,score)
            while test == grid_move(grid, commands[move], score, taille_grid):
                move = read_next_move()
            grid, score = grid_move(grid, commands[move], score, taille_grid)
            grid_add_new_tile(grid)
            if theme == themes[0] :
                grid_print_atomes(atomes(grid), taille_grid)
            else :
                grid_print(grid, taille_grid)
            print("score jeu = ",score)
            #score jeu correspond au score affiché dans le jeu original
            print("score attendu = ",grid_score(grid))
            #score attendu correspond au score tel qu'il est demandé pour le projet
    if grid_get_max_value(grid) == 2048:
        print("You Won !!")
    else:
        print("You Lose ;-(")


def usage():
    print('Usage : {:s}'.format(sys.argv[0]))
    exit(1)

if __name__ == '__main__':
    import sys

    play()
    exit(0)

