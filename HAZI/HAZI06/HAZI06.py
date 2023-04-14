"""
1. Értelmezd az adatokat!!!

2. Írj egy osztályt a következő feladatokra:  
     - Neve legyen NJCleaner és mentsd el a NJCleaner.py-ba. Ebben a fájlban csak ez az osztály legyen.
     - Konsturktorban kapja meg a csv elérési útvonalát és olvassa be pandas segítségével és mentsük el a data (self.data) osztályszintű változóba 
     - Írj egy függvényt ami sorbarendezi a csv-t 'scheduled_time' szerint növekvőbe és visszatér a sorbarendezett df-el, a függvény neve legyen 'order_by_scheduled_time' és térjen vissza a df-el  
     - Dobjuk el a from és a to oszlopokat, illetve a nan-okat és adjuk vissza a df-et. A függvény neve legyen 'drop_columns_and_nan' és térjen vissza a df-el  
     - A date-et alakítsd át napokra, pl.: 2018-03-01 --> Thursday, ennek az oszlopnak legyen neve a 'day'. Ezután dobd el a 'date' oszlopot és térjen vissza a df-el. A függvény neve legyen 'convert_date_to_day' és térjen vissza a df-el   
     - Hozz létre egy új oszlopot 'part_of_the_day' névvel. A 'scheduled_time' oszlopból számítsd ki az alábbi értékeit. A 'scheduled_time'-ot dobd el. A függvény neve legyen 'convert_scheduled_time_to_part_of_the_day' és térjen vissza a df-el  
         4:00-7:59 -- early_morning  
         8:00-11:59 -- morning  
         12:00-15:59 -- afternoon  
         16:00-19:59 -- evening  
         20:00-23:59 -- night  
         0:00-3:59 -- late_night  
    - A késéeket jelöld az alábbiak szerint. Az új osztlop neve legyen 'delay'. A függvény neve legyen pedig 'convert_delay' és térjen vissza a df-el
         0 <= x 5  --> 0  
         5 <= x    --> 1  
    - Dobd el a felesleges oszlopokat 'train_id' 'scheduled_time' 'actual_time' 'delay_minutes'. A függvény neve legyen 'drop_unnecessary_columns' és térjen vissza a df-el
    - Írj egy olyan metódust, ami elmenti a dataframe első 60 000 sorát. A függvénynek egy string paramétere legyen, az pedig az, hogy hova mentse el a csv-t (pl.: 'data/NJ.csv'). A függvény neve legyen 'save_first_60k'. 
    - Írj egy függvényt ami a fenti függvényeket összefogja és megvalósítja (sorbarendezés --> drop_columns_and_nan --> ... --> save_first_60k), a függvény neve legyen 'prep_df'. Egy paramnétert várjon, az pedig a csv-nek a mentési útvonala legyen. Ha default value-ja legyen 'data/NJ.csv'

3.  A feladatot a HAZI06.py-ban old meg.
    Az órán megírt DecisionTreeClassifier-t fit-eld fel az első feladatban lementett csv-re. 
    A feladat célja az, hogy határozzuk meg azt, hogy a vonatok késnek-e vagy sem. 0p <= x < 5p --> nem késik, ha 5 < x --> késik.
    Az adatoknak a 20% legyen test és a splitelés random_state-je pedig 41 (mint órán)
    A testset-en 80% kell elérni. Ha megvan a minimum százalék, akkor azzal paraméterezd fel a decisiontree-t és azt kell leadni.

    A leadásnál csak egy fit kell, ezt azzal a paraméterre paraméterezd fel, amivel a legjobb accuracy-t elérted.

    A helyes paraméter megtalálásához használhatsz grid_search-öt.
    https://www.w3schools.com/python/python_ml_grid_search.asp 

4.  A tanításodat foglald össze 4-5 mondatban a HAZI06.py-ban a fájl legalján kommentben. Írd le a nehézségeket, mivel próbálkoztál, mi vált be és mi nem. Ezen kívül írd le 10 fitelésed eredményét is, hogy milyen paraméterekkel probáltad és milyen accuracy-t értél el. 
Ha ezt feladatot hiányzik, akkor nem fogadjuk el a házit!

##################################################################
##                                                              ##
## A feladatok közül csak a NJCleaner javítom unit test-el      ##
## A decision tree-t majd manuálisan fogom lefuttatni           ##
## NJCleaner - 10p, Tanítás - acc-nál 10%-ként egy pont         ##
## Ha a 4. feladat hiányzik, akkor nem tudjuk elfogadni a házit ##
##                                                              ##
##################################################################
"""

from src.DecisionTreeClassifier import DecisionTreeClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('HAZI/HAZI06/NJ_60k.csv', skiprows = 1, header = None)

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values.reshape(-1, 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 41)

classifier = DecisionTreeClassifier(100, 11)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)
acc = accuracy_score(Y_test, Y_pred)

print(f"Min_split = 100 \t Max_depth = 11 \t Accuracy = {acc}")



# Bruteforce módszerrel kezdtem neki a tanításnak 10-es min_split-tel. Viszonylag erős gépen is, a max_depth növelésével nagyban nőtt a kiértékelés időtartama. For ciklusokkal több variáción végigmentem.
# Megfigyeltem, hogy -esetekben- nagyban eltérő Min_split értékek mellett (10, 11, 20, 30) azonos max_depth-nél 0.2%-on belüli maximum eltérés tapasztalható, illetve max_depth = 9-nél előző min_split értékekkel error-t kapok.
# Max_depth = 8 esetén maximum 79,55%-os pontosságot kaptam, illetve ennek növelésével a pontosság javulása is jól megfigyelhető, így arra jutottam, hogy el kell érnem, hogy ne kapjak errort a magasabb értékekre.
# Szignifikáns!! min_split növelése esetén (min_split = 100) már nem kaptam errort max_depth >= 9 értékekre, így rájöttem, hogy a 2 érték exponenciális összefüggésben van.
# Érdekesség, hogy max_depth = 11 tűnik a holtpontnak magas min_split-tel, eddig nő, ennél nagyobb értékkel pedig csökken a pontosság.
# Min_split = 100, max_depth = 10 kombinációval sikerült először 80% fölötti pontosságot elérni.
# Min_split = 300 értéknél már 80%-ot sem kaptam, így 80.358% pontosság lett a nyerő, Min_split = 100  Max_depth = 11 értékpárral.

# Min_split = 10   Max_depth = 1   Accuracy = 0.7773333333333333
# Min_split = 10   Max_depth = 3   Accuracy = 0.7839166666666667
# Min_split = 10   Max_depth = 4   Accuracy = 0.7849166666666667
# Min_split = 10   Max_depth = 5   Accuracy = 0.7885833333333333
# Min_split = 10   Max_depth = 6   Accuracy = 0.7885
# Min_split = 10   Max_depth = 7   Accuracy = 0.7935
# Min_split = 10   Max_depth = 8   Accuracy = 0.7955833333333333
# Min_split = 10   Max_depth = 9   Accuracy = ERROR!!!

# Min_split = 11   Max_depth = 1   Accuracy = 0.7773333333333333
# Min_split = 11   Max_depth = 2   Accuracy = 0.7823333333333333
# Min_split = 11   Max_depth = 3   Accuracy = 0.7839166666666667
# Min_split = 11   Max_depth = 4   Accuracy = 0.7849166666666667
# Min_split = 11   Max_depth = 5   Accuracy = 0.7885833333333333
# Min_split = 11   Max_depth = 6   Accuracy = 0.7885
# Min_split = 11   Max_depth = 7   Accuracy = 0.7935
# Min_split = 11   Max_depth = 8   Accuracy = 0.7955833333333333
# Min_split = 11   Max_depth = 9   Accuracy = ERROR!!!

# Min_split = 20   Max_depth = 1   Accuracy = 0.7773333333333333
# Min_split = 20   Max_depth = 2   Accuracy = 0.7823333333333333
# Min_split = 20   Max_depth = 3   Accuracy = 0.7839166666666667
# Min_split = 20   Max_depth = 4   Accuracy = 0.7849166666666667
# Min_split = 20   Max_depth = 5   Accuracy = 0.7885833333333333
# Min_split = 20   Max_depth = 6   Accuracy = 0.7885
# Min_split = 20   Max_depth = 7   Accuracy = 0.7936666666666666
# Min_split = 20   Max_depth = 8   Accuracy = 0.7955

# Min_split = 30   Max_depth = 1   Accuracy = 0.7773333333333333
# Min_split = 30   Max_depth = 2   Accuracy = 0.7823333333333333
# Min_split = 30   Max_depth = 3   Accuracy = 0.7839166666666667
# Min_split = 30   Max_depth = 4   Accuracy = 0.7849166666666667
# Min_split = 30   Max_depth = 5   Accuracy = 0.7885833333333333
# Min_split = 30   Max_depth = 6   Accuracy = 0.7885
# Min_split = 30   Max_depth = 7   Accuracy = 0.7936666666666666
# Min_split = 30   Max_depth = 8   Accuracy = 0.7955

# Min_split = 100  Max_depth = 7   Accuracy = 0.7940833333333334
# Min_split = 100  Max_depth = 8   Accuracy = 0.7969166666666667
# Min_split = 100  Max_depth = 9   Accuracy = 0.7986666666666666
# Min_split = 100  Max_depth = 10  Accuracy = 0.80225
# Min_split = 100  Max_depth = 11  Accuracy = 0.8035833333333333
# Min_split = 100  Max_depth = 12  Accuracy = 0.8025
# Min_split = 100  Max_depth = 13  Accuracy = 0.8009166666666667
# Min_split = 100  Max_depth = 14  Accuracy = 0.8005

# Min_split = 110  Max_depth = 7   Accuracy = 0.7935833333333333
# Min_split = 110  Max_depth = 8   Accuracy = 0.7964166666666667
# Min_split = 110  Max_depth = 9   Accuracy = 0.79825
# Min_split = 110  Max_depth = 10  Accuracy = 0.8014166666666667
# Min_split = 110  Max_depth = 11  Accuracy = 0.80275
# Min_split = 110  Max_depth = 12  Accuracy = 0.8016666666666666

# Min_split = 300  Max_depth = 10  Accuracy = 0.7985
# Min_split = 300  Max_depth = 11  Accuracy = 0.7995833333333333
# Min_split = 300  Max_depth = 12  Accuracy = 0.7996666666666666
# Min_split = 300  Max_depth = 13  Accuracy = 0.798