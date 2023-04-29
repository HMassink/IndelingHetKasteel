# IndelingHetKasteel

Under construction.  Dit is ook mijn file met notities. gebruik ik ook voor communicatie met ChatGPT4 :-)
 
Algemene beschrijving
De schaakcompetitie van Schaakvereniging Het Kasteel bestaat uit 3 periodes van elk 9 rondes. Daarbij zitten de spelers in 3 categorieen A, B of C. Tevens wordt er een totaalstand bijgehouden. Aan het eind van het jaar wordt er per categorie een finalegroep van 4 samengesteld, bestaande uit de winnaars van iedere periode en de speler die over het gehele jaar het beste gescoord heeft. Op deze wijze is er per categorie een kampioen. 
Indelen gebeurt op basis van het zwitsers systeem. Bij gelijk eindigen zijn de Sonneborn Berger punten van belang


Doel is om op eenvoudige wijze de competitie indelingen op de clubavonden te maken en de resultaten te publiceren.
Indeling wordt op de avond zelf gedaan. Alle namen van de leden komen op het scherm, per speler kan ingegeven worden : aanwezig, afwezig, vrij , 0 punt, 0,5 punt, 1 punt.  Vervolgens gaat het indelen automatisch. Nadat de resultaten zijn ingevoerd, wordt de stand, de jaarstand, en de rating automatisch gegenereeerd. 
Het programma genereert html-files die op de website gepubliceerd kunnen worden.


In eerste instantie gaat het om het opzetten van de grafische schil. Het maken van de indeling en genereren stand komt later. 

Software is python3.11.  

MAPPENSTRUCTUUR:
Hoofdmap IndelingHetKasteel    
    hoofprogramm :  IndelingHetKasteel.py
submappen :
- py_lijsten :
     Per lijst een py_file met daarin de definitie van de lijst en de functies om de lijst in te lezen uit de txt_file. 
     En de functies om de lijst weg te schrijven naar naar txt_file en eventueel html_file
- py_vensters :
     Per venster een py_file met daarin de definitie van het venster en de knoppen en invoervelden
     De functies die onder de knoppen zitten worden in een afzonderlijke py_file beschreven, bv hoofdvenster_functies
- py_berekeningen :
     Hier komen de py_files voor het berekeningen van indeling, standen enz. later uit te zoeken
- py_tijdelijk :
     Tijdelijk test_functies en probeersels die later verwijderd kunnen worden     
- txt_databases :
     Dit zijn de txt versie van de lijsten. Als opslag van de gegevens uit de lijsten worden txt files gebruikt. Iedere lijst heeft een eigen txt file
- txt_werkfiles :
     Tijdelijke opslagfile van lijsten. Mogelijk zijn deze niet nodig.
- txt_communicatie :
     Txt files met uitslagen rondes, stand, kruistabellen, rating, jaarstand. Deze files kunnen eventueel geprint worden.
- html_communicatie :
     Html files met uitslagen rondes, stand, kruistabellen, rating, jaarstand. Deze html bestanden worden gebruikt voor publicatie op de website.

De databases (lijsten) worden opgeslagen als txt files

VENSTERS :
- hoofd_venster :
    Geeft aan om welke periode en ronde het gaat.
    Bevat vooral knoppen om andere vensters te activeren
- aanwezige_spelers_venster :
    Per speler aangeven wat de status voor de betreffende speelavond is
- indeling_venster :
    De indeling voor de betreffende speelavond. In dit venster kan ook per partij de uitslag aangegeven worden

LIJSTEN :
- spelers :
    Lijst voor spelers die gaan meedoen aan het begin van het toernooi, inclusief start elo
- informatie :
    Lijst met de informatie over het toernooi inclusief de actuele periode en rondes
- spelers_aanwezig :
    Lijst voor spelers die aanwezig zijn op de clubavond
- spelers_totaal_jaar :
    Lijst met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over alle periodes, is ook basis voor rating en jaarlijst
- spelers_totaal_periode1 :
    Lijst met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 1
- spelers_totaal_periode2 :
    Lijst met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 2
- spelers_totaal_periode3 :
    Lijst met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 3
- indeling :
    Lijst met de indeling van de actuele ronde
    N.B.  De uitslagen van de afzonderlijke rondes worden opgeslagen in afzonderlijke txt en html files 



