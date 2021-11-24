import csv

#otevření souboru se vstupními daty a definice výstupních souborů
with open("vstup.csv", encoding="utf-8") as csvinfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_tyden,\
    open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer_tyden = csv.writer(csvoutfile_tyden)
    writer_rok = csv.writer(csvoutfile_rok)

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




