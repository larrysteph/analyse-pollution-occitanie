import csv
import sqlite3
import os


db = sqlite3.connect("BDProjetStat.db")
curs = db.cursor()

# 2. Création de la table
curs.execute("DROP TABLE IF EXISTS Données_geo")
curs.execute("""
    CREATE TABLE IF NOT EXISTS Données_geo (
        code_insee_com TEXT PRIMARY KEY, nom_com TEXT, reg_code INTEGER, reg_nom TEXT,
        dep_code INTEGER, dep_nom TEXT, population INTEGER, superficie REAL,
        densite REAL, latitude REAL, longitude REAL, densite_cat TEXT,
        altitude_med REAL, RR_med REAL, NBJRR1_med REAL, NBJRR5_med REAL,
        NBJRR10_med REAL, Tmin_med REAL, Tmax_med REAL, Tens_vap_med REAL,
        Force_vent_med REAL, Insolation_med REAL, Rayonnement_med REAL
    )
""")


found_file = None
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.csv') and 'donnees_geo_climatiques' in file:
            found_file = os.path.join(root, file)
            break

if found_file:
    print(f"Fichier trouvé : {found_file}")
    try:
        with open(found_file, mode='r', encoding='utf-8-sig') as file: # utf-8-sig gère mieux les fichiers Excel
            reader = csv.DictReader(file)
            
            for i in reader:
                curs.execute("""
                    INSERT INTO Données_geo (
                        code_insee_com, nom_com, reg_code, reg_nom, dep_code, dep_nom, population,
                        superficie, densite, latitude, longitude, densite_cat, altitude_med, RR_med, 
                        NBJRR1_med, NBJRR5_med, NBJRR10_med, Tmin_med, Tmax_med, Tens_vap_med, Force_vent_med, 
                        Insolation_med, Rayonnement_med
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    i.get('code_insee_com'), i.get('nom_com'), i.get('reg_code'), i.get('reg_nom'), 
                    i.get('dep_code'), i.get('dep_nom'), i.get('population'), i.get('superficie_km2'), 
                    i.get('densite'), i.get('latitude'), i.get('longitude'), i.get('densite_cat'), 
                    i.get('alti_med'), i.get('RR_med'), i.get('NBJRR1_med'), i.get('NBJRR5_med'),
                    i.get('NBJRR10_med'), i.get('Tmin_med'), i.get('Tmax_med'), i.get('Tens_vap_med'), 
                    i.get('Force_vent_med'), i.get('Insolation_med'), i.get('Rayonnement_med')
                ))
        
        db.commit()
        print("--- SUCCÈS ---")
        curs.execute("SELECT COUNT(*) FROM Données_geo")
        print(f"Nombre de lignes insérées : {curs.fetchone()[0]}")

    except Exception as e:
        print(f"Erreur lors de la lecture : {e}")
else:
    print("ERREUR : Impossible de trouver le fichier CSV dans aucun dossier !")
    print(f"Dossier actuel de travail : {os.getcwd()}")

curs.close()
db.close()