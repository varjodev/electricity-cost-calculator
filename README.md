# Electricity cost calculator / Pörssihintalaskuri
Based on data from: https://porssisahko.net/tilastot
Can be used to calculate pörssisähkö costs for one year by specifying the year between 2021-2024, yearly consumption in kwh and the daily charging interval in hours.

Dependencies: pandas, pyopenxl

--- 

Perustuu https://porssisahko.net/tilastot dataan.
Laskurilla voi laskea pörssisähkön vuosittaisia hintoja määrittelemällä tarkasteluvuoden, vuotisen kokonaiskulutuksen ja päivittäisen latausvälin.

## Käyttö
Lataa tilastot https://porssisahko.net/tilastot ja muunna ne csv:ksi excel2csv.py avulla.

### Komentoriviltä
Aktivoi kondaympäristö, jossa on pandas

python suorita.py

### Skriptinä
Voit myös määritellä useampia testiskenaarioita kerralla main.py kaltaiseen skriptiin.

