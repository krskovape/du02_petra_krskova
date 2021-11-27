import csv
from datetime import date, timedelta

try:
    #otevření souboru se vstupními daty a definice výstupních souborů
    with open("vstup.csv", encoding="utf-8") as csvinfile,\
        open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile_tyden,\
        open("vystup_rok.csv", "w", newline="", encoding="utf-8") as csvoutfile_rok:
        reader = csv.reader(csvinfile, delimiter = ",")
        writer_tyden = csv.writer(csvoutfile_tyden)
        writer_rok = csv.writer(csvoutfile_rok)

        #inicializace proměnných
        pocet_radku = 0   
        sum_prutok_tyden = 0
        zbyle_dny_tyden = 0
        sum_prutok_rok = 0
        zbyle_dny_rok = 0
        rozdil_dny = timedelta(days=1)

        for row in reader:
            aktualni_rok = int(row[2])

            #přiřazení řádku do nové proměnné, pokud se jedná o první den týdne
            if pocet_radku % 7 == 0:
                prvni_den_tyden = row

            #přiřazení roku z prvního řádku do proměnné představující rok, za který se počítá průměr
            if pocet_radku == 0:
                rok_prutoku = aktualni_rok
                prvni_den_rok = row
                radek_max_prutok = row
                radek_min_prutok = row
                datum1 = date(int(row[2]), int(row[3]), int(row[4]))
                try:
                    max_prutok = float(radek_max_prutok[5])
                    min_prutok = float(radek_min_prutok[5])
                except ValueError:
                    print("Na prvním řádku je chybně zadaná hodnota průtoku.")
                

            #ošetření nekorektního vstupu
            try:
                sum_prutok_tyden += float(row[5])
                aktualni_prutok = float(row[5])
                sum_prutok_rok += aktualni_prutok
                zbyle_dny_tyden += 1
                zbyle_dny_rok += 1
            except ValueError:
                print(f"Na řádku {pocet_radku} je chybně zadaná hodnota průtoku a program ji přeskočí.")
                continue
            
            #chybějící dny
            datum2 = date(int(row[2]), int(row[3]), int(row[4]))
            if datum2 - datum1 == rozdil_dny:
                pass
            elif datum2 - datum1 != rozdil_dny:
                datum = datum1 + rozdil_dny
                while datum < datum2:
                    print (f"Chybí hodnota průtoku pro {datum}.")
                    datum += rozdil_dny
            datum1 = datum2

            #kontrola nulového nebo záporného průtoku
            if aktualni_prutok == 0:
                print(f"{row[4]}.{row[3]}.{row[2]} byl průtok nulový.")
            elif aktualni_prutok < 0:
                print(f"{row[4]}.{row[3]}.{row[2]} byl průtok záporný. Hodnota průtoku = {aktualni_prutok}")


            #spočítání sedmidenního průměru a jeho zápis do souboru
            if pocet_radku % 7 == 6:
                prumer_prutok_tyden = sum_prutok_tyden / zbyle_dny_tyden
                prvni_den_tyden[5] = f"   {prumer_prutok_tyden:.4f}"
                writer_tyden.writerow(prvni_den_tyden)
                sum_prutok_tyden = 0
                zbyle_dny_tyden = 0
            
            #spočítání ročního průměru a jeho zapsání do souboru
            if aktualni_rok != rok_prutoku:
                prumer_prutok_rok = (sum_prutok_rok - aktualni_prutok) / (zbyle_dny_rok - 1)
                prvni_den_rok[5] = f"   {prumer_prutok_rok:.4f}"
                writer_rok.writerow(prvni_den_rok)
                sum_prutok_rok = aktualni_prutok
                zbyle_dny_rok = 1
                rok_prutoku = aktualni_rok
                prvni_den_rok = row
            
            #kontrola maxima a minima
            if aktualni_prutok > max_prutok:
                radek_max_prutok = row
                max_prutok = aktualni_prutok
            elif aktualni_prutok < min_prutok:
                radek_min_prutok = row
                min_prutok = aktualni_prutok

            pocet_radku += 1
        
        #dopočítání sedmidenního průměru ze zbylých dnů
        if (pocet_radku - 1) % 7 != 6:
            prumer_prutok_tyden = sum_prutok_tyden / zbyle_dny_tyden
            prvni_den_tyden[5] = f"   {prumer_prutok_tyden:.4f}"
            writer_tyden.writerow(prvni_den_tyden)
        
        #dopočítání ročního průměru za poslední rok
        if aktualni_rok == rok_prutoku:
            prumer_prutok_rok = sum_prutok_rok / zbyle_dny_rok
            prvni_den_rok[5] = f"   {prumer_prutok_rok:.4f}"
            writer_rok.writerow(prvni_den_rok)

        #výpis maximálního a minimálního průtoku
        print(f"Maximální průtok byl {radek_max_prutok[4]}.{radek_max_prutok[3]}.{radek_max_prutok[2]} s hodnotou {max_prutok}.")
        print(f"Minimální průtok byl {radek_min_prutok[4]}.{radek_min_prutok[3]}.{radek_min_prutok[2]} s hodnotou {min_prutok}.")

except FileNotFoundError:
    print("Zadaný soubor se vstupními daty nelze otevřít. Soubor neexistuje, nebo je chybně zadaná cesta k jeho umístění.")
except PermissionError:
    print("Program nemá dostatečná oprávnění ke vstupnímu nebo výstupnímu programu.")