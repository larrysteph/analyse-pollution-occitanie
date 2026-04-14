import csv
import sqlite3


db = sqlite3.connect("BDProjetStat.db")
curs = db.cursor()


curs.execute("DROP TABLE IF EXISTS Pollution")
curs.execute("""
    CREATE TABLE IF NOT EXISTS Pollution (
        id_mesure INTEGER PRIMARY KEY AUTOINCREMENT,
        nom_dept TEXT,
        nom_com TEXT,
        code_insee_com TEXT,
        nom_station TEXT,
        code_station TEXT,
        typologie TEXT,
        influence TEXT,
        nom_poll TEXT,
        valeur_poll REAL,
        jour INTEGER,
        mois INTEGER,
        annee INTEGER
    )
""")


nom_fichier = 'donne_qualite_air/mesures_occitanie_journaliere_pollution.csv'

try:
    with open(nom_fichier, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',') 
        for row in reader:
            curs.execute("""
                INSERT INTO Pollution (
                    nom_dept, nom_com, code_insee_com, nom_station, 
                    code_station, typologie, influence, nom_poll, 
                    valeur_poll, jour, mois, annee
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row.get('nom_dept'), row.get('nom_com'), row.get('code_insee_com'),
                row.get('nom_station'), row.get('code_station'), row.get('typologie'),
                row.get('influence'), row.get('nom_poll'), row.get('valeur_poll'),
                row.get('jour'), row.get('mois'), row.get('annee')
            ))
    
    db.commit()
    print(f"Succès : Les données de pollution ont été intégrées dans BDProjetStat.db.")

except Exception as e:
    print(f"Erreur lors de l'insertion : {e}")

finally:
    curs.close()
    db.close()