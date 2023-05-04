# IndelingHetKasteel

Under construction.  Dit is ook mijn file met notities. gebruik ik ook voor communicatie met ChatGPT4 :-)

Update 01-05-2023 : Ipv van textfiles ga ik SQlite gebruiken om de data op te slaan. Ik ga notebook gebruiken om alle vensters in één venster via tabbladen zichtbaar te maken
 
Algemene beschrijving
De schaakcompetitie van Schaakvereniging Het Kasteel bestaat uit 3 periodes van elk 9 rondes. Daarbij zitten de spelers in 3 categorieen A, B of C. Tevens wordt er een totaalstand bijgehouden. Aan het eind van het jaar wordt er per categorie een finalegroep van 4 samengesteld, bestaande uit de winnaars van iedere periode en de speler die over het gehele jaar het beste gescoord heeft. Op deze wijze is er per categorie een kampioen. 
Indelen gebeurt op basis van het zwitsers systeem. Bij gelijk eindigen zijn de Sonneborn Berger punten van belang


Doel is om op eenvoudige wijze de competitie indelingen op de clubavonden te maken en de resultaten te publiceren.
Indeling wordt op de avond zelf gedaan. Alle namen van de leden komen op het scherm, per speler kan ingegeven worden : aanwezig, afwezig, vrij , 0 punt, 0,5 punt, 1 punt.  Vervolgens gaat het indelen automatisch. Nadat de resultaten zijn ingevoerd, wordt de stand, de jaarstand, en de rating automatisch gegenereeerd. 
Het programma genereert html-files die op de website gepubliceerd kunnen worden.


In eerste instantie gaat het om het opzetten van de grafische schil. Het maken van de indeling en genereren stand komt later. 

Software is python3.11.  
Voor het bewerken van de SQLite database gebruik ik : https://sqlitebrowser.org/

MAPPENSTRUCTUUR:
Hoofdmap IndelingHetKasteel    
    hoofprogramma :  IndelingHetKasteel.py
           
submappen :
- py_databse :
     IndelingHetKasteel.sqlite. Plus funktie om toegang te krijgen tot tabellen in de database
- py_vensters :
     Met het gebuik van notebook zal dit mogelijk anders worden ingevuld
     Per venster een py_file met daarin de definitie van het venster en de knoppen en invoervelden
     De functies die onder de knoppen zitten worden in een afzonderlijke py_file beschreven, bv hoofdvenster_functies
- py_berekeningen :
     Hier komen de py_files voor het berekeningen van indeling, standen enz. later uit te zoeken
- py_tijdelijk :
     Tijdelijk test_functies en probeersels die later verwijderd kunnen worden     
- txt_werkfiles :
     Tijdelijke opslagfile van lijsten, voor het uitvoeren van berekeningen enz. Mogelijk niet nodig
- html_communicatie :
     Html files met uitslagen rondes, stand, kruistabellen, rating, jaarstand. Deze html bestanden worden gebruikt voor publicatie op de website.

VENSTERS (Worden tab in notebook):
- hoofd_venster :
    Geeft aan om welke periode en ronde het gaat.
    Bevat vooral knoppen om andere vensters te activeren
- aanwezige_spelers_venster :
    Per speler aangeven wat de status voor de betreffende speelavond is
- indeling_venster :
    De indeling voor de betreffende speelavond. In dit venster kan ook per partij de uitslag aangegeven worden

TABELLEN IN DATABASE :
- spelers :
    Tabel voor spelers die gaan meedoen aan het begin van het toernooi, inclusief start elo
- informatie :
    Tabel met de informatie over het toernooi inclusief de actuele periode en rondes
- spelers_aanwezig :
    Tabel voor spelers die aanwezig zijn op de clubavond
- spelers_vrij :
    Tabel voor spelers die vrij geloot zijn gedurenden het seizoen
- spelers_totaal_jaar :
    Tabel met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over alle periodes, is ook basis voor rating en jaarlijst
- spelers_totaal_periode1 :
    Tabel met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 1
- spelers_totaal_periode2 :
    Tabel met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 2
- spelers_totaal_periode3 :
    Tabel met het totaal overzicht van alle spelers tegenstanders, punten enz gaat over periode 3
- indeling_P.._R... :
    Tabel met de indeling, resultaten en datum per ronde      
- spelers_verdwenen
    Tabel met de spelers die geen lid meer zijn. Hun namen moeten niet meer zichtbaar zijn bij de resultaten. 
    Ze kunnen niet verwijderd worden, omdat ze van invloed zijn o pde resultaten van anderen.


REGELS ZWITSERS
Uit het fide handboek : https://handbook.fide.com/chapter/C0401

Vertaald:
C.04.1 Basisregels voor Zwitserse Systemen
De volgende regels zijn geldig voor elk Zwitsers systeem, tenzij uitdrukkelijk anders vermeld.
a Het aantal te spelen ronden wordt vooraf vastgesteld.

b Twee spelers mogen niet meer dan één keer tegen elkaar spelen.

c Als het aantal te koppelen spelers oneven is, wordt één speler niet gekoppeld. Deze speler krijgt een door het koppelingssysteem toegewezen bye: geen tegenstander, geen kleur en evenveel punten als er worden beloond voor een overwinning, tenzij de regels van het toernooi anders bepalen.

d Een speler die al een door het koppelingssysteem toegewezen bye heeft gekregen, of al een (reglementaire) overwinning heeft behaald doordat een tegenstander niet op tijd verscheen, mag geen bye krijgen die door het koppelingssysteem is toegewezen.

e In het algemeen worden spelers gekoppeld aan anderen met dezelfde score.

f Voor elke speler mag het verschil tussen het aantal zwarte en het aantal witte partijen niet groter zijn dan 2 of kleiner dan -2.Elk systeem kan uitzonderingen op deze regel hebben in de laatste ronde van een toernooi.

g Geen enkele speler mag drie keer achter elkaar dezelfde kleur krijgen. Elk systeem kan uitzonderingen op deze regel hebben in de laatste ronde van een toernooi.

h1 In het algemeen krijgt een speler de kleur waarmee hij minder partijen heeft gespeeld.

h2 Als de kleuren al in evenwicht zijn, krijgt de speler over het algemeen de kleur die afwisselt met de laatste waarmee hij heeft gespeeld.

i De koppelingsregels moeten zo transparant zijn dat de persoon die verantwoordelijk is voor de koppeling ze kan uitleggen.

