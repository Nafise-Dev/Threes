from tiles.tile_move import *
from life_cycle.cycle_game import get_score

def init_play():
    """Retourne un plateau correspondant à une nouvelle partie
    Une nouvelle partie est un dictionnaire avec les clés et les valeurs suivant :
    - 'n': vaut 4
    - 'nb_case_libre' : 16 au départ
    - 'tiles' : tableau de 4*4 case initialisé à 0
    """
    plateau={}
    plateau['n']=4
    plateau['nb_case_libre']=16
    table_init=[]
    i=0
    while i<16:
        table_init.append(0)
        i+=1
    plateau['tiles']=table_init
    return plateau



def create_new_play():
    """Créer et retourne une nouvelle partie 
    """
    new_partie={}
    
    plateau=init_play()
    tile=get_next_alea_tiles(plateau,'init')
    put_next_tiles(plateau,tile)
    
    new_partie["plateau"]=plateau    
    new_partie["next_tile"]=get_next_alea_tiles(plateau,'encours')
    new_partie["score"]=get_score(plateau)
    
    return new_partie

    
    
    
    
    
    
    
    
    
    
    
    