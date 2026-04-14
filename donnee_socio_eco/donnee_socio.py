import csv
import sqlite3
import os


db = sqlite3.connect("BDProjetStat.db")
curs = db.cursor()


curs.execute("DROP TABLE IF EXISTS Socio_Eco")
curs.execute("""
    CREATE TABLE Socio_Eco (
        code_insee_com TEXT PRIMARY KEY,
        nom_com TEXT,
        MED21 REAL,
        population REAL
    )
""")

nom_fichier = 'donnee_socio_eco/donnees_socio_economiques.csv'

try:
    with open(nom_fichier, mode='r', encoding='utf-8-sig') as file:
        
        reader = csv.DictReader(file, delimiter=',') 
        
        for row in reader:
            
            code = row.get('code_insee_com')
            nom = row.get('nom_com')
            
            revenu = row.get('niveau_vie_median_2021') 
            pop = row.get('population_municipale_2023')

            curs.execute("""
                INSERT INTO Socio_Eco (code_insee_com, nom_com, MED21, population)
                VALUES (?, ?, ?, ?)
            """, (code, nom, revenu, pop))
    
    db.commit()
    print("--- SUCCÈS : Données Socio-Eco importées ---")

    
    curs.execute("SELECT nom_com, MED21 FROM Socio_Eco WHERE MED21 IS NOT NULL LIMIT 1")
    res = curs.fetchone()
    print(f"Test de donnée : Ville = {res[0]}, Revenu = {res[1]} €")

except Exception as e:
    print(f"Erreur : {e}")
finally:
    db.close()