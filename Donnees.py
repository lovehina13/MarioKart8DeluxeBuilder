# coding: utf-8

#===============================================================================
# Name        : Donnees.py
# Author      : Alexis Foerster (alexis.foerster@gmail.com)
# Version     : 1.0 (05/07/2017)
# Description : Récupération des données
#===============================================================================


def recupererPilotes(nomFichier):
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import separerEtConvertirTexte
    from Pilote import Pilote
    pilotes = {}
    lignes = lireFichier(nomFichier)
    for ligne in lignes[1:]:
        elements = separerEtConvertirTexte(ligne, ";")
        pilote = Pilote(elements[0], elements[1], elements[2], elements[3], elements[4],
                elements[5], elements[6], elements[7], elements[8], elements[9], elements[10],
                elements[11], elements[12], elements[13])
        pilotes[pilote.nom] = pilote
    return pilotes


def recupererVehicules(nomFichier):
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import separerEtConvertirTexte
    from Vehicule import Vehicule
    vehicules = {}
    lignesVehicules = lireFichier(nomFichier)
    for ligne in lignesVehicules[1:]:
        elements = separerEtConvertirTexte(ligne, ";")
        vehicule = Vehicule(elements[0], elements[1], elements[2], elements[3], elements[4],
                elements[5], elements[6], elements[7], elements[8], elements[9], elements[10],
                elements[11], elements[12])
        vehicules[vehicule.nom] = vehicule
    return vehicules


def recupererPneus(nomFichier):
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import separerEtConvertirTexte
    from Pneu import Pneu
    pneus = {}
    lignesPneus = lireFichier(nomFichier)
    for ligne in lignesPneus[1:]:
        elements = separerEtConvertirTexte(ligne, ";")
        pneu = Pneu(elements[0], elements[1], elements[2], elements[3], elements[4], elements[5],
                elements[6], elements[7], elements[8], elements[9], elements[10], elements[11],
                elements[12])
        pneus[pneu.nom] = pneu
    return pneus


def recupererPlaneurs(nomFichier):
    from LectureEcritureFichier import lireFichier
    from OperationsTexte import separerEtConvertirTexte
    from Planeur import Planeur
    planeurs = {}
    lignesPlaneurs = lireFichier(nomFichier)
    for ligne in lignesPlaneurs[1:]:
        elements = separerEtConvertirTexte(ligne, ";")
        planeur = Planeur(elements[0], elements[1], elements[2], elements[3], elements[4],
                elements[5], elements[6], elements[7], elements[8], elements[9], elements[10],
                elements[11], elements[12])
        planeurs[planeur.nom] = planeur
    return planeurs
