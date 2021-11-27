I. Výpočet sedmidenních a ročních průměrných průtoků
    1. otevření souboru se vstupními daty a definice výstupních souborů
    2. inicializace proměnných
    3. FOR cyklus, ve kterém probíhá výpočet průměrných průtoků
        a. přiřazení řádku do nové proměnné, pokud se jedná o první den týdne
            Pokud je zbytek po celočíselném dělení počtu řádků sedmi rovný nule, znamená to, že se jedná o řádek odpovídající prvnímu ze sedmi dní, pro který se počítá průměrný průtok a je tak přiřazen do odpovídající proměnné (prvni_den_tyden).
        b. přiřazení roku z prvního řádku do proměnné představující rok, za který se počítá průměr
            První řádek ze souboru je přiřazen do proměnné odpovídající prvnímu dni z počítaného roku (prvni_den_rok) a rok je přiřazen do proměnné (rok_prutoku), která definuje, pro jaký rok je aktuálně počítán průměrný průtok.
        c. ošetření nekorektního vstupu
            Při chybě ve vstupních datech je vypsána hláška uživateli.
        d. kontrola nulového nebo záporného průtoku
            Program porovná, zda není aktuální průtok nulový či záporný a případně vypíše hlášku do konzole.
        e. spočítání sedmidenního průměru a jeho zápis do souboru
            Pokud zbytek po celočíselném dělení počtu řádků sedmi odpovídá šesti, znamená to, že program narazil na poslední ze sedmi dnů a vypočítá jejich průměrný průtok. Ten následně zapíše do souboru a vynuluje pomocné proměnné.
        f.  spočítání ročního průměru a jeho zapsání do souboru
            Pokud se aktuální rok nerovná roku, pro který je počítán průměrný průtok, znamená to, že program narazil na první řádek dalšího roku. Průtok tohoto dne je tak odečten od sumy průtoků a je spočítán průměrný průtok za počítaný rok, který je následně vypsán do souboru. Hodnoty tohoto prvního dne, by ale chyběly ve výpočtu průměru za nový rok a proto je aktuální průtok přiřazen do proměnné počítající sumy průtoků (sum_prutok_rok) a proměnná počítající dny (zbyle_dny_rok) v roce je nastavena na 1. Aktuální řádek je také přiřazen do proměnné odpovídající prvnímu dni v roce (prvni_den_rok).
        g. Na konci každého cyklu je pak hodnota proměnné udržující počet řádků zvýšena o 1.
    4. dopočítání sedmidenního průměru ze zbylých dnů
        Pokud není počet řádků souboru beze zbytku dělitelný sedmi, je potřeba spočítat průměr za zbylé dny po skončení FOR cyklu. Proměnná udržující počet řádků je zvýšena o 1 na konci každého cyklu, takže po jeho úplném skončení je o 1 vyšší, než je skutečný počet řádků. Proto je při porovnávání od počtu řádků odečtena 1. Pokud je zbytek po jedho celočíselném dělení sedmi různý od šesti, znamená to, že na konci souboru zbylo méně než sedm řádků a nebyl pro ně spočítán průměr. Ten je tak dopočítán a zapsán do souboru.
    5. dopočítání ročního průměru za poslední rok
        Jelikož k výpočtu průměrného ročního průtoku dochází při přeskočení na další rok, není ve FOR cyklu spočítán průměr za poslední rok. Ten je tak spočítán až po jeho úplném skončení.

II. Výpis maximálního a minimálního průtoku
    Program prochází řádky vstupního souboru. První řádek souboru přiřadí do řádku s max. i min. průtokem a jeho hodnoty do odpovídajících proměnných (max_prutok a min_prutok). Aktuální průtok daného řádku je pak porovnán s maximem a minimem. Pokud je větší než max., je průtok přiřazen do max. průtoku a celý řádek do dané proměnné. Obdobně, pokud je aktuální průtok menší než minimální průtok. Na závěr je do konzole vypsán datum a hodnota maximálního a minimálního průtoku.
