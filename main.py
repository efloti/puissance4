import os
from random import randint
NB_LIGNES, NB_COLONNES = 6, 7
# Conventions:
#    g:[[int]] représente la grille sous la forme d'une matrice ayant NB_LIGNES et NB_LIGNES
#        sous la forme d'une liste de liste où chaque liste interne représente une ligne.
#        Elles contient:
#           0: case vide; 1: 1er joueur; 2: 2ème joueur
#    i, j:int  représente un numéro de ligne et de colonne (donc une case).
#    jr:int représente le joueur (vaut 1 ou 2).


def grille_vide() -> "[[int]]":
    """Initialise la grille avec des 0"""
    pass


def afficher(g):
    """Affiche la grille dans la console avec
    'X' pour le premier joueur, 'O' pour le second, rien pour une case vide"""
    pass


def jouer(g, jr, j) -> "(int, int)":
    """Modifie la grille g (en place) si le joueur jr
    place son pion dans la colonne j; renvoie la case où
    le pion «atterit».
    Hypothèse: la colonne j n'est pas pleine
    """
    pass


def coup_possible(g, j) -> "bool":
    """Renvoie True si la colonne j n'est pas pleine.
    """
    pass


def coup_aleatoire(g, jr) -> "(int, int)":
    """joue un coup au hasard (en supposant que la grille n'est pas pleine.
    Renvoie la case où le pion est placé."""
    pass


def victoire(g, jr, i, j) -> "bool":
    """Renvoie true si le joueur jr qui a placé son pion
    dans la case i, j produit un alignement de 4 pions à lui."""


def match_nul(g) -> bool:
    """Renvoie True si la grille est pleine"""
    pass


def ordi_contre_ordi():
    """Réalise une partie de l'ordinateur contre lui-même."""
    pass
