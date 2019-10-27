from tkinter import *
from tkinter.filedialog import *
from textual_2048 import *
from game_2048 import *

### INITIALISATION ###

fenetre1 = Tk()

# Choix du theme
theme_label = Label(fenetre1, text = "Choisissez un thème")
theme_label.pack()

photo = PhotoImage(file = os.path.join('images', 'chimie.1.gif'))
canvas = Canvas(fenetre1,width=205, height=120)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.pack()

def result_theme ():
   if 'Chimie' == str(var_theme.get()) :
      theme = 'Chimie'
   elif '2048' == str(var_theme.get()) :
      theme = '2048'
   return theme

var_theme = StringVar()

choix_chimie = Radiobutton(fenetre1, text = "Chimie", value = "Chimie", variable = var_theme, command = result_theme)
choix_2048 = Radiobutton(fenetre1, text = "2048", value = "2048", variable = var_theme, command = result_theme)

choix_chimie.pack()
choix_2048.pack()

# Choix de la taille de grille
champ_label = Label(fenetre1, text = "Choisissez la taille de la grille")
champ_label.pack()

photo2 = PhotoImage(file = os.path.join('images', '2x2.1.gif'))
canvas = Canvas(fenetre1,width=200, height=100)
canvas.create_image(0, 0, anchor=NW, image=photo2)
canvas.pack()

def result_taille ():
   taille = 0
   if '2x2' == str(var_taille.get()) :
      taille = 2
   elif '3x3' == str(var_taille.get()) :
      taille = 3
   else :
      taille = int(var_taille.get())
   return taille


var_taille = StringVar()
choix_taille_2 = Radiobutton(fenetre1, text = "2x2", variable = var_taille, value = "2x2", command = result_taille)
choix_taille_3 = Radiobutton(fenetre1, text = "3x3", variable = var_taille, value = "3x3", command = result_taille)
champ_label = Label(fenetre1, text = "Autre taille (si vous voulez que ca dure tres tres longtemps)")
ligne_texte1 = Entry(fenetre1, text = "?x?", textvariable=var_taille, width=30)

choix_taille_2.pack()
choix_taille_3.pack()
champ_label.pack()
ligne_texte1.pack()
    
bouton_quitter = Button(fenetre1, text = "Suivant", command = fenetre1.quit)
bouton_quitter.pack()

fenetre1.mainloop()
fenetre1.destroy()

### CARACTERISTIQUES DE LA GRILLE DE JEU

theme, taille_grid = result_theme(), result_taille()

fenetre = None
grid = None
gr_grid = []

#################################### ICI COMMENCE REELLEMENT LE TRAITEMENT DE L'INTERFACE GRAPHIQUE DU JEU##################################################

TILES_BG_COLOR = {   2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 
                  16:"#f59563", 32:"#f67c5f", 64:"#f65e3b",
                  128:"#edcf72", 256:"#edcc61", 512:"#edc850", 
                  1024:"#edc53f", 2048:"#edc22e", 4096:"#edc01e" }

TILES_FG_COLOR = { 2:"#776e65", 4:"#776e65", 8:"#f9f6f2", 16:"#f9f6f2", \
                   32:"#f9f6f2", 64:"#f9f6f2", 128:"#f9f6f2", 256:"#f9f6f2", \
                   512:"#f9f6f2", 1024:"#f9f6f2", 2048:"#f9f6f2", 4096:"#f9f6f2" }

CHIMIE = { 2 : 'H', 4 : 'He', 8 : 'Li', 16 : 'Be', 32 : 'B', 64 : 'C', 128 : 'N', 256 : 'O', 512 : 'F', 1024 : 'Ne', 2048 : 'Na', 4096 : 'Mg'}

TILE_EMPTY_BG = "#9e948a"
TILES_FONT = {"Verdana", 40, "bold"}

GAME_SIZE = 600
GAME_BG = "#92877d" 
TILES_SIZE = GAME_SIZE // 4

  
commands = { "Up" : "up", "Left" : "left", "Right" : "right", "Down" : "down" }

def main():
    """
    launch the graphical game
    
    UC : none
    """
    global fenetre, gr_grid, grid
    fenetre = Frame()
    fenetre.grid()
    fenetre.master.title('2048')
    fenetre.master.bind("<Key>", key_pressed)
    background = Frame(fenetre, bg = GAME_BG,
                       width=GAME_SIZE, height=GAME_SIZE)
    background.grid()
    gr_grid = []
    for i in range(taille_grid):
        gr_line = []
        for j in range(taille_grid):
            cell = Frame(background, bg = TILE_EMPTY_BG,
                         width = TILES_SIZE, height = TILES_SIZE)
            cell.grid(row=i, column=j,padx=1, pady=1)
            t = Label(master = cell, text = "", bg = TILE_EMPTY_BG,
                      justify = CENTER, font = TILES_FONT,
                      width=4, height=2)
            t.grid()
            gr_line.append(t)
        gr_grid.append(gr_line)
    grid = grid_init(taille_grid)
    grid_display(grid, theme)
    
    fenetre.mainloop()
   

def grid_display(grid, theme):
    """
    graphical grid display
    
    UC : none
    """
    global gr_grid, fenetre
    for i in range(taille_grid):
        for j in range(taille_grid):
            number= grid_get_value(grid,i,j)
            if number == 0:
                gr_grid[i][j].configure(text="", bg=TILE_EMPTY_BG)
            elif theme == '2048' :
                gr_grid[i][j].configure(text=str(number), 
                                        bg=TILES_BG_COLOR[number],
                                        fg=TILES_FG_COLOR[number])
            elif theme == 'Chimie' :
               gr_grid[i][j].configure(text=CHIMIE[number], 
                                        bg=TILES_BG_COLOR[number],
                                        fg=TILES_FG_COLOR[number])
    fenetre.update_idletasks()
    print("score attendu = ",grid_score(grid))

def key_pressed(event):
    """
    key press event handler
    
    UC : none
    """
    global fenetre, grid
    
    key = event.keysym
    score=0
    av_grid=[]
    ap_grid=[]
    for ligne in grid :
        for valeur in ligne :
            av_grid+=[valeur]
    if key in commands:
        grid,score = grid_move(grid, commands[key],score, taille_grid)
        print("score jeu = ",score)
        for ligne in grid :
            for valeur in ligne :
                ap_grid+=[valeur]
        if av_grid!=ap_grid:
            grid_add_new_tile(grid)
            grid_display(grid,theme)
        if is_grid_over(grid,score,taille_grid):
            print("You loose !!!")
            #Bon la ligne d'apres ferme la fenetre mais apres y'a une erreur quand meme
            
            #t_as_perdu(grid,score,taille_grid)
            #bouton_quitter = Button(fenetre, text = "Suivant", command = fenetre1.quit)
            #bouton_quitter.pack()
            fenetre.destroy()
        if grid_get_max_value(grid) == 2048:
            print("You win !!!")
            grid_display(grid,theme)

def t_as_perdu (grid,score,taille_grid):
   fenetre2 = Tk()
   message = Label(fenetre2, text = "Bah t'as perdu la en fait")
   message.pack()
   
        
if __name__ == '__main__':
    import sys

    main()
    #exit(0)
