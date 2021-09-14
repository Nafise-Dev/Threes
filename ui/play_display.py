from tiles.tile_acces import *

def full_display(plateau): 
    """Affichage du plateau en couleur """
    cadre1="\033[42m "+" \033[m".rjust(29)
    print(cadre1)
    cadre="\033[42m \033[m"+"\033[40m                         \033[m"+"\033[42m \033[m"
    i=0
    while i<4:
        ligne_inter="\033[42m \033[m"+"\033[40m \033[m"
        ligne="\033[42m \033[m"+"\033[40m \033[m"
        j=0
        while j<4:
            x=get_value(plateau,i,j)
            if x==2:
                nb="\033[1;30;41m"+str(x).rjust(3)+"  \033[m"
                ligne_inter+="\033[41m     \033[m"+"\033[40m \033[m"
            elif x==1:
                nb="\033[1;30;44m"+str(x).rjust(3)+"  \033[m"
                ligne_inter+="\033[44m     \033[m"+"\033[40m \033[m"
            elif x==0:
                nb="\033[44m"+" ".rjust(3)+"  \033[m"
                ligne_inter+="\033[44m     \033[m"+"\033[40m \033[m"
            else:
                nb="\033[1;30;47m"+str(x).rjust(3)+"  \033[m"
                ligne_inter+="\033[47m     \033[m"+"\033[40m \033[m"
            ligne+=nb+"\033[40m \033[m"
            j+=1
        ligne_inter+="\033[42m \033[m"
        ligne+="\033[42m \033[m"
        print(cadre+"\n"+ligne_inter+"\n"+ligne+"\n"+ligne_inter)
        i+=1
    print(cadre+"\n"+cadre1)
    
    
def medium_display(plateau): 
    """Affichage du plateau avec délimitation textetuelle des cases """
    cadreD="┌—————┬—————┬—————┬—————┐"
    ligneI="│     │     │     │     │"
    ligneC="├—————┼—————┼—————┼—————┤"
    ligneI="│     │     │     │     │"
    cadreF="┕—————┴—————┴—————┴—————┘"
    print(cadreD)
    i=0
    while i<4:
        ligne="│"
        j=0
        while j<4:
            if plateau['tiles'][4*i+j]==0:
                ligne += " ".rjust(3) + "  │"
            else :
                ligne += str(plateau['tiles'][4*i+j]).rjust(3) + "  │"
            j+=1
        if i!=0:
            print(ligneC)
            
        print(ligneI)
        print(ligne)
        print(ligneI)
        i+=1
    print(cadreF)
        
    