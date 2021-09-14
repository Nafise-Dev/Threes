def get_user_move():
    """
    Saisi et retoune le coup joué parmi les choix :
    :retourne le choix de l'utilisateur (en minuscule)
    
    - 'h' pour haut
    - 'b' pour bas
    - 'g' pour gauche
    - 'd' pour droite
    - 'm' pour menu principal.
    
    """
    choix=input("Entrez le votre choix : Pour jouer taper 'h' comme haut 'b' comme bas 'g' comme gauche 'd' comme droite :\n\t\t\tPour aller vers le menu taper 'm'").lower()
    while choix not in ["h","b","g","d","m"]:
        choix=input("\033[1;31m\n\tAttention !! Votre choix est invalide.\033[m\n\nEntrez le votre choix :\n\033[1;32m\tPour jouer taper 'h' comme haut 'b' comme bas 'g' comme gauche 'd' comme droite :\n\tPour aller vers le menu taper 'm'\033[m\n>>").lower()
    return choix
    
def get_user_menu(partie):
    """
    Menu du jeu
    Saisi et retourne le choix du joueur dans le menu principal
    La fonction prend en paramétre partie: la partie du jeu jeu en encours ou None sion
    retourne le choix de l'utilisateur en (majuscule)
        - 'N' : Commencer une nouvelle partie,
        - 'L' : Charger une partie,
        - 'S' : Sauvegarder la partie en cours (si le paramètre partie correspond à une partie en cours),
        - 'C' : Reprendre la partie en cours (si le paramètre partie correspond à une partie en cours),
        - 'Q' : Terminer le jeu.
    """
    if partie is None:
        choix=input("\t\t\t\t\t\t\033[1;32mMenu du jeu\033[m\nTaper : - 'N' : Nouvelle partie,\n\t- 'L' : Charger une partie,\n\t- 'Q' : Quitter le jeu. \n").upper()
        while choix not in ["N","L","Q"]:
            choix=input("\t\t\t\t\t\t\033[1;31mAttention !!!!! Votre choix est invalide\033[m\nTaper : - 'N' : Commencer une nouvelle partie,\n\t- 'L' : Charger une partie,\n\t- 'Q' : Quitter le jeu. \n").upper()
        return choix
        
    else :   
        choix=input("\t\t\t\t\t\t\033[1;32mMenu du jeu\033[m\nTaper : - 'N' : Commencer une nouvelle partie,\n\t- 'L' : Charger une partie,\n\t- 'S' : Sauvegarder la partie en cours,\n\t- 'C' : Reprendre la partie,\n\t- 'Q' : Quitter le jeu. \n").upper()
        while choix not in "NLCSQ":
            choix=input("\t\t\t\t\t\t\033[1;31mAttention !!!!! Votre choix est invalide\033[m\nTaper : - 'N' : Nouvelle partie,\n\t- 'L' : Charger une partie,\n\t- 'S' : Sauvegarder la partie,\n\t- 'C' : Reprendre la partie,\n\t- 'Q' : Quitter le jeu.. \n").upper()
        return choix
        