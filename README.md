# IndelingHetKasteel

Under construction.  Dit is ook mijn file met notities. gebruik ik ook voor communicatie met ChatGPT4 :-)
 
Doel is om op eenvoudige wijze de competitie indelingen op de clubavonden te maken en de resultaten te publiceren.
Indeling wordt op de avond zelf gedaan. Alle namen van de leden komen op het scherm, per speler kan ingegeven worden : aanwezig, afwezig, vrij , 0 punt, 0,5 punt, 1 punt.  Vervolgens gaat jhet indelen automatisch. Nadat de resultaten zijn ingevoerd, wordt de stand, de jaarstand, en de rating automatisch gegenereeerd. 
Het programma genereert html-files die op de website gepubliceerd kunnen worden.

Software is python3.11.  

Mappen struktuur project

Hoofdmap IndelingHetKasteel    
    hoofprogramm :  IndelingHetKasteel.py
submappen :
- py_lijsten
     per lijst een py file met daarin de definitie van de lijst en de functies om de lijst in te lezen uit de txt_file. 
     En de functies om de lijst weg te schrijven naar naar txt_file en eventueel html_file
- py_vensters
- py_berekeningen
- txt_databases
- txt_werkfiles
- txt_communicatie
- html_communicatie

De databases (lijsten) worden opgeslagen als txt files

Mogelijke lijst van vensters
- Hoofdvenster
