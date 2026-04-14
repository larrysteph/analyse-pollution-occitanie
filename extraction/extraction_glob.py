import csv
import sqlite3

path_bdd = "BDProjetStat.db"
db = sqlite3.connect(path_bdd)
curs = db.cursor()


requete_fusion = """
SELECT 
    P.code_insee_com, 
    G.nom_com, 
    P.nom_poll, 
    AVG(P.valeur_poll) as moyenne_pollution,
    G.population, 
    G.Force_vent_med, 
    G.Tmax_med,
    S.MED21 
FROM Pollution P
JOIN Données_geo G ON P.code_insee_com = G.code_insee_com
JOIN Socio_Eco S ON P.code_insee_com = S.code_insee_com
GROUP BY P.code_insee_com, P.nom_poll
"""

print("Extraction des données enrichies...")
curs.execute(requete_fusion)
resultats = curs.fetchall()


with open('Donnees_Pour_R.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([
        'code_insee_com', 'nom_commune', 'nom_poll', 'valeur_poll', 
        'population', 'Force_vent_med', 'Tmax_med', 'revenu_median'
    ])
    writer.writerows(resultats)

print(f"Terminé : {len(resultats)} lignes extraites.")
db.close()