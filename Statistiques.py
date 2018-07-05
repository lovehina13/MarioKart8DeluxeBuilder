# coding: utf-8

#===============================================================================
# Name        : Statistiques.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (05/07/2017)
# Description : Définition des statistiques
#===============================================================================


class Statistiques(object):

    def __init__(self, vitesseSol=float(), vitesseEau=float(), vitesseAir=float(),
            vitesseAntiGravite=float(), acceleration=float(), poids=float(), maniabiliteSol=float(),
            maniabiliteEau=float(), maniabiliteAir=float(), maniabiliteAntiGravite=float(),
            adherence=float(), miniTurbo=float()):
        self.vitesse = float()
        self.vitesseSol = vitesseSol
        self.vitesseEau = vitesseEau
        self.vitesseAir = vitesseAir
        self.vitesseAntiGravite = vitesseAntiGravite
        self.acceleration = acceleration
        self.poids = poids
        self.maniabilite = float()
        self.maniabiliteSol = maniabiliteSol
        self.maniabiliteEau = maniabiliteEau
        self.maniabiliteAir = maniabiliteAir
        self.maniabiliteAntiGravite = maniabiliteAntiGravite
        self.adherence = adherence
        self.miniTurbo = miniTurbo
        self.calculerVitesse()
        self.calculerManiabilite()

    def __str__(self):
        return "%.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f" % (
                self.vitesse, self.vitesseSol, self.vitesseEau, self.vitesseAir,
                self.vitesseAntiGravite, self.acceleration, self.poids, self.maniabilite,
                self.maniabiliteSol, self.maniabiliteEau, self.maniabiliteAir,
                self.maniabiliteAntiGravite, self.adherence, self.miniTurbo)

    def calculerVitesse(self):
        self.vitesse = (self.vitesseSol + self.vitesseEau + self.vitesseAir +
                self.vitesseAntiGravite) / 4.0

    def calculerManiabilite(self):
        self.maniabilite = (self.maniabiliteSol + self.maniabiliteEau + self.maniabiliteAir +
                self.maniabiliteAntiGravite) / 4.0
