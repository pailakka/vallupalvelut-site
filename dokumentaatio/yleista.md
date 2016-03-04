# VALLU-tietopalvelut
## Tietoa käyttäjille
Palvelun reitti- ja aikataulutiedot sekä liikennettä koskevat hallinnolliset tiedot päivitetään joka aamu noin klo 07:00.
### Reittien haku
Palvelu VALLU-järjestelmään tallennettujen reittien hakemiselle erilaisilla hakukriteereillä. Tällä hetkellä reittejä on mahdollista hakea seuraavilla kriteereillä:
- Liikenteenharjoittajan nimi tai sen osa
- Liikenteenharjoittajanumero
- Sopimustunnus tai sen osa
    - Esimerkiksi haku `REITTI-` tuottaa tulokseksi kaikki reittiliikenneluvat
- Reitin nimi tai sen osa
- Reitin pysyvä tunniste
- Vuoron pysyvä ja vaihtua tunniste
    - Tuloksena reitti, johon kyseinen vuoro kuuluu

### Pysäkin kautta kulkevat liiknenne

Palvelu tietyn pysäkin kautta kulkevien reittien hakemiseen. Palvelu valtakunnallisesti vain ne pysäkit, joiden kautta on VALLU-järjestelmään tallennettua liikennettä. Haku sisäsltää myös pysäkit, joita ei ole Digiroad-järjestelmässä, mutta jotka ovat käytössä VALLU-liikenteessä.

Pysäkkihaku pyrkii löytämään pysäkkinimistä mahdollisimman lähellä käyttäjän antamaa hakusanaa olevat pysäkit vaikka nimi ei hakutermejä täysin vastaisikaan. Lyhenteent `MH` ja `LAS` tulkitaan automaattisesti "auki" pysäkkejä hakiessa. Usein voi olla hyödyllistä käyttää "Lisää pysäkit läheltä"-toiminnallisuutta lähellä olevien pysäkkien lisäämiseksi hakuun, mikäli oikeasta pysäkistä ei ole täyttä varmuutta. On myös mahdollista, että lähes samassa paikassa on useita käytössä olevia pysäkkejä.

### Kahden paikan välinen liikenne
Palvelu hakee liikennettä kahden pysäkki- tai kuntajoukon välillä. Haku ei välitä liikenteen suunnasta, vaan kaikki liikenne joukkojen A ja B välillä huomioidaan riippumatta siitä kulkevatko ne joukosta A joukkoon B vai toisinpäin. 

Pysäkkihaku toimii samoin kuin yhden pysäkin kautta kulkevan liikenteen tapauksessa.

### vuoro.csv excel-muodossa
Tiedostoon tuotetaan joka aamu noin klo 07:30 vuorocsv:n versio, jossa sisältöä on muokattu paremmin Excel-yhteensopivaan muotoon muun muassa sisällön suodattamisen helpottamiseksi.

### TVV-kohtaiset paikkatietoaineistot
Kansioon tuotetaan joka aamu 07:30 lähtien ESRI Shape-muotoiset paikkatietoaineistot, jotka sisältävät kunkin TVV:n maantieteellisen alueen läpi kulkevien vuorojen linjausgeometrian sekä hallinnolliset tiedot.

## Tunnetut ongelmat / puutteet


