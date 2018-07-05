# coding: utf-8

#===============================================================================
# Name        : Vehicule.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (05/07/2017)
# Description : Définition d'un véhicule
#===============================================================================

from Statistiques import Statistiques


class Vehicule(Statistiques):

    def __init__(self, nom=str(), vitesse_sol=float(), vitesse_eau=float(), vitesse_air=float(),
            vitesse_anti_gravite=float(), acceleration=float(), poids=float(),
            maniabilite_sol=float(), maniabilite_eau=float(), maniabilite_air=float(),
            maniabilite_anti_gravite=float(), adherence=float(), mini_turbo=float()):
        self.nom = nom
        super(Vehicule, self).__init__(vitesse_sol, vitesse_eau, vitesse_air, vitesse_anti_gravite,
                acceleration, poids, maniabilite_sol, maniabilite_eau, maniabilite_air,
                maniabilite_anti_gravite, adherence, mini_turbo)
