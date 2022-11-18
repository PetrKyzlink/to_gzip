# to_gzip

Tento skript slouží ke kompresi dat v určené složce. Komprimuje jednotlivé každý soubor zvlášť a po kompresi odstraní původní soubor určený ke kompresi. Skript prohlédne cyklem složku a v případě, že nenalezne soubor, který by mohl být komprimován, ponechá vše, tak jak bylo před spuštěním skriptu. Z komprese jsou vynechány za použití podmínky if soubory s příponou „ .gz “ a „ .py “.  

Skript je nutné nahrát do složky, která je nadřazená složce „var“. V případě nahrání skriptu do složky log, je pro jeho správné fungování potřeba nahradit ve skriptu cestu os.path.join("var", "log", "") za  náhradu v komentáři ("..", "log", "").
(Chcete-li použít skript v jiné složce, je zapotřebí přepsat os.path.join zcela a to s přesnými názvy složek.)

Skript pracuje v následujících krocích:
Načtení obsahu složky, načtení jednotlivých souborů cyklem s následnou kontrolou splnění podmínky pro kompresi, otevření souboru pro kompresi, komprese souboru a smazání souboru, který byl určen pro kompresi.

------------------------------------------------------------------------------------------------------------------------------------------------------- -->
