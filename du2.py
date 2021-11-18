#Bělá, Častolovice
import csv

def pocet_radku(nazev_souboru):
    sum = 0
    with open(nazev_souboru) as f:
        reader = csv.reader(f)
        for row in reader:
            sum += 1
    return sum

print(pocet_radku("data.csv"))

with open("data.csv", encoding="utf-8") as csvinfile,\
    open("vystup_7dni.csv", "w", newline="", encoding="utf-8") as csvoutfile:
    reader = csv.reader(csvinfile, delimiter = ",")
    writer = csv.writer(csvoutfile)

    opakovani = pocet_radku("data.csv")//7 + 1
    
    a=0
    b=7
    sum = 0
    for row in list(reader)[a:b]:
        try:
            sum += float(row[5])
        except ValueError:
            pass
    prumer = sum/7
    print(f"{prumer:.4f}")
    writer.writerow([row[0], row[1], row[2], row[3], row[4], f"  {prumer:.4f}"])
    a += 7
    b += 7



