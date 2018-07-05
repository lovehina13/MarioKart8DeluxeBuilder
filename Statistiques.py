# coding: utf-8

#===============================================================================
# Name        : Statistiques.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (05/07/2017)
# Description : Définition des statistiques
#===============================================================================


class Statistiques(object):

    def __init__(self, vitesse_sol=float(), vitesse_eau=float(), vitesse_air=float(),
            vitesse_anti_gravite=float(), acceleration=float(), poids=float(),
            maniabilite_sol=float(), maniabilite_eau=float(), maniabilite_air=float(),
            maniabilite_anti_gravite=float(), adherence=float(), mini_turbo=float()):
        self.vitesse = float()
        self.vitesse_sol = vitesse_sol
        self.vitesse_eau = vitesse_eau
        self.vitesse_air = vitesse_air
        self.vitesse_anti_gravite = vitesse_anti_gravite
        self.acceleration = acceleration
        self.poids = poids
        self.maniabilite = float()
        self.maniabilite_sol = maniabilite_sol
        self.maniabilite_eau = maniabilite_eau
        self.maniabilite_air = maniabilite_air
        self.maniabilite_anti_gravite = maniabilite_anti_gravite
        self.adherence = adherence
        self.mini_turbo = mini_turbo
        self.calculerVitesse()
        self.calculerManiabilite()

    def calculerVitesse(self):
        self.vitesse = (self.vitesse_sol + self.vitesse_eau + self.vitesse_air +
                self.vitesse_anti_gravite) / 4.0

    def calculerManiabilite(self):
        self.maniabilite = (self.maniabilite_sol + self.maniabilite_eau + self.maniabilite_air +
                self.maniabilite_anti_gravite) / 4.0
