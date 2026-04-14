import csv
import sqlite3
db = sqlite3.connect("BDProjetStat.db")
curs = db.cursor()
curs.execute (""" drop table if exists Données_geo """)
curs.execute (""" create table if not exists Données_geo (code_insee_com text PRIMARY KEY,
                                                                nom_com text ,  
                                                                reg_code  integer ,
                                                                reg_nom text,
                                                                dep_code integer  ,
                                                                dep_nom text ,
                                                                population integer ,
                                                                superficie real ,
                                                                densite real ,
                                                                latitude real ,
                                                                longitude real ,
                                                                densite_cat text ,
                                                                altitude_med real ,
                                                                RR_med real ,
                                                                NBJRR1_med real ,
                                                                NBJRR5_med real ,
                                                                NBJRR10_med real ,
                                                                Tmin_med real ,             
                                                                Tmax_med real ,
                                                                Tens_vap_med real ,     
                                                                Force_vent_med real ,                       
                                                                Insolation_med real,           
                                                                Rayonnement_med real)""")

table=[]
with open('Données_geo_clim/donnees_geo_climatiques - donnees_geo_climatiques.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        table.append(row) 
    print(table)
for i in table:
    print(i['code_insee_com'] ,i['nom_com'],i['reg_code'],i['reg_nom'],i['dep_code'],
          i['dep_nom'],i['population'],i['superficie_km2'],i['densite'],i['latitude'],
          i['longitude'],i['densite_cat'],i['alti_med'],i['RR_med'],i['NBJRR1_med'],
          i['NBJRR5_med'],i['NBJRR10_med'],i['Tmin_med'],i['Tmax_med'],i['Tens_vap_med'],
          i['Force_vent_med'],i['Insolation_med'],i['Rayonnement_med'])
    curs.execute("""
         INSERT INTO Données_geo (
                  code_insee_com, nom_com, reg_code, reg_nom, dep_code, dep_nom, population,
                  superficie, densite, latitude, longitude, densite_cat, altitude_med, RR_med, 
                  NBJRR1_med, NBJRR5_med, NBJRR10_med, Tmin_med, Tmax_med, Tens_vap_med, Force_vent_med, 
                  Insolation_med, Rayonnement_med)

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
             ,(i['code_insee_com'], i['nom_com'], i['reg_code'], i['reg_nom'], 
               i['dep_code'], i['dep_nom'], i['population'], i['superficie_km2'], 
               i['densite'], i['latitude'], i['longitude'], i['densite_cat'], 
               i['alti_med'], i['RR_med'], i['NBJRR1_med'], i['NBJRR5_med'],
               i['NBJRR10_med'], i['Tmin_med'], i['Tmax_med'], i['Tens_vap_med'], 
               i['Force_vent_med'], i['Insolation_med'],i['Rayonnement_med']))
db.commit() 

curs.execute("select  * from Données_geo ")
x=curs.fetchone()
while x!=None:
    print(x)
    x=curs.fetchone()

curs.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = curs.fetchall()
print("Tables dans la base de données :", tables) 





curs.close()
db.close()     

