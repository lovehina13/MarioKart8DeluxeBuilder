# coding: utf-8

#===============================================================================
# Name        : Planeur.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (05/07/2017)
# Description : Définition d'un planeur
#===============================================================================

from Statistiques import Statistiques


class Planeur(Statistiques):

    def __init__(self, nom=str(), vitesseSol=float(), vitesseEau=float(), vitesseAir=float(),
            vitesseAntiGravite=float(), acceleration=float(), poids=float(), maniabiliteSol=float(),
            maniabiliteEau=float(), maniabiliteAir=float(), maniabiliteAntiGravite=float(),
            adherence=float(), miniTurbo=float()):
        self.nom = nom
        super(Planeur, self).__init__(vitesseSol, vitesseEau, vitesseAir, vitesseAntiGravite,
                acceleration, poids, maniabiliteSol, maniabiliteEau, maniabiliteAir,
                maniabiliteAntiGravite, adherence, miniTurbo)

    def __str__(self):
        return "%s %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f %.2f" % (
                self.nom, self.vitesse, self.vitesseSol, self.vitesseEau, self.vitesseAir,
                self.vitesseAntiGravite, self.acceleration, self.poids, self.maniabilite,
                self.maniabiliteSol, self.maniabiliteEau, self.maniabiliteAir,
                self.maniabiliteAntiGravite, self.adherence, self.miniTurbo)
