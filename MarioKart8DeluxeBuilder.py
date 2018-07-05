# coding: utf-8

#===============================================================================
# Name        : MarioKart8DeluxeBuilder.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (10/06/2018)
# Description : Programme principal
#===============================================================================

if __name__ == '__main__':

    from Donnees import recupererPilotes, recupererPlaneurs, recupererPneus, recupererVehicules
    from Statistiques import Statistiques

    pilotes = recupererPilotes("donnees/Drivers.txt")
    vehicules = recupererVehicules("donnees/Bodies.txt")
    pneus = recupererPneus("donnees/Tires.txt")
    planeurs = recupererPlaneurs("donnees/Gliders.txt")

    filtrePilotes = []
    filtreVehicules = []
    filtrePneus = []
    filtrePlaneurs = []

    for nomPilote, pilote in sorted(pilotes.items()):
        if filtrePilotes and nomPilote not in filtrePilotes:
            continue
        for nomVehicule, vehicule in sorted(vehicules.items()):
            if filtreVehicules and nomVehicule not in filtreVehicules:
                continue
            for nomPneu, pneu in sorted(pneus.items()):
                if filtrePneus and nomPneu not in filtrePneus:
                    continue
                for nomPlaneur, planeur in sorted(planeurs.items()):
                    if filtrePlaneurs and nomPlaneur not in filtrePlaneurs:
                        continue
                    vitesseSol = (pilote.vitesseSol + vehicule.vitesseSol + pneu.vitesseSol +
                            planeur.vitesseSol + 3.0) / 4.0
                    vitesseEau = (pilote.vitesseEau + vehicule.vitesseEau + pneu.vitesseEau +
                            planeur.vitesseEau + 3.0) / 4.0
                    vitesseAir = (pilote.vitesseAir + vehicule.vitesseAir + pneu.vitesseAir +
                            planeur.vitesseAir + 3.0) / 4.0
                    vitesseAntiGravite = (pilote.vitesseAntiGravite + vehicule.vitesseAntiGravite +
                            pneu.vitesseAntiGravite + planeur.vitesseAntiGravite + 3.0) / 4.0
                    acceleration = (pilote.acceleration + vehicule.acceleration +
                            pneu.acceleration + planeur.acceleration + 3.0) / 4.0
                    poids = (pilote.poids + vehicule.poids + pneu.poids + planeur.poids + 3.0) / 4.0
                    maniabiliteSol = (pilote.maniabiliteSol + vehicule.maniabiliteSol +
                            pneu.maniabiliteSol + planeur.maniabiliteSol + 3.0) / 4.0
                    maniabiliteEau = (pilote.maniabiliteEau + vehicule.maniabiliteEau +
                            pneu.maniabiliteEau + planeur.maniabiliteEau + 3.0) / 4.0
                    maniabiliteAir = (pilote.maniabiliteAir + vehicule.maniabiliteAir +
                            pneu.maniabiliteAir + planeur.maniabiliteAir + 3.0) / 4.0
                    maniabiliteAntiGravite = (pilote.maniabiliteAntiGravite +
                            vehicule.maniabiliteAntiGravite + pneu.maniabiliteAntiGravite +
                            planeur.maniabiliteAntiGravite + 3.0) / 4.0
                    adherence = (pilote.adherence + vehicule.adherence + pneu.adherence +
                            planeur.adherence + 3.0) / 4.0
                    miniTurbo = (pilote.miniTurbo + vehicule.miniTurbo + pneu.miniTurbo +
                            planeur.miniTurbo + 3.0) / 4.0
                    statistiques = Statistiques(vitesseSol, vitesseEau, vitesseAir,
                            vitesseAntiGravite, acceleration, poids, maniabiliteSol, maniabiliteEau,
                            maniabiliteAir, maniabiliteAntiGravite, adherence, miniTurbo)
                    print "%s\t%s\t%s\t%s\t%s" % (nomPilote, nomVehicule, nomPneu, nomPlaneur,
                            str(statistiques).replace(" ", "\t"))
