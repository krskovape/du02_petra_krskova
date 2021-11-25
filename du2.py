import csv
#SEDMIDENNÍ PRŮTOKY
#otevření souboru se vstupními daty a definice výstupních souborů
with open("vstup.csv", encoding="utf-8") as csvinfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_tyden:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer_tyden = csv.writer(csvoutfile_tyden)

    #inicializace proměnných
    pocet_radku = 0   
    sum_prutok = 0
    zbyle_dny = 0

    for row in reader:
        #přiřazení řádku do nové proměnné, pokud se jedná o první den týdne
        if pocet_radku % 7 == 0:
            prvni_den_tyden = row

        #ošetření nekorektního vstupu
        try:
            sum_prutok += float(row[5])
            zbyle_dny += 1
        except ValueError:
            pass
        
        #spočítání sedmidenního průměru a jeho zápis do souboru
        if pocet_radku % 7 == 6:
            prumer_prutok = sum_prutok / 7
            prvni_den_tyden[5] = f" {prumer_prutok:.4f}"
            writer_tyden.writerow(prvni_den_tyden)
            sum_prutok = 0
            prumer_prutok = 0
            zbyle_dny = 0
        pocet_radku += 1
    
    #dopočítání průměru ze zbylých dnů
    if pocet_radku % 7 != 6:
        prumer_prutok = sum_prutok / zbyle_dny
        prvni_den_tyden[5] = f" {prumer_prutok:.4f}"
        writer_tyden.writerow(prvni_den_tyden)

#ROČNÍ PRŮTOKY
#otevření souboru se vstupními daty a definice výstupních souborů
with open("vstup.csv", encoding="utf-8") as csvinfile,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer_rok = csv.writer(csvoutfile_rok)

    #inicializace proměnných
    pocet_radku = 0   
    sum_prutok = 0
    zbyle_dny = 0
    
    for row in reader:
        aktualni_rok = int(row[2])
        #přiřazení roku z prvního řádku do proměnné představující rok, za který se počítá průměr
        if pocet_radku == 0:
            rok_prutoku = int(row[2])
            prvni_den_rok = row
        
        #ošetření nekorektního vstupu
        try:
            sum_prutok += float(row[5])
            zbyle_dny += 1
        except ValueError:
            pass

        #spočítání ročního průměru a jeho zapsání do souboru
        if aktualni_rok != rok_prutoku:
            aktualni_prutok = float(row[5])
            prumer_prutok = (sum_prutok - aktualni_prutok) / (zbyle_dny - 1)
            prvni_den_rok[5] = f" {prumer_prutok:.4f}"
            writer_rok.writerow(prvni_den_rok)
            sum_prutok = aktualni_prutok
            prumer_prutok = 0
            zbyle_dny = 1
            rok_prutoku = int(row[2])
            prvni_den_rok = row
        pocet_radku += 1

    #dopočítání průměru za poslední rok
    if aktualni_rok == rok_prutoku:
        prumer_prutok = sum_prutok / zbyle_dny
        prvni_den_rok[5] = f" {prumer_prutok:.4f}"
        writer_rok.writerow(prvni_den_rok)





