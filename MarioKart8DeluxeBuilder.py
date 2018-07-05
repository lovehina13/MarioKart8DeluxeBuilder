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
    filtreStatistiques = {"vitesse": 0.0, "vitesseSol": 0.0, "vitesseEau": 0.0, "vitesseAir": 0.0,
            "vitesseAntiGravite": 0.0, "acceleration": 0.0, "poids": 0.0, "maniabilite": 0.0,
            "maniabiliteSol": 0.0, "maniabiliteEau": 0.0, "maniabiliteAir": 0.0,
            "maniabiliteAntiGravite": 0.0, "adherence": 0.0, "miniTurbo": 0.0}

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

                    if filtreStatistiques["vitesse"] and statistiques.vitesse < \
                            filtreStatistiques["vitesse"]:
                        continue
                    if filtreStatistiques["vitesseSol"] and statistiques.vitesseSol < \
                            filtreStatistiques["vitesseSol"]:
                        continue
                    if filtreStatistiques["vitesseEau"] and statistiques.vitesseEau < \
                            filtreStatistiques["vitesseEau"]:
                        continue
                    if filtreStatistiques["vitesseAir"] and statistiques.vitesseAir < \
                            filtreStatistiques["vitesseAir"]:
                        continue
                    if filtreStatistiques["vitesseAntiGravite"] and \
                            statistiques.vitesseAntiGravite < filtreStatistiques["vitesseAntiGravite"]:
                        continue
                    if filtreStatistiques["acceleration"] and statistiques.acceleration < \
                            filtreStatistiques["acceleration"]:
                        continue
                    if filtreStatistiques["poids"] and statistiques.poids < \
                            filtreStatistiques["poids"]:
                        continue
                    if filtreStatistiques["maniabilite"] and statistiques.maniabilite < \
                            filtreStatistiques["maniabilite"]:
                        continue
                    if filtreStatistiques["maniabiliteSol"] and statistiques.maniabiliteSol < \
                            filtreStatistiques["maniabiliteSol"]:
                        continue
                    if filtreStatistiques["maniabiliteEau"] and statistiques.maniabiliteEau < \
                            filtreStatistiques["maniabiliteEau"]:
                        continue
                    if filtreStatistiques["maniabiliteAir"] and statistiques.maniabiliteAir < \
                            filtreStatistiques["maniabiliteAir"]:
                        continue
                    if filtreStatistiques["maniabiliteAntiGravite"] and \
                            statistiques.maniabiliteAntiGravite < \
                            filtreStatistiques["maniabiliteAntiGravite"]:
                        continue
                    if filtreStatistiques["adherence"] and statistiques.adherence < \
                            filtreStatistiques["adherence"]:
                        continue
                    if filtreStatistiques["miniTurbo"] and statistiques.miniTurbo < \
                            filtreStatistiques["miniTurbo"]:
                        continue

                    print "%s\t%s\t%s\t%s\t%s" % (nomPilote, nomVehicule, nomPneu, nomPlaneur,
                            str(statistiques).replace(" ", "\t"))
