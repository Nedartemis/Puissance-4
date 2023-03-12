def main():
    pass

if __name__ == '__main__':
    main()

from Puissance_4_annexe import *

tgrille = 80
dimension = [7, 6]
Liste_couleur = ['red', 'yellow', 'blue']
decoupage_memoire = 300

window = Tk()
canvas = Canvas(window, width=5, height=5, bg='black')
canvas.pack()

def deplacement_pointeur(*parametres):
    global position

    touche = parametres[2]

    if touche == 'd':
        if position == dimension[0]-1:
            deplacement = 1 - dimension[0]
        else:
            deplacement = 1
    else:
        "si touche == q"
        if position == 0:
            deplacement = dimension[0]-1
        else:
            deplacement = -1

    position += deplacement
    canvas.move(pointeur, deplacement * tgrille, 0)

def activer_descente_pion(*parametres):
    global pointeur, Big_data

    if fin != 0:
        fin_partie()

    elif Big_data.count(position) != dimension[1] and pointeur != 0:
        "si ça ne dépasse pas les dimensions verticales"

        canvas.delete(pointeur)
        pointeur = 0

        jouer_pion(Big_data, position)
        Big_data += [position]

        verification_fin()

def jouer_pion(Liste_jeton_place, position):

    roundp = len(Liste_jeton_place)

    canvas.move(Liste_pion[roundp], position * tgrille, 2*tgrille)

    if acceleration == 0:
        for k in range((dimension[1]-Liste_jeton_place.count(position))*10):
            canvas.after(temps_descente, descente_pion(roundp))
    else:

        canvas.move(Liste_pion[roundp], 0, (dimension[1]-Liste_jeton_place.count(position))*tgrille)
        canvas.update()

def descente_pion(roundp):

    canvas.move(Liste_pion[roundp], 0, tgrille / 10)
    canvas.update()

def monter_pion(roundp):

    canvas.move(Liste_pion[roundp], 0, -tgrille / 10)
    canvas.update()


def supprimer_pion(nombre_restant_jetons):

    position = (canvas.coords(Liste_pion[nombre_restant_jetons])[0] - ecart_bord) // tgrille

    if acceleration == 0:
        for k in range((dimension[1] - Big_data[:nombre_restant_jetons].count(position)) * 10):
            canvas.after(temps_descente, monter_pion(nombre_restant_jetons))
    else:
        canvas.move(Liste_pion[nombre_restant_jetons], 0, -(dimension[1] - Big_data[:nombre_restant_jetons].count(position))*tgrille)

    canvas.move(Liste_pion[nombre_restant_jetons], - position*tgrille, -2*tgrille)

acceleration = 0
temps_descente = 3
"s'il n'y a qu'un joueur, mettre la strategie autorisé à l'index 1 : strategie_memoire_ou_logique, strategie_mixte_logique_memoir, strategie_logique"
Strategie_IA = [strategie_logique, strategie_mixte_logique_memoire]
simulation = 'non'

"[3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 5, 5, 4, 4, 2, 6]"

BigBig_data = []
" new 215 "
BigBig_data += [[0, 3, 3, 3, 3, 4, 2, 6, 5, 3, 3, 5, 2, 2, 0, 0, 2, 0, 6, 0, 0, 5, 5, 6, 6, 6, 5, 5, 6, 2, 2, 1, 1, -1], [3, 2, 3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 0, 2, 6, 6, 6, 6, 6, 6, 0, 0, 5, 0, 0, 0, 5, 5, 5, 5, 5, 1, 1, -1], [3, 2, 2, 2, 3, 3, 2, 3, 3, 3, 2, 2, 6, 5, 6, 5, 5, 6, 6, 5, 5, 5, 4, 4, 4, 4, 4, -1], [0, 3, 3, 3, 3, 4, 2, 6, 5, 3, 3, 5, 2, 2, 0, 0, 2, 0, 6, 0, 0, 5, 5, 6, 6, 6, 6, 5, 5, 2, 2, 1, 1, -1], [0, 3, 3, 3, 3, 4, 2, 6, 5, 3, 3, 5, 2, 2, 0, 0, 2, 0, 6, 0, 0, 5, 5, 6, 6, 6, 2, 2, 5, 5, 6, 1, 1, -1], [0, 3, 3, 3, 3, 4, 2, 6, 5, 3, 3, 5, 2, 2, 0, 0, 2, 0, 6, 0, 0, 5, 5, 6, 6, 6, 6, 5, 2, 2, 5, 1, 1, -1], [0, 4, 3, 3, 3, 3, 3, 3, 1, 2, 4, 4, 4, 2, 5, 5, 6, 1, 0, 4, 2, 2, 2, 2, 0, 0, 1, -1], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 4, 5, 5, 2, 6, 5, 5, 5, 5, 0, 1, 1, 1, 2, 2, -2], [3, 3, 3, 3, 3, 3, 2, 4, 0, 1, 1, 0, 4, 4, 6, 4, 4, 4, 5, 5, 2, 6, 1, 1, 2, 2, -2], [3, 3, 2, 4, 3, 3, 1, 0, 1, 3, 3, 6, 2, 2, 4, 2, 2, 0, 1, 1, -2], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 4, 0, 0, 5, 5, 2, 0, 0, 0, 5, 5, 5, 5, 6, 1, 1, 1, 2, 2, -2], [3, 3, 1, 2, 3, 2, 1, 3, 1, 1, 2, 2, 2, 3, 3, 2, 4, 6, 6, 6, 6, 6, 6, 0, 1, 1, 5, 5, 4, 4, -2], [3, 3, 2, 4, 3, 3, 1, 0, 1, 3, 3, 6, 2, 2, 4, 2, 2, 2, 0, 5, 0, 0, 0, 0, 6, 5, 4, 4, 5, 5, -2], [3, 3, 1, 2, 3, 2, 2, 3, 3, 3, 2, 2, 2, 6, 6, 6, 6, 1, 1, 1, 1, 1, 6, 6, 5, 5, 5, 5, 5, 5, 0, 0, -2], [0, 3, 3, 3, 3, 3, 3, 4, 5, 2, 1, 1, 1, 1, 4, 5, 4, 4, 2, 5, 5, 4, 5, 1, 1, 4, 2, 0, 0, 5, 0, 0, 0, 6, 6, 6, 6, 6, 6, 2, 2, -1], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 4, 5, 5, 2, 6, 5, 5, 5, 5, 0, 0, 0, 0, 0, 1, 1, -1], [3, 2, 3, 3, 3, 3, 3, 2, 2, 4, 0, 2, 4, 0, 0, 2, 2, 4, 4, 4, 4, 5, 5, 5, 0, 0, 0, 5, 5, 5, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 5, 4, 4, 0, 0, 4, 4, 0, 0, 0, 6, 6, 6, 6, 6, 6, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 5, 5, -1], [3, 2, 3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 0, 2, 4, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 4, 4, 1, 1, 4, 4, 1, 1, 1, 1], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 4, 5, 5, 2, 5, 5, 5, 5, 0, 6, 6, 6, 0, 0, 0, 0, 6, 6, 1, 1, -1], [3, 2, 2, 2, 2, 2, 2, 3, 3, 5, 3, 3, 1, 3, 4, 4, 5, 6, 0, 6, 6, 5, 5, 5, 6, 6, 5, 6, 0, 0, 0, 0, 0, 1, 1, -1], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 5, 4, 4, 0, 0, 4, 0, 0, 4, 0, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 2, 2, -1], [3, 3, 3, 3, 2, 1, 5, 4, 4, 3, 3, 4, 2, 4, 4, 6, 5, 5, 6, 5, 5, 4, 0, 0, 0, 0, 0, 0, 5, 6, 6, 6, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 1, 1, 2, 2, 2, 1, 2, 6, 6, 6, 6, 6, 6, 1, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 4, 4, -1], [3, 3, 3, 3, 3, 3, 1, 4, 2, 0, 1, 2, 2, 1, 4, 4, 2, 5, 5, 2, 4, 5, 4, 2, 4, 5, 5, 6, 5, 6, 6, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 2, 0, 1, 1, 2, 0, 0, 1, 1, 4, 4, 5, 5, 5, 5, 5, 5, 4, 4, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 1, 1, 2, 4, 1, 4, 5, 4, 4, 6, 2, 6, 6, 6, 2, 2, 2, 1, 4, 6, 6, 0, 0, 0, 0, 0, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 2, 4, 4, 1, 4, 4, 1, 4, 2, 6, 6, 1, 6, 1, 6, 6, 6, 0, 0, 0, 0, 0, 2, 2, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 4, 2, 2, 5, 4, 0, 2, 0, 0, 0, 2, 0, 4, 4, 6, 4, 6, 6, 6, 6, 6, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 2, 3, 3, 2, 3, 2, 2, 1, 0, 2, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 0, 0, 4, 4, 5, 4, 4, 5, -1], [3, 3, 3, 2, 2, 3, 3, 3, 2, 1, 2, 2, 5, 6, 6, 5, 5, 2, 4, 4, 4, -1], [3, 3, 3, 3, 3, 3, 2, 1, 5, 4, 4, 4, 2, 5, 6, 4, 4, 0, 4, 1, 2, 2, 2, 2, 6, 0, 0, 1, 1, 1, 1, 0, 0, 0, 6, 6, 6, 6, 5, 5, -2], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 5, 5, 0, 1, 0, 0, 1, 1, 1, 1, 0, 5, 5, 5, 4, 5, 0, 6, 2, 2, 2, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 2, 1, 4, 4, 2, 5, 5, 2, 4, 5, 4, 4, 2, 5, 5, 5, 6, 6, 6, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, -1], [3, 3, 1, 2, 3, 3, 3, 3, 2, 2, 2, 5, 4, 4, 5, 0, 1, 1, 4, 4, 5, 5, 4, 2, 1, 1, 2, 5, 5, 0, 0, 0, 0, 6, 4, 0, 1, 6, 6, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 2, 1, 4, 2, 1, 4, 4, 2, 2, 4, 6, 4, 6, 6, 6, 6, 6, 1, 1, 0, 0, 0, 0, 0, 5, 5, -2], [3, 3, 3, 3, 3, 3, 4, 2, 5, 6, 5, 2, 5, 5, 2, 2, 2, 2, 5, 5, 6, 6, 6, 4, 4, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 2, 0, 1, 1, 1, 1, 2, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 5, 5, -2], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 4, 5, 5, 2, 0, 5, 5, 5, 5, 6, 1, 1, 1, 2, 2, -2], [3, 3, 3, 3, 3, 0, 3, 4, 4, 5, 4, 4, 4, 4, 0, 0, 0, 0, 0, 6, 1, 1, 1, 1, 1, 1, 2, 2, 2, -1, -2], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 6, 4, 4, 5, 5, 0, 1, 0, 0, 2, 4, 5, 5, 5, 0, 0, 6, 6, 6, 5, 6, 6, 1, 1, 2, 2, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 1, 1, 2, 2, 2, 1, 4, 4, 4, 2, 4, 4, 1, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 0, 0, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 5, 5, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 4, 4, 4, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 3, 2, 4, 0, 1, 3, 3, 4, 4, 4, 4, 1, 4, 6, 6, 6, 6, 5, 5, 2, 1, 5, 6, 5, 5, 5, 1, 2, 2, 2, 2, 0, 6, 0, 0, -2], [3, 3, 3, 3, 1, 3, 4, 2, 2, 3, 4, 5, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 0, 0, 0, 0, 5, 5, 2, 2, 5, 5, 5, 5, 4, 4, 4, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 1, 1, -2], [3, 3, 1, 3, 3, 2, 3, 3, 6, 2, 1, 2, 2, 1, 1, 2, 2, 4, 6, 4, 4, 4, 6, 6, 0, 4, 4, 6, 6, 1, 1, 0, 0, 0, 0, 0, 5, 5, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 0, 0, 2, 0, 0, 2, 5, 5, 5, 5, 5, 5, 4, 4, 4, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 0, 0, 0, 0, 2, 2, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 5, 5, -2], [3, 3, 0, 3, 3, 3, 2, 1, 3, 2, 1, 2, 4, 5, 2, 4, 5, 4, 1, 4, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 4, 1, 1, 4, 4, 1, 1, 0, 0, 0, 2, 2, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 0, 2, 2, 2, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 4, 4, 4, 4, 1, 1, -2], [2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 2, 2, 6, 5, 6, 6, 6, 6, 6, 0, 4, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1, 1, -2], [2, 3, 3, 3, 3, 3, 3, 2, 1, 2, 2, 6, 4, 2, 2, 6, 6, 0, 6, 6, 6, 0, 0, 0, 0, 0, 5, 4, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 1, 2, 4, 2, 2, 1, 4, 2, 1, 4, 0, 2, 0, 0, 0, 1, 0, 5, 6, 6, 6, 6, 6, 6, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 4, 4, 6, 4, 4, 5, 5, 5, 5, 5, 4, 5, 1, 1, 2, 2, -2], [3, 3, 2, 4, 3, 3, 3, 3, 1, 0, 1, 4, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4, 4, 4, 4, 1, 1, -2], [2, 3, 2, 3, 3, 2, 4, 2, 2, 3, 0, 3, 3, 2, 0, 1, 0, 0, 1, 0, 4, 6, 4, 4, 4, 5, 4, 5, 5, 5, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 4, 1, 1, 1, 4, 4, 0, 0, 0, 0, 0, 1, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 2, 2, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 1, 4, 2, 2, 2, 4, 4, 1, 2, 2, 1, 0, 1, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 5, 5, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 2, 2, 4, 4, 4, 4, 0, 0, 0, 0, 5, 5, 5, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 2, 2, 0, 0, 0, 0, 5, 5, 5, 6, 4, 6, -2], [2, 3, 3, 3, 3, 3, 3, 2, 2, 2, 5, 0, 0, 2, 1, 4, 4, 4, 4, 4, 4, 5, 2, 5, 6, 5, 5, 5, 0, 0, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 3, 2, 4, 2, 1, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 1, 1, -1], [3, 3, 3, 3, 3, 3, 2, 4, 0, 1, 4, 4, 6, 4, 4, 0, 1, 5, 5, 4, 0, 0, 5, 5, 5, 5, 6, 0, 0, 1, 1, 2, 1, 1, 2, 2, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 2, 0, 2, 6, 6, 6, 2, 6, 6, 6, 0, 0, 0, 0, 5, 5, 4, 4, 4, 1, 1, 1, 4, 1, 5, 5, -2], [2, 3, 6, 3, 3, 3, 3, 3, 2, 2, 0, 2, 2, 2, 4, 6, 4, 1, 1, 6, 6, 6, 4, 4, 4, 4, 6, 0, 5, 5, 0, 0, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 1, 2, 4, 2, 2, 1, 4, 4, 0, 2, 1, 2, 0, 0, 0, 0, 1, 5, 6, 6, 6, 6, 6, 6, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 1, 1, 2, 2, 4, 2, 1, 2, 2, 1, 4, 4, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 5, 5, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 2, 2, 1, 2, 2, 2, 4, 6, 6, 0, 0, 0, 0, 0, 5, 6, 6, 6, 6, 1, 1, 1, 1, 4, 4, -1], [2, 5, 3, 1, 3, 3, 3, 4, 2, 4, 4, 1, 1, 4, 5, 6, 4, 3, 3, 4, 6, 1, 6, 6, 1, 1, 6, 6, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 2, 2, -2], [3, 3, 4, 2, 5, 6, 5, 3, 3, 3, 5, 5, 2, 3, 2, 0, 0, 2, 0, 0, 2, 2, 5, 5, 6, 6, 6, 4, 4, -1], [3, 3, 2, 1, 5, 4, 3, 4, 3, 2, 1, 5, -2], [3, 3, 1, 2, 3, 3, 2, 3, 3, 2, 4, 1, 0, 2, 2, 1, 0, 1, 1, 0, 0, 0, -2], [2, 3, 2, 2, 2, 2, 2, 3, 3, 3, 0, 3, 3, 4, 5, 4, 4, 5, 5, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 5, 5, 5, 4, 4, 4, 6, 6, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 1, 2, 4, 2, 2, 1, 2, 4, 2, 4, 0, 0, 0, 0, 0, 5, 6, 6, 6, 6, 6, 6, 1, 1, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 4, 2, 1, 1, 2, -1], [0, 3, 3, 3, 3, 3, 3, 4, 5, 1, 2, 2, 2, 1, 1, 2, 1, 1, 4, 2, 5, 4, 4, 4, -2], [1, 3, 3, 3, 3, 3, 3, 2, 5, 2, 2, 2, 0, 1, 1, 1, 1, 2, 2, 1, 5, 6, 6, 5, 6, 6, 5, 5, 5, 6, 6, 0, 0, 0, 0, 0, 4, 4, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 4, 4, 2, 0, 4, 4, 2, 2, 0, 0, 0, 0, 5, 5, 5, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 0, 0, 2, 1, 1, 2, 2, 6, 6, 5, 5, 5, 1, 1, 4, 4, 4, 5, 5, 4, 5, 0, 0, 0, 6, 6, -2], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 2, 2, 1, 2, 4, 2, 2, 6, 0, 0, 0, 1, 1, 6, 6, 6, 6, 6, 0, 0, 1, 1, 4, 4, 4, 4, 5, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 2, 2, 1, 2, 2, 2, 4, 6, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 4, 4, 4, 4, 5, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 4, 2, 2, 0, 2, 2, 6, 6, 6, 2, 6, 6, 6, 5, 5, 4, 4, 4, 4, 0, 0, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 2, 2, 3, 1, 2, 2, 5, 2, 0, 1, 1, 4, 4, 4, 4, 4, 5, 5, 2, 4, 0, 0, 0, 0, 0, 5, 5, 5, 6, 6, 6, 6, 6, 6, 1, 1, -1], [3, 3, 3, 3, 3, 3, 2, 4, 1, 0, 1, 2, 2, 4, 4, 1, 4, 2, 4, 4, 1, 2, 2, 1, 0, 0, 0, 0, 0, 1, 6, 6, 6, 6, 6, 6, 5, 5, -2], [3, 3, 4, 5, 1, 2, 3, 3, 2, 3, 2, 3, 2, 2, 4, 2, 4, 4, 4, 4, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 5, 5, -1], [3, 3, 2, 1, 5, 4, 3, 3, 4, 3, 4, 3, 4, 4, 2, 4, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 1, 1, -1], [3, 2, 2, 3, 3, 2, 4, 3, 5, 6, 2, 4, 5, 4, 4, 1, 4, 1, 0, 1, 1, 2, 2, 3, 3, 0, 4, 0, 0, 0, 1, 1, -2], [3, 2, 2, 3, 3, 2, 3, 2, 2, 3, 3, 4, 1, 4, 2, 1, 6, 6, 4, 4, 6, 6, 4, 6, 4, 6, 0, 1, 0, 1, -2], [3, 3, 3, 3, 3, 3, 2, 1, 5, 4, 4, 4, 5, 5, 4, 5, 5, 2, 4, 1, 4, 1, 1, 1, 5, 1, 6, 6, 2, 2, 2, -1], [3, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 2, 6, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 2, 3, 6, 2, 1, 2, 2, 2, 2, 6, 6, 4, 6, 6, 6, 0, 5, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 1, 5, 3, 1, 6, 5, 2, 5, 5, 6, 6, 6, 6, 1, 1, 0, 6, 0, 0, 0, 2, 0, 1, 1, 0, 5, 5, 4, 4, 4, 2, 2, -1], [3, 3, 3, 3, 3, 3, 2, 1, 5, 4, 4, 4, 4, 6, 5, 5, 4, 2, 1, 4, 0, 6, 6, 5, 5, 5, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 2, -1], [3, 3, 3, 2, 2, 3, 2, 1, 2, 2, 3, 3, 5, 6, 6, 5, 5, 2, 5, 5, 5, 6, 6, 6, 4, 4, 4, -1], [3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 0, 2, 2, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, -2], [3, 3, 3, 2, 2, 3, 2, 2, 3, 3, 2, 1, 6, 5, 6, 6, 6, 2, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 5, 5, -1], [3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 2, 2, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, -2], [3, 3, 3, 2, 3, 3, 2, 3, 2, 2, 0, 0, 0, 0, 1, 1, 1, -1], [3, 1, 3, 3, 4, 3, 5, 2, 6, -1], [3, 3, 3, 2, 2, 2, 4, 6, 1, 3, 2, 0, 1, 1, 4, 5, 3, 3, 2, 2, 0, 5, 4, 4, 5, 4, 5, 4, 0, 0, 0, 0, 1, 1, 1, 5, 5, 6, 6, -1], [3, 1, 5, 3, 4, 2, 6, -1], [3, 3, 3, 2, 3, 2, 3, 3, 2, 2, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 2, 2, 0, 0, 4, 4, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 2, 3, 2, 3, 3, 2, 6, 2, 2, 5, 5, 6, 5, 5, 5, 5, 6, 6, 6, 2, 6, 0, 0, 0, 0, 0, 0, 1, 1, -2], [3, 3, 3, 2, 2, 3, 1, 3, 2, 3, 2, 2, 5, 6, 5, 5, 6, 2, 5, 5, 5, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, -1], [3, 3, 3, 2, 3, 2, 3, 3, 2, 6, 2, 2, 5, 5, 6, 5, 5, 5, 5, 6, 6, 2, 0, 0, 0, 0, 6, 6, 0, 0, 1, 1, -2], [3, 3, 3, 2, 2, 2, 3, 3, 2, 3, 5, 1, 2, 6, 5, 2, 4, 4, 4, -1], [3, 3, 3, 2, 3, 3, 3, 2, 2, 2, 2, 2, 6, 4, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 4, 4, -1], [3, 0, 3, 3, 3, 4, 3, 3, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, -1], [3, 2, 3, 3, 3, 2, 2, 4, 3, 3, 0, 2, 4, 2, 2, 4, 4, 4, 5, 4, 0, 0, 0, 0, 0, 6, 6, 5, 5, -1], [3, 2, 0, 0, 6, 3, 3, 3, 2, 5, 3, 3, 2, 1, 0, 0, 2, 2, 6, 6, 2, 6, 6, 6, 4, 4, 4, 4, 4, 4, 0, 0, 5, 5, 5, 5, 5, 1, 1, -1], [3, 2, 6, 3, 3, 3, 3, 3, 5, 4, 4, 4, 2, 4, 4, 5, 4, 0, 6, 0, 0, 0, 0, 0, 6, 6, 6, 6, 1, 1, 2, 1, 2, -1], [3, 2, 2, 2, 3, 3, 3, 3, 2, 3, 6, 2, 5, 4, 5, 4, 4, -1], [3, 3, 3, 3, 2, 4, 4, 3, 3, 4, 1, 0, 1, 4, 4, 6, 1, 1, 6, 2, 2, 2, -2], [3, 2, 2, 2, 3, 2, 3, 3, 3, 2, 2, 6, 3, 0, 0, 6, 6, 6, 6, 6, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 4, 1, 1, -1], [3, 2, 3, 3, 3, 5, 3, 3, 0, 2, 2, 2, 2, 5, 5, 2, 5, 5, 5, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 1, 1, 1, 1, 1, -1], [3, 2, 3, 3, 3, 6, 3, 3, 0, 0, 6, 6, 6, 0, 0, 2, 2, 2, 2, 0, 4, 4, 5, 0, 4, 5, 6, 4, 1, 1, 4, 6, 4, 2, 1, 1, 1, -1], [3, 3, 3, 3, 2, 1, 5, 4, 4, 3, 4, 1, 2, 1, 1, 0, 2, 2, 0, 4, 3, 2, 2, 4, 1, 4, -2], [3, 2, 3, 3, 3, 5, 5, 2, 2, 3, 2, 2, 6, 3, 0, 6, 2, 5, 5, 5, 4, 5, 4, 4, 4, -1], [2, 3, 3, 3, 3, 3, 3, 6, 6, 5, 4, 4, 4, 2, 1, 0, 1, 1, 1, 2, 2, 4, 2, 5, 2, 6, 6, 6, 6, 4, 4, 0, 0, -1], [3, 3, 2, 4, 3, 4, 3, 2, 3, 3, 2, 4, 4, 0, 2, 0, 0, 0, 2, 2, 4, 4, 0, 0, 6, 6, 6, 6, 6, 6, 1, 1, -2], [3, 2, 3, 3, 4, 3, 3, 3, 4, 6, 2, 4, 2, 4, 2, 2, 2, 4, 4, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, 1, -1], [3, 2, 2, 2, 2, 6, 5, 5, 2, 5, 2, 5, 5, 5, 6, 6, 6, 6, 6, 3, 3, 3, 3, 3, 0, 0, 0, 1, 1, 1, 4, 4, 4, 4, 4, -1], [3, 2, 2, 2, 2, 6, 5, 5, 2, 5, 2, 5, 5, 3, 3, 3, 3, 5, 6, 3, 4, 4, 4, 4, 4, -1], [3, 2, 2, 2, 2, 3, 3, 3, 5, 6, 0, 3, 5, 3, 5, 5, 5, 5, 2, 2, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 6, 6, 6, 4, 4, 4, -1], [3, 3, 3, 2, 3, 3, 3, 2, 2, 6, 2, 2, 0, 0, 0, 0, 2, 0, 0, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 1, 1, -2], [3, 2, 2, 3, 3, 3, 2, 2, 1, 4, 3, 3, 2, 2, 0, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 5, 5, 5, 4, 4, -1], [3, 2, 2, 4, 3, 3, 3, 4, 4, 3, 4, 4, 6, 3, 4, 0, 0, 0, 0, 0, 1, 1, 1, -1], [3, 3, 2, 4, 3, 4, 3, 2, 3, 3, 2, 4, 4, 4, 2, 2, 2, 0, 0, 0, 0, 0, 4, 6, 6, 6, 0, 6, 6, 6, 1, 1, -2], [3, 3, 3, 2, 2, 3, 3, 6, 1, 2, 2, 3, 5, 5, 5, 6, 6, 6, 5, 5, 6, 5, 0, 0, 0, 6, 0, 0, 0, 2, 2, 1, 1, -1], [3, 2, 3, 3, 4, 3, 3, 3, 6, 5, 4, 5, 5, 6, 2, 2, 2, 4, 2, 2, 0, 0, 6, 6, 6, 0, 6, 0, 0, 0, 5, 5, 5, 4, 4, 4, 1, 1, 1, 1, 1, -1], [3, 3, 3, 2, 3, 3, 3, 2, 2, 6, 2, 2, 2, 6, 6, 6, 0, 0, 0, 0, 6, 6, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, -2], [3, 3, 2, 4, 3, 3, 3, 4, 3, 2, 2, 4, 4, 2, 2, 4, 2, 0, 4, 6, 6, 6, 0, 0, 0, 0, 0, 6, 6, 6, 1, 1, -2], [3, 3, 3, 2, 2, 3, 5, 6, 2, 2, 1, 3, 2, 3, 2, 5, 5, 5, 5, 4, 6, 6, 6, 4, 4, -1], [3, 3, 3, 3, 2, 4, 1, 0, 2, 3, 2, 2, 3, 2, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 0, 5, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 2, 2, 3, 2, 3, 1, 3, 2, 2, 5, 6, 0, 5, 5, 5, 6, 5, 4, 4, 4, -1], [3, 3, 3, 3, 2, 4, 0, 1, 2, 3, 2, 2, 3, 0, 0, 2, 0, 2, 0, 0, 6, 5, 6, 5, 5, 5, 5, 5, 6, 6, 6, 6, 1, 1, -2], [3, 3, 3, 2, 2, 3, 2, 5, 1, 3, 3, 2, 2, 2, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 1, 1, -1], [3, 3, 3, 3, 2, 4, 4, 4, 1, 0, 0, 4, 4, 3, 3, 5, 6, 6, 1, 4, 1, 1, 1, 2, 2, 2, -2], [3, 3, 3, 3, 2, 4, 1, 0, 2, 3, 2, 2, 3, 2, 4, 0, 0, 0, 0, 2, 6, 6, 6, 6, 6, 6, 0, 5, 4, 4, 4, 4, 5, 5, -2], [3, 3, 2, 4, 3, 3, 3, 3, 1, 0, 1, 4, 4, 0, 4, 2, 2, 1, 4, 4, 0, 0, 2, 2, 2, 1, 1, 1, 6, 6, 6, 6, 6, 6, 0, 0, 5, 5, -2], [3, 3, 2, 4, 3, 3, 4, 3, 1, 0, 1, 3, 1, 1, 1, 4, 4, 2, 2, 2, 2, 6, 2, 4, 4, 1, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, -2], [3, 3, 3, 2, 2, 2, 1, 3, 2, 5, 3, 3, 0, 5, 2, 0, 5, 2, 4, 4, 5, 5, 5, 1, 1, 1, 1, 1, 0, 0, 0, -1], [3, 3, 3, 2, 2, 3, 1, 2, 0, 3, 2, 3, 4, 5, 4, 5, 4, 4, 5, 4, 1, 5, 2, 1, 4, 6, 1, 1, 2, 0, 1, 0, 0, 0, 0, 5, 5, 6, 6, -1], [3, 3, 3, 3, 2, 4, 3, 4, 3, 2, 2, 4, 4, 4, 4, 0, 2, 2, 2, 0, 0, 0, 6, 6, 6, 6, 6, 6, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 2, 4, 3, 5, 6, 5, 4, 5, 5, 4, 4, 4, 4, 0, 0, 0, 0, 0, 5, 0, 5, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 2, 6, 6, -1], [3, 3, 3, 2, 2, 2, 1, 3, 0, 3, 4, 5, 2, 3, 4, 5, 5, 2, 4, 4, 4, 5, 6, 2, 6, 6, 6, -1], [3, 3, 3, 2, 2, 3, 2, 2, 1, 6, 3, 3, 2, 2, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 4, 4, 5, 1, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 5, 5, 4, 4, 2, 6, -2], [3, 3, 3, 3, 2, 4, 0, 1, 2, 3, 2, 2, 3, 0, 2, 0, 0, 2, 6, 6, 4, 6, 6, 6, 6, 5, 0, 0, 4, 4, 4, 4, 1, 1, -2], [3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 5, 5, 2, 1, 1, 2, 4, 4, 6, 4, 4, 2, 2, 2, -2], [3, 3, 3, 3, 3, 2, 4, 3, 5, 6, 5, 5, 5, 2, 5, 4, 2, 4, 6, 4, 4, 4, 5, 6, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1, 1, 1, 1, 1, 6, 6, -1], [3, 3, 3, 3, 3, 2, 3, 2, 2, 6, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, -2], [3, 3, 3, 3, 3, 2, 4, 3, 5, 6, 5, 2, 2, 5, 4, 2, 4, 4, 5, 2, 5, 2, 4, 4, 5, 6, 6, 0, 0, 0, 0, 1, 0, 0, 6, 6, 6, 1, 1, -1], [3, 3, 3, 2, 6, 2, 2, 5, 3, 5, 3, 3, 5, 2, 6, 6, 5, 6, 5, 5, 6, 6, 0, 0, 0, 0, 2, 2, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 2, 4, 3, 5, 6, 5, 4, 5, 5, 4, 4, 4, 5, 2, 2, 2, 4, 2, 5, 2, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 6, 6, -1], [3, 3, 3, 3, 3, 2, 3, 2, 2, 6, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 4, 4, -2], [3, 3, 3, 2, 3, 2, 3, 3, 6, 4, 2, 4, 4, 6, 6, 6, 0, 0, 0, 0, 2, 2, 4, 4, 2, 4, 0, 0, 6, 6, 1, 1, -2], [3, 3, 3, 2, 6, 2, 3, 4, 3, 3, 2, 4, 4, 6, 6, 6, 2, 2, 4, 4, 2, 4, 0, 0, 0, 0, 0, 0, 6, 6, 5, 5, -2], [3, 3, 2, 4, 3, 3, 1, 0, 2, 2, 1, 3, 2, 2, 4, 5, 3, 5, 4, 4, 5, 4, 6, 1, 1, 1, -2], [3, 3, 3, 3, 3, 2, 3, 6, 2, 2, 1, 0, 1, 1, 1, 2, 2, 1, 2, 1, 4, 6, 6, 6, 6, 6, 0, 0, 0, 0, 4, 0, 5, 5, 4, 4, 5, -1], [3, 3, 3, 2, 2, 3, 2, 2, 1, 2, 2, 3, 6, 3, 4, 5, 4, 6, 6, 6, 6, 6, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 1, 1, -2], [3, 3, 2, 1, 5, 4, 3, 3, 4, 4, 4, 6, 5, 5, 4, 4, 3, 3, 6, 2, 1, 6, 0, 1, 1, 1, 1, 0, 0, 0, 0, 5, 5, 5, 0, 2, 2, -1], [3, 3, 3, 2, 2, 3, 2, 2, 1, 2, 0, 2, 4, 6, 3, 3, 4, 6, 6, 6, 4, 4, 5, 6, 6, 4, 4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 2, 2, 2, 1, 3, 0, 2, 4, 2, 2, 6, 3, 3, 4, 1, 6, 6, 6, 6, 6, 1, 1, 0, 0, 0, 5, 0, 0, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 2, 2, 3, 1, 2, 2, 4, 4, 5, 2, 1, 0, 0, 6, 2, 0, 0, 0, 0, 6, 6, 6, 6, 6, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 2, 3, 2, 2, 6, 2, 2, 6, 6, 2, 6, 6, 6, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, -2], [3, 3, 2, 1, 5, 4, 4, 4, 4, 1, 1, 1, 3, 3, 4, 6, 5, 5, 4, 3, 3, 5, 5, 2, 2, 2, 5, 6, 6, 1, 1, 0, 0, 0, 0, 0, 2, 2, 0, 6, 6, 6, -3], [3, 2, 2, 2, 2, 6, 3, 3, 2, 2, 3, 3, 3, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, -3], [3, 3, 2, 1, 5, 4, 4, 4, 4, 1, 1, 1, 3, 3, 4, 6, 5, 5, 4, 3, 3, 5, 5, 2, 2, 2, 5, 6, 6, 1, 1, 6, 6, 6, 2, 2, 0, 0, -2], [3, 2, 3, 3, 3, 5, 3, 3, 2, 5, 5, 5, 2, 2, 0, 0, 2, 2, 5, 5, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, -1], [3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 1, 3, 2, 2, 6, 6, 6, 6, 6, 6, 5, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, -3], [3, 3, 3, 2, 2, 0, 1, 3, 2, 2, 6, 3, 2, 3, 2, 5, 4, 6, 6, 0, 0, 0, 0, 6, 6, 6, 0, 5, 4, 5, 5, 5, 5, 1, 1, -1], [3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 2, 3, 4, 5, 4, 4, 4, 1, 0, 4, 2, 0, 0, 2, 0, 1, 1, 1, 1, 0, 0, 6, 6, 6, 6, 6, 6, 5, 5, -1], [3, 3, 3, 3, 3, 2, 3, 2, 2, 6, 2, 6, 2, 2, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 0, 0, -2], [3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 1, 3, 2, 2, 6, 6, 4, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, -1], [3, 3, 3, 3, 3, 2, 4, 2, 6, 5, 5, 4, 2, 4, 4, 5, 5, 5, 3, 4, 4, 5, 2, 2, 2, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 1, 1, -2], [3, 3, 3, 3, 3, 2, 2, 5, 2, 3, 1, 2, 6, 2, 2, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 0, 0, 0, 0, 4, 0, 0, 4, 1, 1, -1], [3, 3, 3, 2, 2, 3, 2, 3, 1, 5, 3, 2, 2, 2, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 0, 4, 5, 5, 5, 5, 5, 4, 4, -1], [3, 3, 3, 2, 2, 2, 1, 3, 0, 3, 2, 3, 4, 5, 4, 2, 5, 5, 2, 5, 4, 4, 4, 5, 5, 4, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 1, 1, -1], [3, 3, 3, 3, 3, 2, 2, 6, 1, 2, 2, 3, 5, 5, 5, 6, 6, 6, 5, 5, 6, 5, 0, 6, 0, 2, 2, 0, 0, 0, 0, 1, 1, -1], [3, 1, 3, 5, 1, 1, 1, 3, 3, 3, 3, 5, 5, 5, 1, 1, 5, 5, 0, 0, 0, 0, 0, 6, 2, 6, 6, 6, 4, 4, 4, 4, 2, 2, 2, 2, 0, 2, 4, 4, 6, 6, -3], [3, 1, 5, 3, 6, 4, 4, 4, 4, 1, 3, 3, 3, 3, 4, 6, 1, 4, 1, 1, 1, 5, 5, 5, 2, 2, 5, 5, 2, 2, 2, -1], [3, 1, 5, 3, 6, 4, 4, 4, 4, 1, 3, 3, 3, 3, 4, 6, 1, 4, 1, 1, 1, 0, 0, 2, 0, 0, 5, 0, 0, 6, 6, 5, 5, 5, 5, 6, 6, 2, 2, -1], [3, 3, 3, 3, 3, 0, 4, 5, 3, 0, 0, 5, 5, 5, 4, 4, 2, 6, -2], [3, 3, 3, 3, 3, 0, 4, 5, 3, 0, 0, 5, 5, 5, 4, 4, 2, 1, 6, 4, 4, 6, 1, 1, 1, 1, 1, 0, 4, 0, 0, 5, 5, 2, 2, 2, -2], [3, 3, 3, 3, 3, 2, 2, 3, 2, 2, 1, 6, 2, 2, 6, 6, 6, 0, 6, 6, 4, 0, 0, 0, 0, 0, 5, 5, 5, 4, 4, -1], [3, 3, 3, 3, 3, 2, 2, 2, 1, 3, 2, 5, 4, 5, 4, 5, 5, 2, 4, 4, 4, 4, 5, 2, 5, 0, 1, 1, 6, 6, 6, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, -1], [3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 5, 5, 4, 4, 2, 1, 6, 1, 4, 6, 1, 0, 2, 2, -2], [3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 5, 5, 2, 1, 1, 6, 6, 2, 4, 4, -2], [3, 3, 3, 3, 3, 0, 4, 5, 3, 5, 4, 4, 6, 5, 5, 1, 1, 1, 1, 1, 1, 5, 5, 2, 2, 2, 0, 0, 0, 4, 4, 4, 0, 0, 6, 6, 6, 6, 6, 2, 2, 2, -3], [3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 1, 3, 2, 2, 0, 6, 6, 6, 6, 6, 6, 5, 4, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 0, 4, 5, 5, 3, 5, 5, 2, 1, 1, 1, 1, 1, 1, 5, 5, 0, 0, 0, 4, 4, 4, 4, 2, 2, 2, 0, 0, 4, 2, 2, 6, 6, 6, 6, 6, 6, -3], [3, 3, 3, 2, 2, 0, 1, 3, 2, 2, 3, 3, 2, 6, 6, 2, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 4, 4, -1], [3, 3, 3, 3, 3, 2, 2, 1, 2, 6, 3, 2, 2, 6, 6, 2, 6, 6, 6, 0, 0, 0, 0, 0, 0, 4, 5, 5, 4, 4, -2], [3, 3, 3, 3, 3, 2, 2, 5, 2, 3, 2, 2, 1, 5, 5, 2, 5, 5, 5, 4, 0, 0, 0, 0, 0, 0, 1, 1, 1, 6, 6, 6, 6, 4, 4, -1], [3, 2, 2, 3, 0, 3, 3, 3, 2, 3, 2, 2, 6, 4, 6, 6, 6, 2, 6, 6, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 1, 1, 1, -1], [3, 3, 3, 3, 3, 2, 2, 2, 4, 1, 5, 6, 5, 2, 3, 1, 0, 2, 2, 6, 5, 5, 1, 4, 4, 4, -2], [3, 3, 3, 3, 3, 2, 2, 2, 1, 4, 2, 1, 0, 3, 4, 5, 6, 2, 5, 5, 5, 0, 2, 0, 0, 1, 1, 1, 1, 5, 5, 6, 6, 6, 6, 0, 0, 6, 4, 4, 4, 4, -3], [3, 1, 3, 5, 3, 3, 5, 3, 5, 3, 5, 5, 1, 1, 1, 5, 2, 2, 2, 4, 6, 2, 4, 4, 6, -1], [3, 3, 3, 3, 2, 4, 1, 0, 2, 2, 1, 2, 2, 3, 3, 0, 1, 1, -2], [3, 3, 3, 3, 3, 2, 2, 6, 1, 2, 2, 3, 4, 0, 1, 1, 4, 5, 5, 5, 5, 2, 2, 5, 5, 6, 6, 6, 6, 6, 1, 1, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, -3], [3, 3, 3, 3, 2, 4, 3, 4, 3, 2, 2, 4, 4, 0, 0, 0, 2, 2, 2, 4, 4, 6, 6, 6, 0, 0, 0, 6, 6, 6, 1, 1, -2], [3, 3, 3, 3, 2, 4, 0, 1, 2, 3, 2, 2, 3, 0, 0, 0, 2, 6, 6, 6, 6, 6, 2, 0, 0, 6, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, -2], [3, 3, 3, 3, 3, 2, 2, 2, 1, 3, 2, 4, 4, 5, 2, 1, 0, 0, 6, 2, 0, 0, 0, 0, 6, 6, 6, 6, 6, 1, 1, 1, 1, 5, 5, -1], [3, 3, 3, 3, 3, 2, 2, 3, 1, 2, 2, 6, 5, 5, 5, 6, 6, 6, 5, 5, 6, 5, 0, 0, 0, 6, 0, 0, 0, 2, 2, 4, 4, -1], [3, 3, 3, 3, 3, 2, 2, 6, 1, 2, 4, 3, 2, 4, 6, 6, 2, 0, 1, 1, 2, 0, 6, 0, 0, 0, 1, 1, 1, 6, 6, 0, 5, 5, 4, 4, 4, 5, 5, 5, 5, 4, -3], [3, 3, 3, 3, 3, 3, 2, 1, 5, 4, 4, 4, 2, 4, 4, 5, 6, 0, 4, 1, 2, 2, 2, 2, 6, 0, 0, 1, 1, 1, 1, 0, 0, 0, 6, 6, 6, 6, 5, 5, -2], [3, 3, 3, 3, 3, 1, 5, 6, 3, 5, 6, 4, 5, 5, 1, 1, 1, 1, 1, 2, 2, 5, 5, 2, 2, 4, 4, 4, 6, -1], [3, 3, 3, 3, 3, 2, 2, 4, 2, 2, 1, 3, 2, 0, 4, 2, 6, 5, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 4, 4, -1], [3, 2, 2, 4, 3, 3, 3, 4, 4, 3, 4, 4, 6, 3, 4, 2, 2, 2, 2, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, -3]]

nombre_joueur = 1

#for partie in BigBig_data:
    #if BigBig_data.count(partie) > 1:
        #print(MERDE)

first = 1
event = 0

partie_deja_vu = 0

def initialisation_variable_partie():
    global position, fin, pointeur, Liste_index_pions_gagnants, Big_data, Big_data_selective, Big_data_repechage

    position = 0
    fin = 0
    pointeur = 0
    Liste_index_pions_gagnants = []

    "changer couleur pions en fonction de first ; si first = 0 : le rouge commence ..."
    for index_pion in range(len(Liste_pion)):
        canvas.itemconfigure(Liste_pion[index_pion], fill=Liste_couleur[(index_pion + first) % 2], outline=Liste_couleur[(index_pion + first) % 2])

    Big_data = []
    Big_data_selective = BigBig_data + BigBig_data_symetrie
    Big_data_repechage = []

    if simulation != 'non':
        Big_data = fonction_simulation(simulation)

def fin_partie(*parametres):
    global Big_data, BigBig_data, BigBig_data_symetrie, partie_deja_vu, first, fin

    roundp = len(Big_data)

    if len(parametres) == 0:

        if fin == 2:
            fin = 3
        else:
            fin += (1 - roundp % 2)

        Big_data += [-fin]

        if Big_data in BigBig_data:
            partie_deja_vu += 1
            print('partie_deja_vu', partie_deja_vu)

        elif (Strategie_IA[1] == strategie_mixte_logique_memoire or Strategie_IA[1] == strategie_logique) and (first%2 == fin - 1 or fin == 3) or strategie_mixte_logique_memoire in Strategie_IA and strategie_logique in Strategie_IA:

            print('parfait', len(BigBig_data))

            "rajouter partie dans la mémoire"

            BigBig_data += [Big_data]
            BigBig_data_symetrie += [retourner_liste(Big_data[:-1]) + [Big_data[-1]]]

            if len(BigBig_data) % decoupage_memoire == 0:
                recopier_memoire()

    if acceleration == 0:
        "descente stylée de tout les pions"

        vitesse = 10

        for k in range(dimension[1] * vitesse):

            for index_pion in range(roundp):
                canvas.move(Liste_pion[index_pion], 0, tgrille / vitesse)

            canvas.update()
            sleep(temps_descente / 2000)

    "remise en place de tout les points"
    for index_pion in range(roundp):
        deplacement_x = -(canvas.coords(Liste_pion[index_pion])[0] - ecart_bord) // tgrille + 1
        deplacement_y = -(canvas.coords(Liste_pion[index_pion])[1] - ecart_bord) // tgrille - 2

        canvas.move(Liste_pion[index_pion], deplacement_x * tgrille, deplacement_y * tgrille)

    canvas.delete(pointeur)
    # sleep(1)

    first = (first + 1) % 2

    initialisation_variable_partie()
    puissance_4()

def puissance_4():
    global pointeur, Big_data, position

    "evente=0, tout les variables sont redéfinies; evente=1, annonce la pause et depause donc pas à redéfinir mais doit redémarer"

    roundp = len(Big_data)

    #print(Big_data)
    #canvas.update()
    #sleep(1)

    if (nombre_joueur == 2 or roundp%2 == first) and nombre_joueur != 0:

        "création pointeur"
        taille_pionteur = tgrille * 0.5

        coord = position * tgrille + (tgrille - taille_pionteur) / 2 + ecart_bord, (tgrille - taille_pionteur) / 2 + ecart_bord, position * tgrille + (tgrille + taille_pionteur) / 2 + ecart_bord, (tgrille + taille_pionteur) / 2 + ecart_bord
        pointeur = canvas.create_oval(coord, fill=Liste_couleur[(roundp+first) % 2])

    else:

        position = tour_ordi(Big_data, Big_data_selective, Strategie_IA, first)
        jouer_pion(Big_data, position)
        Big_data += [position]

        verification_fin()

def verification_fin():
    global fin, Liste_index_pions_gagnants

    "vérification si gagné ou non"
    fin, k, direction = verification_puissance_4(Big_data.copy(), 1 - len(Big_data) % 2, 'retrouver pions gagnants')

    if fin == 1:

        "trouver puis changer de couleur les 4 jetons gagnants"

        if direction == 0:
            "horizontale"
            position_depart = [k % dimension[0], k // dimension[0]]
            deplacement = [-1, 0]
        elif direction == 1:
            "verticale"
            position_depart = [k // dimension[1], k % dimension[1]]
            deplacement = [0, -1]
        elif direction == 2:
            "d1"
            position_depart = [k % dimension[0], k % dimension[0] - 3 + k // dimension[0]]
            deplacement = [-1, -1]
        else:
            "d2"
            position_depart = [dimension[0] - 1 - k % dimension[0], k % dimension[0] - 3 + k // dimension[0]]
            deplacement = [1, -1]

        "déterminer les position des 4 pions gagnants"
        Liste_positions_pions = []
        for index in range(4):
            Liste_positions_pions += [(position_depart[0] + deplacement[0]*index, position_depart[1] + deplacement[1]*index)]

        Liste_index_pions_gagnants = []

        index = 0
        "déterminer leur index dans Big_data"
        while index < len(Big_data) and len(Liste_index_pions_gagnants) < 4:

            x = Big_data[index]
            y = Big_data[:index].count(Big_data[index])

            if (x, y) in Liste_positions_pions:
                Liste_index_pions_gagnants += [index]

            index += 1

        "les changer de couleur"
        for index in range(4):
            canvas.itemconfigure(Liste_pion[Liste_index_pions_gagnants[index]], outline='green')

    elif len(Big_data) == dimension[0] * dimension[1]:

        "Egalité"
        fin = 2

    else:

        trier_memoire(Big_data, Big_data_selective, Big_data_repechage)
        puissance_4()


def recopier_memoire(*parametres):

    k = depart_decoupage//decoupage_memoire
    print('"', 'new', len(BigBig_data), '"')
    while (k + 1) * decoupage_memoire < len(BigBig_data):
        print('BigBig_data +=', BigBig_data[k * decoupage_memoire:(k + 1) * decoupage_memoire])
        k += 1
    print('BigBig_data +=', BigBig_data[k * decoupage_memoire:])

def fonction_simulation(Liste_partie):

    for roundp in range(len(Liste_partie)):

        jouer_pion(Liste_partie[:roundp], Liste_partie[roundp])

    return Liste_partie

def variation_vitesse_descente(commande, k, n_commande, *parametres):
    global temps_descente

    if commande[k * n_commande + 12] == plus:
        temps_descente -= temps_descente // 3
    else:
        temps_descente += temps_descente // 2

def controle_pion(commande, k, n_commande, *parametres):
    global event, Big_data, pointeur, nombre_restant_jetons, fin
    "commande[k * n_commande + 14] = sens du bouton"

    if event == 0:
        "pause"
        if pointeur != 0:
            canvas.delete(pointeur)
            pointeur = 0

        "si une pause a été faite alors que c'était fini"
        if fin != 0:
            fin = 0
            for index_pions_gagnants in Liste_index_pions_gagnants:
                canvas.itemconfigure(Liste_pion[index_pions_gagnants], outline=Liste_couleur[(1 + len(Big_data) + first) % 2])

        event = 1
        for corps_bouton in Liste_bouton[1]:
            canvas.itemconfigure(corps_bouton, fill='red')
        nombre_restant_jetons = len(Big_data)

    elif commande[k * n_commande + 14] == 2:
        "enlever un pion"
        if nombre_restant_jetons > 0:
            nombre_restant_jetons += -1
            supprimer_pion(nombre_restant_jetons)
            canvas.itemconfigure(Liste_bouton[2], fill='white')

    elif commande[k * n_commande + 14] == 0:
        if nombre_restant_jetons < len(Big_data):
            "rajouter un pion"
            canvas.itemconfigure(Liste_bouton[2], fill='red')
            jouer_pion(Big_data[:nombre_restant_jetons], Big_data[nombre_restant_jetons])
            nombre_restant_jetons += 1
            canvas.itemconfigure(Liste_bouton[2], fill='white')
        else:
            "peut pas rajouter un pion"
            canvas.itemconfigure(Liste_bouton[2], fill='blue')
    else:
        "depause"

        for corps_bouton in Liste_bouton[1]:
            canvas.itemconfigure(corps_bouton, fill='white')

        canvas.itemconfigure(Liste_bouton[2], fill='white')

        Big_data = Big_data[:nombre_restant_jetons]

        event = 0
        puissance_4()

"page"

Liste_modalite = ['longueur canvas', 400, 'largueur canvas', 400, 'largueur bouton', 40, 'largueur_texte', 24, 'epaiseur_texte', 4, 'couleur_bouton', 'white', 'couleur_texte_bouton', 'black', 'couleur_texte', 'white']

def page_menu(*parametres):

    canvas.config(width=Liste_modalite[1], height=Liste_modalite[3])

    "jouer"

    "1 joueur"
    Sacha_bouton(canvas=canvas, bouton=text, texte='1 joueur', commande=transfert, information=page_jeu, x=Liste_modalite[1] / 2, y=50, largueur=Liste_modalite[5], epaiseur=Liste_modalite[9], couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)
    "2 joueur"
    Sacha_bouton(canvas=canvas, bouton=text, texte='2 joueurs', commande=transfert, information=page_jeu, x=Liste_modalite[1] / 2, y=130, largueur=Liste_modalite[5], epaiseur=Liste_modalite[9], couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)

    "option"
    Sacha_bouton(canvas=canvas, bouton=text, texte='option', commande=transfert, information=page_option, x=Liste_modalite[1] / 2, y=250, largueur=Liste_modalite[5], epaiseur=Liste_modalite[9], couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)


def page_jeu(commande, k, n_commande, *parametres):
    global ecart_bord, nombre_joueur, Liste_pion, taille_rond, depart_decoupage, BigBig_data_symetrie

    ecart_bord = tgrille * 1
    place_droite = tgrille*4
    if nombre_joueur != 0:
        nombre_joueur = k + 1
    variable_a_definir(canvas, dimension, tgrille)

    canvas.config(width=tgrille*dimension[0] + ecart_bord*2 + place_droite, height=tgrille*dimension[1] + ecart_bord*2)

    Liste_pion, taille_rond = creation_terrain(Liste_couleur, ecart_bord)
    page_jeu_bouton(place_droite)

    depart_decoupage = len(BigBig_data)

    "dedouble la memoire avec la symétrie"
    BigBig_data_symetrie = []

    for partie in BigBig_data:
        BigBig_data_symetrie += [retourner_liste(partie[:-1]) + [partie[-1]]]

    initialisation_variable_partie()
    puissance_4()

def page_jeu_bouton(place_droite):
    global Liste_bouton

    "creation_bouton"

    Liste_bouton = []

    modalite = ['largueur_grille', tgrille * dimension[0] + ecart_bord * 2, 'longueur', tgrille*0.9, 'difference de x', 1.7 * tgrille, 'couleur', 'white', 'changement_couleur', 'red', 'pas de changement couleur', 'bouton', moins, plus, fleche, pause, 'ecart en y par rapport au bas et haut', tgrille*1.5]

    "plus, moins : changement vitesse de descente"
    for k in range(2):
        Sacha_bouton(canvas=canvas, bouton=modalite[k + 12], commande=variation_vitesse_descente, longueur=modalite[3], carre=1, epaiseur=tgrille * 0.2, x=modalite[1] + (place_droite - modalite[3] + (k * 2 - 1) * modalite[5]) / 2, y=modalite[17] - modalite[3]/2, couleur=modalite[7], changement_couleur_activation=modalite[9], temps_changement_couleur_activation=50, appuyer_relacher_maintenu=3)

    "fleches + pause : pour enlever des pions ou les remettre"
    for k in range(3):
        Liste_bouton += [Sacha_bouton(canvas=canvas, bouton=modalite[k % 2 + 14], sens=2 - k, commande=controle_pion, longueur=modalite[3] * 0.9, largueur=modalite[3] * 1.2, epaiseur=tgrille * 0.3, x=modalite[1] + (place_droite - modalite[3]) / 2 + (k - 1) * modalite[5] * 0.7, y=dimension[1]*tgrille + 2*ecart_bord - modalite[17] - modalite[3]/2, couleur=modalite[7], changement_couleur_activation=modalite[9 + (k + 1) // 2], temps_changement_couleur_activation=50)]

    "fonction pour déplacer le curseur et jouer"
    rajout_fonction('appuyer', 'm', recopier_memoire, 'q', deplacement_pointeur, 'd', deplacement_pointeur, 'space', activer_descente_pion)

    ecart = tgrille * 0.7
    modalite[3] = modalite[3]*0.65

    "menu"
    Sacha_bouton(canvas=canvas, bouton=text, texte='menu', commande=transfert, information=page_menu, x=modalite[1] + place_droite / 2, y=(dimension[1]*tgrille - modalite[3]) / 2 - ecart + ecart_bord, largueur=modalite[3], epaiseur=tgrille*0.08, couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)
    "recommencer"
    Sacha_bouton(canvas=canvas, bouton=text, texte='recommencer', commande=fin_partie, x=modalite[1] + place_droite / 2, y=(dimension[1]*tgrille - modalite[3]) / 2 + ecart + ecart_bord, largueur=modalite[3], epaiseur=tgrille*0.08, couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)


def page_option(*parametres):

    canvas.config(width=Liste_modalite[1], height=Liste_modalite[3])

    "menu"
    Sacha_bouton(canvas=canvas, bouton=text, texte='menu', commande=transfert, information=page_menu, x=Liste_modalite[1] / 2, y=30, largueur=Liste_modalite[5], epaiseur=Liste_modalite[9], couleur=Liste_modalite[11], couleur_texte=Liste_modalite[13], centrer=1)

    "tgrille"
    Sacha_texte(canvas=canvas, texte='taille grille', xt=Liste_modalite[1] / 2, yt=130, largueur=Liste_modalite[7], epaiseur_texte=Liste_modalite[9], couleur=Liste_modalite[15], centrer=1)
    Sacha_bouton(canvas=canvas, bouton=spinbox, texte=spinbox_range(30, 100), commande=recuperer_tgrille, information=tgrille - 30, x=Liste_modalite[1]/2, y=170, largueur=Liste_modalite[5], epaiseur_texte=Liste_modalite[9], couleur=Liste_modalite[13], couleur_annexe=Liste_modalite[13], couleur_texte=Liste_modalite[11], couleur_outline=Liste_modalite[11], changement_couleur_activation='red', centrer=1, appuyer_relacher_maintenu=3, temps_repetition_commande=100)

"récupérer variable"

def recuperer_tgrille(information):
    global tgrille

    tgrille = information

page_menu()

window.mainloop()