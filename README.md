
# MiukuM@uku - Ohjelmistotekniikan harjoitustyö
Sovelluksen avulla käyttäjä voi luoda virtuaalisen kissan lemmikikseen ja pitää siitä huolta. Käyttäjä pääsee kokemaan minkälaista vastuuta lemmikin omistaminen vaati. Jos käyttäjä ei vastaa kissan tarpeisiin, kissasta tulee tyytymätön omistajaansa ja karkaa.

Sovellus on toteutettu Helsingin yliopiston kurssilla Ohjelmistotekniikka. 
## Python versio
Sovellusta on testattu Pythonin `3.8` versiolla.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Arkkitehtuuri](./dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./dokumentaatio/kayttoohje.md)

### Asennus

- [Loppupalautus](https://github.com/leinson/ohte-harjoitustyo/releases/tag/loppupalautus)

- Riippuvuudet asennetaan komennolla: `poetry install`
- Sovelluksen käynnistäminen komennolla: `poetry run invoke start`

### Komentorivitoiminnot
- Ohjelma suoritetaan komennolla: `poetry run invoke start`
- Testit tehdään komennolla: `poetry run invoke test`
- Testikattavuuden saa komennolla: `poetry run invoke coverage-report`
- Pylint tarkistus komennolla: `poetry run invoke lint`
