Analyse de la Pollution de l'Air en Occitanie
Ce projet a été réalisé dans le cadre de l'UE 403 (Informatique et Statistiques) en L2 MIASHS. Il combine l'ingénierie de données via Python/SQL et l'analyse statistique sous R.

Structure du Projet
L'organisation des fichiers suit la logique du flux de traitement des données :

scripts_python/ : Dossier contenant les scripts unitaires pour la gestion de la base de données.

donnees_geo.py : Importation des variables climatiques.

qualite_air.py : Intégration des mesures de pollution.

sociaux_eco.py : Données sur le niveau de vie.

main_extraction.py : Script global assurant la fusion des tables (JOINS) et l'exportation du dataset final au format CSV.

analyse_statistique.Rmd : Rapport complet intégrant le code source R, les quatre problématiques étudiées et les visualisations.

data/ : Répertoire contenant le dataset fusionné nommé Donnees_Pour_R.csv.

assets/ : Schémas techniques et diagrammes d'activité illustrant le workflow du projet.

Installation et Utilisation
Cloner le dépôt sur votre machine locale.

Exécuter les scripts Python pour générer la base de données relationnelle BDProjetStat.db.

Lancer l'analyse sous RStudio en ouvrant le fichier .Rmd pour générer le rapport final.

Résultats Clés de l'Analyse
Ozone (O3) : Mise en évidence d'une corrélation positive marquée avec la température maximale.

Dioxyde d'Azote (NO2) : Identification d'un lien direct avec la densité de population, particulièrement visible pour les métropoles de Toulouse et Montpellier.

Facteurs socio-économiques : Absence de lien linéaire significatif entre le revenu médian des communes et les taux de pollution globale.

Auteur
Essabe Mbome Oye Larry Stephane - Groupe 14

Projet universitaire - Avril 2026
