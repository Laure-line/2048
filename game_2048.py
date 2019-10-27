#Projet informatique 2048
#HANNA Emile - PROUVOST Laureline
#PeiP A Groupe 13

#Note : la premiere coordonnee correspond a la ligne et la seconde correspond a la colone

from random import *

combinaisons=[[[0, 0, 0, 0],0],
              [['2', 0, 0, 0],2],
              [['4', 0, 0, 0],4],
              [['8', 0, 0, 0],8],
              [['1', '6', 0, 0],16],
              [['3', '2', 0, 0],32],
              [['6', '4', 0, 0],64],
              [['1', '2', '8', 0],128],
              [['2', '5', '6', 0],256],
              [['5', '1', '2', 0],512],
              [['1', '0', '2', '4'],1024],
              [['2', '0', '4', '8'],2048],
              [['4', '0', '9', '6'],4096]]

nom_chimie=[[0,0],[2,'H'],[4,'He'],[8,'Li'],[16,'Be'],[32,'B'],[64,'C'],[128,'N'],[256,'O'],[512,'F'],[1024,'Ne'],[2048,'Na'],[4096,'Mg']]

themes=['chimie','2048']

def get_new_position(grid):
        """
        parametre grid(list) la grille dans la quelle on cherche une case vide
        valer renvoyee (list) une liste de liste donnant les coordonnes de la case vide
        CU : grid est une grille valide
        
        Exemples:
        >>> get_new_position([[0,0,0,4],[0,0,2,8],[0,2,8,16],[2,4,32,64]])
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [2, 0]]
        >>> get_new_position([[0,2,2,4],[2,4,2,8],[2,2,8,16],[2,4,32,64]])
        [[0, 0]]
        >>> get_new_position([[2,2,2,4],[2,4,2,8],[2,2,8,16],[2,4,32,64]])
        []
        """
        res=[]
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j]==0:
                                res+=[[i,j]]
        return res

def get_new_tile():
        """
        parametre : (none) aucun
        valeure renvoyee (int) la valeur d' une nouvelle case qui est de 2 ou 4
        CU : /
        
        Exemple:
        >>> get_new_tile() in {2,4}
        True
        """
        valeur=randint(0,100)
        if valeur>=80:
                return 4
        else:
                return 2

def grid_add_new_tile(grid):
        """
        parametre grille :(list) la grille a modifier
        valeur renvoyee:(list) la nouvelle liste
        effet de bord(list) modifie la liste grid
        CU : Grid est une grille
        
        Exemple:
        >>> [[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]]!=grid_add_new_tile([[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]])
        True
        """
        liste_positions=get_new_position(grid)
        coordonnes=liste_positions[randint(0,len(liste_positions)-1)]
        grid[coordonnes[0]][coordonnes[1]]=get_new_tile()
        return grid

def grid_init(taille_grid):
        """
        C'est une fonction qui crée la grille initiale
        parametre:(none)
        valeur renvoyée:(list) renvoie la grille initiale avec une case remplie d'un 2 ou d'un 4 de façon non équiprobable
        effet de bord(none)
        CU : Aucune
        
        Exemple:
        >>> est_une_grille(grid_init(4)) and len(grid_init(4))==4
        True
        """
        return grid_add_new_tile(empty_grid(taille_grid))

def empty_grid(taille_grid):
        """
        Renvoie une grille vierge de taille taille_grid
        """
        return [[0]*taille_grid for i in range(taille_grid)]
        

def grid_print (grid,taille_grid):
        """
        parametre grid :(list) la liste a imprimer
        valeur renvoyee: (none)
        effet de bord: imprime la liste passee en parametre
        CU : /
        
        Exemple:
        >>> grid_print([[0,0,0,0],[0,0,0,0],[0,4,0,0],[0,0,0,0]],4)
        --------------------
        |    |    |    |    |
        --------------------
        |    |    |    |    |
        --------------------
        |    | 4  |    |    |
        --------------------
        |    |    |    |    |
        --------------------
        """
        tiret=taille_grid*5*'-'
        colonne='|'
        for i in grid :
                print(tiret)
                colo_imp=colonne
                for j in i :
                        if j!=0:
                                colo_imp+='{:^4d}'.format(j)+colonne
                        else :
                                colo_imp+='    '+colonne
                print(colo_imp)
        print(tiret)

def grid_get_max_value(grid):
        """
        parametre grille:(list) la grille a evaluer
        valeur renvoyee (int) la valeur maximale presente dans la grille
        effet de bord (none)
        CU : grille doit etre une grille
        
        Exemples:
        >>> grid_get_max_value([[0,0,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]])
        2048
        >>> grid_get_max_value([[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]])
        2048
        """
        max=0
        for i in grid:
                for j in i:
                        if j>=max:
                                max=j
        return max

def grid_move(grid, commande, score, taille_grid):
        '''
        parametres grille:(list) la grille a modifier
        parametre commande:(str) le mouvement a effectuer
        valeur renvoyée :(list) La grille une fois le mouvement effectué
        effet de bord :(none)
        CU : grille est une grille
            commande appartient à commands
        
        Exemples:
        >>> grid_move([[0,0,0,4],[0,0,2,8],[0,2,8,16],[2,4,32,64]],'left',0,4)
        ([[4, 0, 0, 0], [2, 8, 0, 0], [2, 8, 16, 0], [2, 4, 32, 64]], 0)
        >>> grid_move([[2,0,0,0],[2,0,2,8],[8,0,2,16],[4,2,2,32]],'left', 4,4)
        ([[2, 0, 0, 0], [4, 8, 0, 0], [8, 2, 16, 0], [4, 4, 32, 0]], 12)
        >>> grid_move([[2, 0, 0, 0],[2, 0, 2, 8],[8, 0, 2, 16],[4, 2, 2, 32]],'down',0,4)
        ([[0, 0, 0, 0], [4, 0, 0, 8], [8, 0, 2, 16], [4, 2, 4, 32]], 8)
        >>> grid_move([[2,0,0,0],[2,0,2,8],[8,0,2,16],[4,2,2,32]],'right',0,4)
        ([[0, 0, 0, 2], [0, 0, 4, 8], [0, 8, 2, 16], [0, 4, 4, 32]], 8)
        >>> grid_move([[4,0,0,4],[2,2,2,8],[0,2,8,16],[2,4,32,64]],'right',0,4)
        ([[0, 0, 0, 8], [0, 2, 4, 8], [0, 2, 8, 16], [2, 4, 32, 64]], 12)
        >>> grid_move([[2,0,0,0],[2,0,2,8],[8,0,2,16],[4,2,2,32]],'up',36,4)
        ([[4, 2, 4, 8], [8, 0, 2, 16], [4, 0, 0, 32], [0, 0, 0, 0]], 44)
        '''
        newgrid=[]
        if commande =='left':
                for ligne in grid:
                        lignebis=[]
                        for valeur in ligne:
                                if valeur!=0:
                                        lignebis+=[valeur]
                        lignefinale,score=mvt(lignebis,score,taille_grid)
                        newgrid+=[lignefinale]
        if commande=='right':
                for ligne in grid:
                        ligne=ligne[::-1]
                        lignebis=[]
                        for valeur in ligne:
                                if valeur!=0:
                                        lignebis+=[valeur]
                        lignefinale,score=mvt(lignebis,score,taille_grid)
                        lignefinale=lignefinale[::-1]
                        newgrid+=[lignefinale]
        if commande=='up':
                newgrid=empty_grid(taille_grid)
                for ligne in range(len(grid)):
                        lignebis=[]
                        for valeur in range(len(grid)):
                                if grid[valeur][ligne] !=0:
                                        lignebis+=[grid[valeur][ligne]]
                        lignefinale,score=mvt(lignebis,score,taille_grid)
                        for valeurs in range(len(lignefinale)):
                                newgrid[valeurs][ligne]=lignefinale[valeurs]
        if commande=='down':
                newgrid=empty_grid(taille_grid)
                for ligne in range(len(grid)):
                        lignebis=[]
                        for valeur in range(len(grid)):
                                if grid[valeur][ligne] !=0:
                                        lignebis+=[grid[valeur][ligne]]
                        lignebis=lignebis[::-1]
                        lignefinale,score=mvt(lignebis,score,taille_grid)
                        lignefinale=lignefinale[::-1]
                        for valeurs in range(len(lignefinale)):
                                newgrid[valeurs][ligne]=lignefinale[valeurs]
        return newgrid,score

def mvt (lignebis,score,taille_grid):
        """
        parametre lignebis:(liste) la ligne dont on effectue le mouvement vers la gauche
        valeur renvoyée : (list) la liste dont le mouvement vers la gauche a été effectué
        effet de bord : (none)
        CU : lignebis doit être une liste

        Exemples :
        >>> mvt([0,0,0,0], 0,4)
        ([0, 0, 0, 0], 0)
        >>> mvt([2,2,2,2], 0,4)
        ([4, 4, 0, 0], 8)
        >>> mvt([4,2,2,8], 0,4)
        ([4, 4, 8, 0], 4)
        >>> mvt ([4,2,4,8], 0,4)
        ([4, 2, 4, 8], 0)
        """
        i=0
        lignefinale=[]
        while i<=len(lignebis)-1:
                if i!=len(lignebis)-1 and lignebis[i]==lignebis[i+1]:
                        lignefinale+=[lignebis[i]*2]
                        score+=lignebis[i]*2
                        i+=2
                else:
                        lignefinale+=[lignebis[i]]
                        i+=1
        if len(lignebis)==1:
                lignefinale=[lignebis[0]]
        lignefinale+=(taille_grid-len(lignefinale))*[0]
        return lignefinale,score

def  is_grid_over(grid,score,taille_grid):
        """
        parametre grille: (list) la grille a evaluer
        valeur renvoyee: (bool) renvoie True si il existe encore des combinaisons possibles et False sinon
        effet de bord (none)
        CU : grille doit etre une grille
        
        Exemples:
        >>> is_grid_over([[0,0,0,0],[0,0,0,0],[0,4,0,0],[0,0,0,0]],0,4)
        False
        >>> is_grid_over([[2,2,2,4],[2,4,2,8],[2,2,8,16],[2,4,32,64]],0,4)
        False
        >>> is_grid_over([[8,16,32,4],[2,4,2,8],[4,2,8,16],[2,4,32,64]],0,4)
        True
        """
        grille,stock=grid_move(grid,'left',score, taille_grid)
        if not grid==grille:
                return False
        grille,stock=grid_move(grid,'right',score, taille_grid)
        if not grid==grille:
                return False
        grille,stock=grid_move(grid,'up',score, taille_grid)
        if not grid==grille:
                return False
        grille,stock=grid_move(grid,'down',score, taille_grid)
        if not grid==grille:
                return False 
        return True

###Extensions###

#Extension graphique

def grid_get_value(grid,i,j):
        """
        parametre grid :(list) la liste a etudier
        parametre i(int): le numerot de la ligne de cla celluele dont on cherche les coordonnes
        parametre j(int): le numerot de la colone de cla celluele dont on cherche les coordonnes
        valeur renvoyee: (int) la valeur de la cellule de coordonnes (i,j)
        CU :
        -grid est une grille valide
        i et j sont des coordonnes valides , c'est a dire des entiers comprris entre 0 et les dimensions de la grille
        
        Exemple:
        >>> grid_get_value([[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]],2,2)
        0
        """
        return grid[i][j]

#Sauvegarde et chargement de partie

def grid_frame (grid,fname,theme,score, taille_grid):
        """
        parametre grid : (list) la grille à sauvergarder
        paramètre fname : (str) le nom du fichier sous lequel est enregistré la grille
        valeur renvoyée : (None)
        CU : grid est une grille valide
        """
        sortie = open(fname,'w')
        tiret=taille_grid*5*'-'
        colonne='|'
        for i in grid :
                sortie.write(tiret)
                sortie.write('\n')
                colo_imp=colonne
                for j in i :
                        if j!=0:
                                valeur=j
                                if j<10 :
                                        colo_imp+=str(valeur)+'   '+colonne
                                else :
                                        if j<100 :
                                                colo_imp+=str(valeur)+'  '+colonne
                                        else :
                                                if j<1000 :
                                                        colo_imp+=str(valeur)+' '+colonne
                                                else :
                                                        colo_imp+=str(valeur)+colonne
                        else :
                                colo_imp+='    '+colonne
                sortie.write(colo_imp)
                sortie.write('\n')
        sortie.write(tiret)
        sortie.write('\ntaille de la grille = ')
        sortie.write(str(taille_grid))
        sortie.write('\nscore = ')
        sortie.write(str(score))
        sortie.write('\ntheme : ')
        sortie.write(theme)
        sortie.close
    
def grid_load (fname):
        """
        paramètre fname : (str) le nom d'un fichier contenant une grille de jeu valide
        valeur renvoyée : (list)
        CU : fname est un fichier valide contenant une grille valide

        Exemple :
        >>> grid=[[0, 0, 0, 0], [0, 0, 4, 2], [0, 0, 0, 0], [0, 0, 0, 8]]
        >>> score=8
        >>> theme='2048'
        >>> grid_frame(grid,'test.txt',theme,score)
        >>> load_grid,load_theme,load_score=grid_load('test.txt')
        >>> load_grid == grid
        True
        >>> load_theme == theme
        True
        >>> load_score == score
        True
        """
        entree=open(fname,'r')
        lu=entree.readlines()
        grid=[]
        theme=lu[len(lu)-1]
        theme=theme[8:]
        score=lu[len(lu)-2]
        taille_grid=lu[len(lu)-3]
        taille_grid=taille_grid[22]
        lu=lu[:len(lu)-3]
        if 'chimie' in theme :
                theme=themes[0]
        score=score[8:(len(score)-1)]
        score=int(score)
        for ligne_init in range(1,len(lu),2) :
                lues=''
                lues=lu[ligne_init].rstrip('\n')
                ligne=[]
                for m in range(len(lues)):
                        if lues[m] != '|':
                                ligne+=lues[m]
                nbre=[]
                for valeur in ligne:
                        if valeur==' ':
                                nbre+=[0]
                        else:
                                nbre+=[valeur]
                res=False
                separes=[]
                cpt=0
                while res==False :
                      separes+=[nbre[cpt:cpt+4]]
                      cpt+=4
                      if cpt>=len(nbre):
                              res=True
                ligne=[]
                for chiffres in separes:
                        res=False
                        cpt=0
                        while res==False:
                                if chiffres == combinaisons[cpt][0]:
                                        res=True
                                        ligne+=[combinaisons[cpt][1]]
                                else:
                                        cpt+=1
                grid+=[ligne] 
        return grid,theme,score,int(taille_grid)

#Calcul du score

def grid_score (grid):
        """
        parametre grid:(list) une grille de jeu
        valeur renvoyée : (int) somme des valeurs des tuiles présentes dans la grille
        CU : grid est une grille valide

        Exemple :
        >>> grid_score ([[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]])
        4106
        >>> grid_score ([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        0
        """
        score=0
        for ligne in grid :
                for valeur in ligne :
                        score+=valeur
        return score

#Thème chimie

def atomes (grid):
        """
        Exemples :
        >>> atomes([[0,2048,0,0],[0,0,0,0],[2,8,0,0],[0,2048,0,0]])
        [[0, 'Na', 0, 0], [0, 0, 0, 0], ['H', 'Li', 0, 0], [0, 'Na', 0, 0]]
        """
        newgrid=[]
        for ligne in grid :
                newligne=[]
                for valeur in ligne:
                        if valeur !=0:
                                cpt=0
                                while cpt<len(nom_chimie)-1:
                                        cpt+=1
                                        if nom_chimie[cpt][0]==valeur:
                                                newligne+=[nom_chimie[cpt][1]]
                                                cpt=len(nom_chimie)
                        else:
                                newligne+=[0]
                newgrid+=[newligne]
        return newgrid

def grid_print_atomes (grid,taille_grid):
        """
        parametre grid :(list) la liste a imprimer
        valeur renvoyee: (none)
        effet de bord: imprime la liste passee en parametre
        CU : /
        
        Exemple:
        >>> grid_print_atomes([[0,0,0,0],[0,0,0,0],[0,'Na',0,0],[0,0,0,0]],4)
        --------------------
        |    |    |    |    |
        --------------------
        |    |    |    |    |
        --------------------
        |    | Na |    |    |
        --------------------
        |    |    |    |    |
        --------------------
        """
        tiret=taille_grid*5*'-'
        colonne='|'
        for ligne in grid :
                print(tiret)
                colo_imp=colonne
                for valeur in ligne :
                        if valeur!=0:
                                variable=valeur.center(taille_grid)
                                colo_imp+=variable+colonne
                        else :
                                colo_imp+='    '+colonne
                print(colo_imp)
        print(tiret)

#Tests sur les grilles

def sont_coordonnes_valides(grid,i,j):
        """
        parametre grid(list): la liste dans laquelle on evalue les coordonnes i et j
        parametres i et j(int): les coordonnes dont on evalue la validite
        valeur renvoyee: (bool) renvoie True si i et j sont des coordonnées valides avec i le numero de ligne et j celui de la colonne
        CU:
        -grid est une grille valide
        -i et j sont des entiers
        
        Exemples:
        >>> sont_coordonnes_valides([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,0,0]],2,2)
        True
        >>> sont_coordonnes_valides([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,0,0]],10,2)
        False
        >>> sont_coordonnes_valides([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,0,0]],2,12)
        False
        """
        res=False
        if i <=len(grid)-1 and j<= len(grid[1])-1:
                res=True
        return res

def est_une_grille (liste):
        """
        parametre liste:(list) la liste a evaluer
        valeur renvoyee :(bool) renvoie true si la liste passee en parametre est une grille et false dans le cas contraire
        CU : /
        
        Exemples:
        >>> est_une_grille([(0,0),(00,)])
        False
        >>> est_une_grille([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,2,0,0]])
        True
        >>> est_une_grille([[0,0,0,0],[0,0,0,0,2],[0,0,0,0],[0,2,0,0]])
        False
        >>> est_une_grille(([0,0,0,0],[0,0,0,0,2],[0,0,0,0],[0,2,0,0]))
        False
        """
        res=True
        for i in liste :
                if len(liste)!=len(i):
                        res=False
                if type(i)!=list:
                        res=False
        if type(liste)!=list:
                res=False
        return res

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
