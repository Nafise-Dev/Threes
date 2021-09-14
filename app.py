from life_cycle.play import *
from ui.entries import *

def threes():
    """
    Permet d'enchainer les parties du jeu threes
    """
    #Tout a début on commence avec le menu simple
    # Y'a que 3 choix possibles : nouvelle partie ou charger ou quitter
   
    # Début du boucle pour le menu de démarage ou quand le joueur perd une partie
    # Lose_or_menu_partie signifie le cycle d'une partie soit elle est True(quand le joueur perd) soit False (le menu est demandé)
    
    lose_or_menu_partie=True
    while lose_or_menu_partie:
        menu=get_user_menu(None)
        if menu=="N":
            lose_or_menu_partie=cycle_play(None)
        elif menu=="L":
            partie=restore_game_encours()
            lose_or_menu_partie=cycle_play(partie)
        # Dès que le joueur veut quitter la fonction s'arrete en retournant 0
        elif menu=="Q":
            print(" Fin du jeu, Au revoir!!")
            return 0
        # Si le menu est demandé dans une partie, alors y'a 5 choix: le joueur peux sauvegarder ou continuer le jeu dans ce cas
        #Et tant que le menu est demandé (Lose_or_menu_partie==False) on procéde ainsi
        while not lose_or_menu_partie:
            partie=restore_game_encours()
            menu=get_user_menu(partie)
            if menu=="N":
                lose_or_menu_partie=cycle_play(None)
            elif menu=="L":
                partie=restore_game_encours()
                lose_or_menu_partie=cycle_play(partie)
            elif menu=="S":
                save_game(partie)
            elif menu=="C":
                partie=restore_game_encours()
                lose_or_menu_partie=cycle_play(partie)
            elif menu=="Q":
                print(" Fin du jeu, Au revoir!!")
                return
                
                
threes()
                        
            
            