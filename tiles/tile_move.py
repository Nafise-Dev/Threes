from random import randint
from tiles.tile_acces import *
from life_cycle.cycle_game import *
#########################################
####       Foncton de la partie 1   #####
#########################################

def get_nb_empty_rooms(plateau):
    """Met à jour le dictionnaire avec le nombre de case libre (s) 
    et renvoie le nombre de case libre du plateau"""
    # On parcours le tableau tiles et on compte le nombre de case contenant la valeur 0 à l'aide d'un variable nb
    nb=0
    for i in range(16):
        if plateau['tiles'][i]==0:
            nb+=1
    plateau['nb_case_libre']=nb
    return nb

#########################################
####       Foncton de la partie 2   #####
#########################################



def get_next_alea_tiles(plateau,mode):
    """Retounre une ou deux tuiles(s) dont la position est triée 
    aléatoirement et correspont à une emplacement libre du plateau
    
    plateau : dictinnaire contenant le plateau de jeu
    mode : deux modes possibles 'init' et 'encours'
    
        - 'init' : Un dictionnaire contenant deux tuiles de valeur 1 et 2.
                   La position de chaque tuile est tiré aléatoirement à un emplacelent du plateau.
                   Ce mode est utilisé lors de l'initialisation du jeu.
                   
        - 'encours' : Un dictionnaire contenant une tuile de valeur comprise entre 1 et 3 est retournée.
                      La position du tuile est tiré aléatoirement et correspond à un emplacelent libre du plateau.
                      Ce mode est utilisé en cours du jeu.
                  
    """
    # Teste si le mode est bien définit c-à-d deux modes sont possibles 'init' et 'encours'
    assert mode in ['init' ,'encours'], "Deux modes sont possibles 'init' et 'encours' (voir commentaire de la fonction)"
    if mode=='init':
        #En mode 'init' deux valeurs sont introdiutes dans le plateau
        # Création d'un tableau de 16 case  dont les valeurs sont ceux des indices du tableau tile dans le plateau
        tableau=list(range(16))
        # On prend aléatoirement un premier indice stocké dans un variable x
        x=randint(0,15)
        # On supprime cette valeur dans le tableau pour ne pas le reprendre
        del(tableau[x])
        # On prend aléatoirement un deuxième indice dans le tableau stocké dans un variable i
        i=randint(0,14)
        # On prend aléatoirement un premier indice stocké dans un variable x
        y=tableau[i]
        # Pour accéder aux cases: l'indice de la ligne est la division entière et la colonne reste de la division
        return {'mode':'init', 0:{'val':2,'lig':x//4,'col':x%4}, 1:{'val':1,'lig':y//4,'col':y%4},
              'check': not is_game_over(plateau)}
    else:
        # En mode 'encours' On récupère les indices du tableau tiles ayant la valeur 0 
        tableau=[]
        for i in range(16):
            if plateau['tiles'][i]==0:
                tableau.append(i)
        if len (tableau)!=0:
            # S'il y a au moins une case libre, on choisi de manière aléatoire une de ces valeurs du tableau crée
            indice = randint(0,len(tableau)-1)
            x, val = tableau[indice], randint(1,3)
            return {'mode':'encours', 0:{'val':val,'lig':x//4,'col':x%4},'check': not is_game_over(plateau)}
        # Si ya pas de case vide on passe
        else:
            return {'mode':'encours','check': not is_game_over(plateau)}
        
        
        
            
#########################################
####       Foncton de la partie     #####
####          put_next_tiles        #####
#########################################

def put_next_tiles(plateau,tile):
    """
    Permet de placer une ou deux tuile(s) dans le plateau
    et qui dépend du plateau tiles retourné par la fonction get_next_ale_tile 
    """
    if tile['mode']=='init':
        set_value(plateau,tile[0]["lig"],tile[0]["col"],tile[0]["val"])
        set_value(plateau,tile[1]["lig"],tile[1]["col"],tile[1]["val"])
    elif tile['mode']=='encours' and len(tile)!=2:
        set_value(plateau,tile[0]["lig"],tile[0]["col"],tile[0]["val"])
        
        
        
#########################################
####       Foncton de la partie     #####
####            line_pack           #####
#########################################
        
def line_pack(plateau,num_lig, debut, sens):
    """Tasse les tuiles d'une ligne dans un sens donné
       plateau : dictionnaire contant le plateau du jeu
       num_lig : indice de la ligne à tasser
       debut :  l'indice à partir du quel se fait le tassement  
       sens : sens du tassement 1 vers la guache et O vers la droite"""
    assert check_room(plateau,num_lig,debut) , "Erreur sur l'indice"
    assert sens in [0,1], "le sens est incorrect (O et 1 valeurs possibles)"
    if sens==1:
        for i in range(debut,3,1):
            plateau['tiles'][4*num_lig+i] = plateau['tiles'][4*num_lig+i+1]
        plateau['tiles'][4*num_lig+3] = 0
    else:
        for i in range(debut,-1,-1):
            plateau['tiles'][4*num_lig+i]= plateau['tiles'][4*num_lig+i-1]
        plateau['tiles'][4*num_lig]=0

def colum_pack(plateau, num_col, debut, sens):
    """Tasse les tuiles d'une ligne dans un sens donné
       plateau : dictionnaire contant le plateau du jeu
       num_lig : indice de la ligne à tasser
       debut :  l'indice à partir du quel se fait le tassement  
       sens : sens du tassement 1 vers le haut et O vers le bas"""
    assert check_room(plateau,num_col,debut) , "Erreur sur l'indice"
    assert sens in [0,1], "le sens est incorrect (O et 1 valeurs possibles)"
    if sens==1:
        for i in range(debut,3,1):
            plateau['tiles'][4*i+num_col]= plateau['tiles'][4*(i+1)+num_col]
        plateau['tiles'][12+num_col]=0
    else:
        for i in range(debut,-1,-1):
            plateau['tiles'][4*i+num_col]= plateau['tiles'][4*(i-1)+num_col]
        plateau['tiles'][num_col]=0
    
    
def line_move(plateau, num_lig, sens):
    """Déplace les tuiles d'une ligne donnée dans un sens donné
       en appliquant les règle du jeu Threes
       palateau : dictionnaire contenant le plateau du jeu
       num_lig : indice de la ligne pour laquelle il faut déplacer les tuiles
       sens : sens du tassement 1 vers la guache et O vers la droite
    """
    if sens==1:
        debut=0
        test=False
        while debut<3 and not test:
            x,y = get_value(plateau,num_lig,debut), get_value(plateau,num_lig,debut+1)
            if is_room_empty(plateau,num_lig,debut):
                line_pack(plateau,num_lig, debut, 1)
                test=True
            elif (x==2 and y==1) or (x==1 and y==2):
                line_pack(plateau,num_lig, debut, 1)
                set_value(plateau,num_lig, debut,3)
                test=True
            elif x%3==0 and x==y:
                line_pack(plateau,num_lig, debut, 1)
                set_value(plateau,num_lig,debut,2*x)
                test=True
            debut+=1
    else:
        debut=3
        test=False
        while debut>0 and not test:
            x, y = get_value(plateau,num_lig,debut), get_value(plateau,num_lig,debut-1)
            if is_room_empty(plateau,num_lig,debut):
                line_pack(plateau,num_lig, debut, 0)
                test=True
            elif (x==2 and y==1) or (x==1 and y==2):
                line_pack(plateau,num_lig, debut, 0)
                set_value(plateau,num_lig, debut,3)
                test=True
            elif x%3==0 and x==y:
                line_pack(plateau,num_lig, debut, 0)
                set_value(plateau,num_lig,debut,2*x)
                test=True            
            debut-=1
        
def colum_move(plateau, num_col, sens):
    """Déplace les tuiles d'une colonne donnée dans un sens donné
       en appliquant les règle du jeu Threes
       palateau : dictionnaire contenant le plateau du jeu
       num_col : indice de la ligne pour laquelle il faut déplacer les tuiles
       sens : sens du tassement 1 vers le haut et O vers le bas"""
    if sens==1:
        debut=0
        test=False
        while debut<3 and not test:
            x, y = get_value(plateau,debut,num_col), get_value(plateau,debut+1,num_col)
            if is_room_empty(plateau,debut,num_col)==True:
                colum_pack(plateau, num_col, debut, 1)
                test=True
            elif (x==2 and y==1) or (x==1 and y==2):
                colum_pack(plateau, num_col, debut, 1)
                set_value(plateau,debut,num_col,3)
                test=True
            elif x%3==0 and x==y:
                colum_pack(plateau, num_col, debut, 1)
                set_value(plateau, debut, num_col, 2*x)
                test=True
            debut+=1
        
    elif sens==0:
        debut=3
        test=False
        while debut>0 and not test:
            x, y = get_value(plateau,debut,num_col), get_value(plateau,debut-1,num_col)
            if is_room_empty(plateau,debut,num_col)==True:
                colum_pack(plateau, num_col, debut, 0)
                test=True
            elif (x==2 and y==1) or (x==1 and y==2):
                colum_pack(plateau, num_col, debut, 0)
                set_value(plateau,debut,num_col,3)
                test=True
            elif x%3==0 and x==y:
                colum_pack(plateau, num_col, debut, 0)
                set_value(plateau, debut, num_col, 2*x)
                test=True
            debut-=1

def lines_move(plateau,sens):
    """Déplace les tuiles de toutes les lignes dans un sens donné
       en appliquant les règle du jeu Threes
       palateau : dictionnaire contenant le plateau du jeu
       sens : sens du tassement 1 vers la guache et O vers la droite
    """
    for i in range(4):
        line_move(plateau, i, sens)

def colums_move(plateau,sens):
    """Déplace les tuiles de toutes les collonnes dans un sens donné
       en appliquant les règle du jeu Threes
       palateau : dictionnaire contenant le plateau du jeu
       sens : sens du tassement 1 vers le haut et O vers le bas
    """
    for i in range(4):
        colum_move(plateau, i, sens)
        
def play_move(plateau,sens):
    """
    Permet de jouer le coups du joueur dans le sens voulu
    plateau : plateau contenant les tuiles 
    sens : le sens de tachement des tuiles du plateau 
    """
    if sens=="h":
        colums_move(plateau,1)
    elif sens=="b":
        colums_move(plateau,0)
    elif sens=="g":
        lines_move(plateau,1)
    elif sens=="d":
        lines_move(plateau,0)