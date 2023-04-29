# IndelingHetKasteel

Under construction.  Dit is ook mijn file met notities. gebruik ik ook voor communicatie met ChatGPT4 :-)
 
Doel is om op eenvoudige wijze de competitie indelingen op de clubavonden te maken en de resultaten te publiceren.
Indeling wordt op de avond zelf gedaan. Alle namen van de leden komen op het scherm, per speler kan ingegeven worden : aanwezig, afwezig, vrij , 0 punt, 0,5 punt, 1 punt.  Vervolgens gaat jhet indelen automatisch. Nadat de resultaten zijn ingevoerd, wordt de stand, de jaarstand, en de rating automatisch gegenereeerd. 
Het programma genereert html-files die op de website gepubliceerd kunnen worden.

In eerste instantie gaat het om het opzetten van de grafische schil. Het maken van de indeling en genereren stand komt later. 

Software is python3.11.  

Mappen struktuur project

Hoofdmap IndelingHetKasteel    
    hoofprogramm :  IndelingHetKasteel.py
submappen :
- py_lijsten
     Per lijst een py_file met daarin de definitie van de lijst en de functies om de lijst in te lezen uit de txt_file. 
     En de functies om de lijst weg te schrijven naar naar txt_file en eventueel html_file
- py_vensters
     Per venster een py_file met daarin de definitie van het venster en de knoppen en invoervelden
     De functies die onder de knoppen zitten worden in een afzonderlijke py_file beschreven, bv hoofdvenster_functies
- py_berekeningen
     Hier komen de py_files voor het berekeningen van indeling, standen enz. later uit te zoeken
- py_tijdelijk
     Tijdelijk test_functies en probeersels die later verwijderd kunnen worden     
- txt_databases
     Dit zijn de txt versie van de lijsten. Als opslag van de gegevens uit de lijsten worden txt files gebruikt. Iedere lijst heeft een eigen txt file
- txt_werkfiles
     Tijdelijke opslagfile van lijsten. Mogelijk zijn deze niet nodig.
- txt_communicatie
     Txt files met uitslagen rondes, stand, kruistabellen, rating, jaarstand. Mogelijk zijn deze files niet nodig.
- html_communicatie
     Html files met uitslagen rondes, stand, kruistabellen, rating, jaarstand. Deze html bestanden worden gebruikt voor publicatie op de website.

De databases (lijsten) worden opgeslagen als txt files

Mogelijke lijst van vensters
- Hoofdvenster
