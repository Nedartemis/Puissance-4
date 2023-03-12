from tkinter import *
from time import time, sleep
import math
from random import randint
from Sacha_bouton import *

def variable_a_definir(v0, v1, v2):
    global canvas, dimension, tgrille

    canvas, dimension, tgrille = v0, v1, v2


def approche_horizontale(position_play, k, sens):

    return (position_play[0] + k * (-1) ** (1 - sens), position_play[1])


def approche_verticale(position_play, k, sens):

    return (position_play[0], position_play[1] + k * (-1) ** (1 - sens))


def approche_diagonale_1(position_play, k, sens):

    return (position_play[0] + k * (-1) ** (1 - sens), position_play[1] + k * (-1) ** (1 - sens))


def approche_diagonale_2(position_play, k, sens):

    return (position_play[0] + k * (-1) ** (1 - sens), position_play[1] + k * (-1) ** (sens))


def creation_terrain(Liste_couleur, ecart_bord):

    taille_rond = tgrille*0.75
    epaiseur = tgrille-taille_rond
    Liste_pion = []

    "creation de tout les jetons"
    for k in range(dimension[0] * dimension[1]):
        coord = (tgrille - taille_rond) / 2 + ecart_bord, (tgrille - taille_rond) / 2 - 2*tgrille, (tgrille + taille_rond) / 2 + ecart_bord, (tgrille + taille_rond) / 2 - 2*tgrille
        Liste_pion += [canvas.create_oval(coord, fill=Liste_couleur[k % 2], width=8, outline=Liste_couleur[k % 2])]

    "verticale"
    for y in range(dimension[0] + 1):
        coord = y * tgrille + ecart_bord, ecart_bord - epaiseur/2, y * tgrille + ecart_bord, dimension[1] * tgrille + ecart_bord + epaiseur/2
        canvas.create_line(coord, fill=Liste_couleur[2], width=epaiseur)

        if y != dimension[0]:
            "contenant rond"
            for x in range(dimension[1]):
                coord = y * tgrille + (tgrille-taille_rond)/2 - epaiseur/2 + ecart_bord, x * tgrille + (tgrille-taille_rond)/2 - epaiseur/2 + ecart_bord, y * tgrille + (tgrille+taille_rond)/2 + epaiseur/2 + ecart_bord, x * tgrille + (tgrille+taille_rond)/2 + epaiseur/2 + ecart_bord
                canvas.create_oval(coord, outline=Liste_couleur[2], width=epaiseur)

    "horizontale"
    for x in range(dimension[1] + 1):
        coord = ecart_bord, x * tgrille + ecart_bord, dimension[0] * tgrille + ecart_bord, x * tgrille + ecart_bord
        canvas.create_line(coord, fill=Liste_couleur[2], width=epaiseur)

    epaiseur = ecart_bord*0.1
    coord = epaiseur/2, epaiseur/2, dimension[0]*tgrille + ecart_bord*2 - epaiseur/2, dimension[1]*tgrille + ecart_bord*2 - epaiseur/2
    canvas.create_rectangle(coord, outline='white', width=epaiseur)

    return Liste_pion, taille_rond

def definir_les_coordonnees(Liste_partie, numero):
    global Liste_position_play

    Liste_position_play = []

    for index in range(len(Liste_partie)):

        "Liste_position_play += [(x, y)]"
        Liste_position_play += [(Liste_partie[index], Liste_partie[:index].count(Liste_partie[index]))]

    if numero == 'garder les deux':

        Liste_position_play = separer_liste(Liste_position_play)

    elif numero != 'ne pas séparer':

        Liste_position_play = separer_liste(Liste_position_play)[numero]

    return Liste_position_play

def definir_Liste_play_a_ne_pas_faire(Liste_partie):

    Liste_play_a_ne_pas_faire = []

    for potentiel_play in range(dimension[0]):

        if Liste_partie.count(potentiel_play) < dimension[1] - 1:

            for l in range(2):
                Liste_partie += [potentiel_play]

            puissance_4 = verification_puissance_4(Liste_partie, 1 - len(Liste_partie) % 2)

            Liste_partie = Liste_partie[:-2]

            if puissance_4 != 0:
                Liste_play_a_ne_pas_faire += [potentiel_play]

    return Liste_play_a_ne_pas_faire


def recherche_double_puissance_4(Liste_partie):

    x = 0
    nombre_puissance_4 = 0

    Liste_position_play = definir_les_coordonnees(Liste_partie, len(Liste_partie)%2)
    Liste_position_play_adversaire = definir_les_coordonnees(Liste_partie, (len(Liste_partie) + 1)%2)

    #print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    while x < dimension[0] and nombre_puissance_4 < 2:

        nombre_puissance_4 = 0

        #print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')

        for y in range(Liste_partie.count(x) + 1, dimension[1]):

            Liste_position_play += [(x, y)]
            Liste_position_play_adversaire += [(x, y)]

            #print(Liste_position_play, Liste_position_play_adversaire)

            puissance_4 = verification_puissance_4(Liste_position_play, 'pas nécessaire', 'Liste_position_play')
            puissance_4_adversaire = verification_puissance_4(Liste_position_play_adversaire, 'pas nécessaire', 'Liste_position_play')

            Liste_position_play = Liste_position_play[:-1]
            Liste_position_play_adversaire = Liste_position_play_adversaire[:-1]

            #print(puissance_4, puissance_4_adversaire)

            if puissance_4 == 1:
                nombre_puissance_4 += 1

            else:
                nombre_puissance_4 = 0

            if nombre_puissance_4 == 2 or puissance_4_adversaire == 1:
                break

        x += 1

    if nombre_puissance_4 == 2:
        return x - 1
    else:
        return dimension[0] + 10

def retourner_liste(Liste):

    "symétriquement"
    nouvelle_liste = []
    for position in Liste:
        nouvelle_liste += [dimension[0] - 1 - position]

    return nouvelle_liste

def separer_liste(Liste):

    Liste_dedouble = [[], []]

    for index in range(len(Liste)):

        Liste_dedouble[index%2] += [Liste[index]]

    return Liste_dedouble

def strategie_aleatoire(Big_data, Liste_play_a_ne_pas_faire, *parametres):

    "aleatoire"

    Liste_potentiel_play = []

    for play in range(dimension[0]):
        if Big_data.count(play) < dimension[1] and not play in Liste_play_a_ne_pas_faire:
            Liste_potentiel_play += [play]

    if len(Liste_potentiel_play) > 0:
        return Sacha_random(Liste_potentiel_play)

    else:
        return Liste_play_a_ne_pas_faire[-1]

def strategie_logique(Big_data, Liste_play_a_ne_pas_faire, *parametres):

    "logique"

    Liste_nombre_possibilite = [0] * dimension[0]

    "approche horizontale, verticale, diagonole gaughe-bas-->droite-haut, diagonale droite-bas-->gauche-haut"
    Liste_approche = [approche_horizontale, approche_verticale, approche_diagonale_1, approche_diagonale_2]

    "établir la liste des positions des jetons des différents joueurs (les tiens puis les siens)"
    Liste_position_play_Big_data = [definir_les_coordonnees(Big_data, len(Big_data) % 2), definir_les_coordonnees(Big_data, 1 - len(Big_data) % 2)]

    Liste_play_que_ne_veux_pas_faire_l_adversaire = [definir_Liste_play_a_ne_pas_faire(Big_data.copy() + [-100])]

    "attribuer le nombre de possibilité à chacun des plays"
    for play in range(dimension[0]):

        if Big_data.count(play) >= dimension[1]:
            "impossible d'y jouer puiqu'il sort de la grille"
            Liste_nombre_possibilite[play] = -300000

        elif play in Liste_play_a_ne_pas_faire:
            "marquer tout les play à ne pas faire pour les mieux les repérer"
            Liste_nombre_possibilite[play] = -100000

        else:

            "peut être qu'augmenter le y de 1 le fera sortir de la grille"
            if Big_data.count(play) + 1 >= dimension[1]:
                repetition = 1
            else:
                repetition = 2
                "cette liste diffère de Liste_play_que_ne_veux_pas_faire_l_adversaire puisque celle_ci est défini en fonction de la position une fois plus haute"
                Liste_play_que_ne_veux_pas_faire_l_adversaire += [definir_Liste_play_a_ne_pas_faire(Big_data.copy() + [play])]

                #if Liste_play_que_ne_veux_pas_faire_l_adversaire[1] != []:

                    # print('roundp =', roundp, ', play =', play, ', Liste_play_que_ne_veux_pas_faire_l_adversaire =', Liste_play_que_ne_veux_pas_faire_l_adversaire)

            "on regarde aussi les possibilités perdus (pour toi) et offert à l'adversaire : on regarde du coup les possibiltés de la position juste au dessus"
            for position_y in range(repetition):

                "établir la positions du play potentiel ; si position == 1 alors c'est pour regarder la position au dessus"
                position_play = definir_les_coordonnees(Big_data + [play] * (1 + position_y), (len(Big_data) + position_y) % 2)[-1]
                # print('roundp =', roundp, ', play =', play, ', position_y =', position_y, ', position_play =', position_play)

                "comme l'adversaire ne devrait pas jouer ce play puisque cela te ferait gagner, tu ne dois pas essayer de le bloquer sur cette position ou si position_y == 1, ne pas t'en préocuper tout court"
                if play in Liste_play_que_ne_veux_pas_faire_l_adversaire[position_y]:
                    repetition = 1 - position_y
                else:
                    repetition = 2

                # print('roundp =', roundp, ', play =', play, ', position_y =', position_y, ', repetition =', repetition)

                for joueur in range(repetition):

                    "approche horizontale, verticale, diagonole gaughe-bas-->droite-haut, diagonale droite-bas-->gauche-haut"
                    for approche in Liste_approche:

                        nombre_jeton, nombre_case_disponible, nombre_case_disponible_directement = 0, 0, 0

                        for sens in range(2):

                            for avancement in range(1, 4):

                                position_entourage = approche(position_play, avancement, sens)

                                if position_entourage[0] < 0 or position_entourage[0] > dimension[0] - 1 or position_entourage[1] < 0 or position_entourage[1] > dimension[1] - 1 or position_entourage in Liste_position_play_Big_data[1 - joueur]:
                                    "tu es hors de la grille ou y'a ton adversaire qui y est donc ça va bloquer pour tout les autres"
                                    break

                                elif position_entourage in Liste_position_play_Big_data[joueur]:
                                    "une position où tu as déjà un jeton"
                                    nombre_jeton += 1

                                elif not position_entourage in Liste_position_play_Big_data[1 - joueur]:
                                    "en gros c'est une position vide donc tu pourras t'y poser"

                                    if Big_data.count(position_entourage[0]) == position_entourage[1]:
                                        nombre_case_disponible_directement += 1
                                    else:
                                        nombre_case_disponible += 1

                                else:
                                    print('lol, y a un probleme au niveau de l attribution de possibilité')

                        if position_y == 1 and approche == approche_verticale:
                            "il va compter la case qui est juste en dessous de lui, je rectifie le tir"
                            nombre_case_disponible_directement = 0

                        "si la somme est inférieur ou égale à deux alors ça ne sert à rien puisque que c'est un puissance 4"
                        if nombre_jeton + nombre_case_disponible_directement + nombre_case_disponible > 2:
                            "les notes sont ce qui a de plus difficile à juger ; elles sont positives lorsque ça compte le nombre de possibilité que tu gagnes mais sont négatives quand elles peuvent offrir des possibilités à ton adversaire"
                            Liste_nombre_possibilite[play] += ((nombre_jeton ** 3) * 2 + (nombre_case_disponible_directement*2) ** 2 + nombre_case_disponible) * (-0.5) ** position_y

                if position_y == 1:
                    Liste_play_que_ne_veux_pas_faire_l_adversaire = Liste_play_que_ne_veux_pas_faire_l_adversaire[:-1]
                    # print('roundp =', roundp, ', play =', ', position_y =', position_y, play, ', Liste_play_que_ne_veux_pas_faire_l_adversaire =', Liste_play_que_ne_veux_pas_faire_l_adversaire)

    "-300 000 signifie impossiple, -100 000 précise que ce play est dans la liste à ne pas faire et 0 signifie souvent que la position juste au dessus te faisait gagner"
    # print(roundp, Liste_nombre_possibilite)

    "petite aide supplementaire qui n'a rien à voir avec le reste, on essaye de voir s'il y a deux solutions gagnantes à la suite"
    position = recherche_double_puissance_4(Big_data)
    if position < dimension[0]:
        print(Liste_nombre_possibilite)
        Liste_nombre_possibilite[position] += 10
        print(Liste_nombre_possibilite)

    "c'est le signe d'une stratégie mixte"
    if 'mixte' in parametres:
        return Liste_nombre_possibilite

    "prendre le play avec la meilleur note"
    meileur_nombre_possibilite = -200000
    for play in range(dimension[0]):
        if Liste_nombre_possibilite[play] > meileur_nombre_possibilite:
            position = play
            meileur_nombre_possibilite = Liste_nombre_possibilite[play]

    return position



def strategie_memoire(Big_data, Liste_play_a_ne_pas_faire, Big_data_selective, *parametres):

    "memoire"

    Liste_position_play_Big_data = []

    roundp = len(Big_data)

    "établir les positions de chaque play potentiel"
    for play in range(dimension[0]):
        Liste_position_play_Big_data += [definir_les_coordonnees(Big_data + [play], len(Big_data) % 2)[-1]]

    # print(roundp, 'Liste_position_play_Big_data =', Liste_position_play_Big_data)

    Liste_note = [0] * dimension[0]

    for partie_memorise in Big_data_selective:

        Liste_position_play_partie_memorise = definir_les_coordonnees(partie_memorise[:-1], len(Big_data) % 2)

        # print(roundp, 'Liste_position_play_partie_memorise =', Liste_position_play_partie_memorise)

        "définir la note donné au play si la liste correspond"
        if partie_memorise[-1] == -(roundp % 2 + 1):
            "gagné"
            note = 2
        elif partie_memorise[-1] == -3:
            "égalité"
            note = -1
        else:
            "perdu"
            note = -2

        # print(roundp, 'note =', note)

        play = partie_memorise[roundp]
        Liste_note[play] += note

    # print(roundp, 'Liste_note =', Liste_note, len(Big_data_selective))

    "c'est le signe d'une stratégie mixte"
    if 'mixte' in parametres:
        return Liste_note

    #print(Liste_note)

    "sélection du meilleur play en comparant les valeurs"
    meilleur_note = -100000000000000000000000000000000000000000
    "il faut faire deux tours puiqu'il est possible que l'ordi puisse seulement jouer un play qui est dans la Liste_play_a_ne_pas_faire"
    for tour in range(2):
        if meilleur_note == -100000000000000000000000000000000000000000:
            for play in range(dimension[0]):
                if Liste_note[play] > meilleur_note and Big_data.count(play) < dimension[1] and not play + dimension[0] * tour in Liste_play_a_ne_pas_faire:
                    meilleur_note = Liste_note[play]
                    position = play

    return position

def strategie_mixte_logique_memoire(Big_data, Liste_play_a_ne_pas_faire, Big_data_selective, *parametres):

    Liste_note_possibilite = strategie_logique(Big_data, Liste_play_a_ne_pas_faire, 'mixte')
    #print(Liste_note_possibilite, 1)

    Liste_note_memoire = strategie_memoire(Big_data, 'pas besoin', Big_data_selective, 'mixte')
    #print(Liste_note_memoire, 2)

    Liste_note = [0]*dimension[0]

    for play in range(dimension[0]):

        Liste_note[play] = Liste_note_possibilite[play] + Liste_note_memoire[play]*1

    #print(Liste_nombre_possibilite, Liste_note_memoire, Liste_note)

    meilleur_note = -200000

    for play in range(dimension[0]):
        if Liste_note[play] > meilleur_note:
            meilleur_note = Liste_note[play]
            position = play

    return position

def strategie_memoire_ou_logique(Big_data, Liste_play_a_ne_pas_faire, Big_data_selective, *parametres):

    if len(Big_data_selective) > 0:

        position = strategie_memoire(Big_data, Liste_play_a_ne_pas_faire, Big_data_selective, *parametres)

    else:

        position = strategie_logique(Big_data, Liste_play_a_ne_pas_faire, *parametres)

    return position


def trier_memoire(Big_data, Big_data_selective, Big_data_repechage):

    roundp = len(Big_data) - 1

    "vérifie dans sa mémoire s'il a déja fait une partie similaire #Big_data_selective"
    index = 0
    while index < len(Big_data_selective):

        partie_memorise = Big_data_selective[index].copy()

        Liste_position_play_partie_memorise = definir_les_coordonnees(partie_memorise[:-1], 'ne pas séparer')

        Liste_position_play_Big_data = definir_les_coordonnees(Big_data, 1 - len(Big_data) % 2)

        "si la position du dernier jeton n'est pas dans... mais si elle n'est nul part (c'est à dire ni dans la liste de tes jetons ni dans ccelle de l'adversaire) alors la partie n'est pas supprimé étant donné qu'on peut toujours espérer avoir la même fin donc être influencer par cette partie"
        if Liste_position_play_Big_data[-1] != Liste_position_play_partie_memorise[roundp]:
            Big_data_repechage += [Big_data_selective[index]]
            Big_data_selective.pop(index)
        else:
            index += 1

    "trier Big_data_repechage"
    index = 0
    while index < len(Big_data_repechage):

        partie_repechage = Big_data_repechage[index].copy()

        Liste_position_play_partie_memorise = definir_les_coordonnees(partie_repechage, 1 - len(Big_data) % 2)

        Liste_position_play_Big_data = definir_les_coordonnees(Big_data, 1 - len(Big_data) % 2)

        if not Liste_position_play_Big_data[-1] in Liste_position_play_partie_memorise:
            "effaçage définitif"
            Big_data_repechage.pop(index)

        else:

            etat = 0

            Liste_position_play_Big_data = definir_les_coordonnees(Big_data, 'garder les deux')

            Liste_position_play_partie_memorise = definir_les_coordonnees(partie_repechage[:roundp + 1], 'garder les deux')

            for k in range(2):

                if trier_position(Liste_position_play_partie_memorise[k]) != trier_position(Liste_position_play_Big_data[k]):
                    etat = 1

            "si les listes sont exactment pareil"
            if etat == 0:
                "le placer dans Big_data_selective"
                Big_data_selective += [Big_data_repechage[index]]
                Big_data_repechage.pop(index)

            index += 1

    #print(len(Big_data_selective), Big_data_selective)

    return Big_data_selective, Big_data_repechage

def tour_ordi(Big_data, Big_data_selective, Strategie_IA, first):

    puissance_4 = 0

    "vérification si peut directement gagné ou contrer directement l'adversaire"
    "il va essayer toutes les possibilités de son coté et du cote adversaire et voir si cela donne sa victoire ou celle de son adversaire"

    for joueur in range(2):

        Liste_partie = Big_data.copy()

        if joueur == 1:
            Liste_partie += [-100]

        numero = len(Liste_partie) % 2

        position = 0
        while position != 7 and puissance_4 == 0:

            "définir les coordonnées de l'adversaire en lui rajoutant chaque play"
            Liste_partie += [position]

            if Liste_partie.count(position) <= dimension[1]:
                puissance_4 = verification_puissance_4(Liste_partie, numero)

            Liste_partie = Liste_partie[:-1]

            position += 1

        if puissance_4 != 0:
            break

    if puissance_4 != 0:

        return position - 1

    else:

        "définir le play à ne pas faire : si apres un certain play l'adverdsaire pourra directement gagné"
        Liste_play_a_ne_pas_faire = definir_Liste_play_a_ne_pas_faire(Big_data.copy())

        # print(roundp, 'Liste_play_a_ne_pas_faire =', Liste_play_a_ne_pas_faire)

        "strategie demande"
        position = Strategie_IA[(len(Big_data) + first) % 2](Big_data, Liste_play_a_ne_pas_faire, Big_data_selective)

        return position

def trier_position(Liste_donne):

    Liste_nouvelle = []

    for position in Liste_donne:

        index = 0

        taille_liste = len(Liste_nouvelle)

        while index < taille_liste and position[0] >= Liste_nouvelle[index][0] and (position[0] > Liste_nouvelle[index][0] or position[1] > Liste_nouvelle[index][1]):

            index += 1

        Liste_nouvelle = Liste_nouvelle[:index] + [position] + Liste_nouvelle[index:]

    return Liste_nouvelle

def verification_puissance_4(Liste_partie, joueur, *parametres):

    if parametres == ('Liste_position_play',):
        Liste_position_play = Liste_partie
    else:
        Liste_position_play = definir_les_coordonnees(Liste_partie, joueur)

    fin = 0
    k = 0
    h, v, d1, d2 = 0, 0, 0, 0

    while k != dimension[0] * dimension[1] and fin == 0:

        if k % dimension[0] == 0:
            h, d1, d2 = 0, 0, 0

        if k % dimension[1] == 0:
            v = 0

        "horizontale"
        if (k % dimension[0], k // dimension[0]) in Liste_position_play:
            h += 1
        else:
            h = 0

        "verticale"
        if (k // dimension[1], k % dimension[1]) in Liste_position_play:
            v += 1
        else:
            v = 0

        "diagonole gaughe-bas-->droite-haut"
        if (k % dimension[0], k % dimension[0] - 3 + k // dimension[0]) in Liste_position_play:
            d1 += 1
        else:
            d1 = 0

        "diagonale droite-bas-->gauche-haut"
        if (dimension[0] - 1 - k % dimension[0], k % dimension[0] - 3 + k // dimension[0]) in Liste_position_play:
            d2 += 1
        else:
            d2 = 0

        if h == 4 or v == 4 or d1 == 4 or d2 == 4:
            fin = 1

        k = k + 1


    if parametres == ('retrouver pions gagnants',):

        if fin == 0:
            return 0, 0, 0

        Liste = [h, v, d1, d2]
        return fin, k-1, Liste.index(4)

    else:
        return fin

