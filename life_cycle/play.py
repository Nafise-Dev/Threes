from game.play import *
from ui.play_display import *
from ui.entries import *
from tiles.tile_move import *
import json
from random import randint


def cycle_play(partie):
    """ Permet de jouer à Threes
        param partie : Partie de jeu en cours ou None sinon
        return True si la partie est terminée, False si menu demandé
        
        Séquencement des actions pour cette fonction :
        1 - afficher le plateau de jeu,
        2 - affiche la prochaine tuile pour informer le joueur
        3 - saisir le mouvement proposé par le joueur ; deux cas possible :
            * jouer le coup du joueur courant, mettre à jour le score et revenir au point 1
            * ou retourner False si menu demandé
        4 - si la partie est terminée, retourne True
    """
    # Si la partie est None on commence une nouvelle partie
    if partie == None:
        partie = create_new_play()
    # Séquence 1 : affiche le plateau du jeu
    full_display(partie["plateau"])
    
    tuile = get_next_alea_tiles(partie["plateau"],"encours")
    while tuile["check"]:
        
        # Séquence 2 : affiche la prochaine tuile
        if  len(tuile)==3:
            val_tuile = tuile[0]["val"]
            print("Valeur de la prochaine tuile :", val_tuile)

        # Séquence 3 : saisie le mouvement du joueur
        saisie = get_user_move()
        if saisie == "m" :
            save_game_encours(partie)
            return False
        else:
            play_move(partie["plateau"], saisie)
            tuile = get_next_alea_tiles(partie["plateau"],"encours")
            print(tuile)
            if len(tuile)==3:
                tuile[0]["val"] = val_tuile
                put_next_tiles(partie["plateau"],tuile)
                
            partie["score"] = get_score(partie["plateau"])
            
        # Séquence 1 : affiche le plateau du jeu   
        full_display(partie["plateau"])

        # Séquence 2 : affiche la prochaine tuile
        tuile = get_next_alea_tiles(partie["plateau"],"encours")
        
    print("\n###########################")
    print("#       \033[41;mGAME OVER !\033[m       #")
    print("###########################")
    print("#  Votre score :",str(partie["score"]).rjust(6),"  #")
    print("###########################\n")
    return True


def cycle_play0(partie):
    """Cycle du jeu"""
    # Si la partie est None on commence une nouvelle partie
    if partie is None:
        partie=create_new_play()
    # Tant qu'il y'a possibilité de jouer le jeu continue
    while partie["next_tile"]["check"]:
        
        full_display(partie["plateau"])
        if len(partie["next_tile"])==3:
            print('La ptochaine tuile',partie["next_tile"]["0"]["val"])
            
        choix=get_user_move()
        if choix=="m":
            save_game_encours(partie)
            return False
        else:
            play_move(partie["plateau"],choix)
        
        if len(partie["next_tile"])==3:
            put_next_tiles(partie["plateau"],partie["next_tile"])
            
        partie["score"]=get_score(partie["plateau"])
        
        partie["next_tile"]=get_next_alea_tiles(partie["plateau"],"encours")
        
    
    full_display(partie["plateau"])
    print("\n###########################")
    print("#       \033[41;mGAME OVER !\033[m       #")
    print("###########################")
    print("#  Votre score :",str(partie["score"]).rjust(6),"  #")
    print("###########################\n")
    return True


def cycle_play1(partie):
    """Cycle du jeu"""
    # Si la partie est None on commence une nouvelle partie
    if partie is None:
        partie=create_new_play()
    # Tant qu'il y'a possibilité de jouer le jeu continue
    while partie["next_tile"]["check"]:
        
        full_display(partie["plateau"])
        if len(partie["next_tile"])==3:
            print('La ptochaine tuile',partie["next_tile"]["0"]["val"])
            
        choix=get_user_move()
        if choix=="m":
            save_game_encours(partie)
            return False
        else:
            play_move(partie["plateau"],choix)
        
        partie["next_tile"]=get_next_alea_tiles(partie["plateau"],"encours")
        put_next_tiles(partie["plateau"],partie["next_tile"])
        partie["score"]=get_score(partie["plateau"])
        
    full_display(partie["plateau"])
    print("###################          GAME OVER !!!!!!!!           ###################")
    print("Votre score est",str(partie["score"]))
    return True


def cycle_play2(partie):
    """Cycle du jeu"""
    # Si la partie est None on commence une nouvelle partie
    if partie is None:
        partie=create_new_play()
    # Tant qu'il y'a possibilité de jouer le jeu continue
    while partie["next_tile"]["check"]:
        
        full_display(partie["plateau"])
        nb=randint(1,3)
        print('La ptochaine tuile',nb)
            
        choix=get_user_move()
        if choix=="m":
            save_game_encours(partie)
            return False
        else:
            play_move(partie["plateau"],choix)
            
        partie["next_tile"]=get_next_alea_tiles(partie["plateau"],"encours")
        
        if len(partie["next_tile"])==3:
            partie["next_tile"]["0"]["val"]=nb
            put_next_tiles(partie["plateau"],partie["next_tile"])
            
        partie["score"]=get_score(partie["plateau"])
               
    full_display(partie["plateau"])
    print("###################          GAME OVER !!!!!!!!           ###################")
    print("Votre score est",str(partie["score"]))
    return True




def save_game(partie):
    """
    Sauvegarde une partie en cours dans le fichier save_game.json
    """
    fichier= open("save_game.json","w")
    json.dump(partie,fichier)
    fichier.close()

def restore_game():
    """
    Restaure et retourne une partie sauvegardée dans le fichier "game_save.json",
    ou retourne une nouvelle partie si aucune partie n'est sauvegardée
    """
    with open("save_game.json","r") as fichier:
        try:
            partie=json.load(fichier)
            fichier.close()
            return partie
        except:
            pass
        else:
            return create_new_play()
        
    
def save_game_encours(partie):
    """
    Sauvegarde une partie en cours dans le fichier contgamejson
    """
    fichier= open("contgame.json","w")
    json.dump(partie,fichier)
    fichier.close()
        
def restore_game_encours():
    """
    Restaure et retourne une partie sauvegardée dans le fichier "contgamejson",
    """
    with open("contgame.json","r") as fichier:
        partie=json.load(fichier)
        fichier.close()
        return partie




