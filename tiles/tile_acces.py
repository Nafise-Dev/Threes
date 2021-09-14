def check_indice(plateau,indice):
    """Return True si indice correspond à un indice valide de pour le plateau (entre 0 et n-1) """
    return indice>=0 and indice<=plateau['n']-1


def check_room(plateau,lig,col):
    """Return True si (lig,col) est une case du tableau c-à-d lig et col sont des indices valides."""
    return check_indice(plateau,lig) and check_indice(plateau,col)
 
def get_value(plateau,lig,col):
    """Return le valeur de la case (lig,col) passée en paramètre,
    Erreur si la case est invalide"""
    assert check_room(plateau,lig,col), "La case est invalide"
    return plateau['tiles'][4*lig+col]

def set_value(plateau,lig,col,val):
    """Affecte une valeur val à une case (lig, col) passée en paramétre
    Retourne Erreur si la case est invalide ou si la valeur est négative
    Met à jour aussi le nombre de case libre"""
    assert check_room(plateau,lig,col), "La case est invalide"
    assert val>0, "Erreur sur la valeur"
    plateau['tiles'][4*lig+col]=val
    nb=0
    for i in range(16):
        if plateau['tiles'][i]==0:
            nb+=1
    plateau['nb_case_libre']=nb
                
def is_room_empty(plateau,i,j):
    """Teste si une case du plateau est libre ou pas
    retourne True si elle est libre, sinon False"""
    assert check_room(plateau,i,j), "La case est invalide"
    return get_value(plateau,i,j)==0

