# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi luoda virtuaalisen kissan lemmikikseen ja pitää siitä huolta. Käyttäjä pääsee kokemaan minkälaista vastuuta lemmikin omistaminen vaati. Jos käyttäjä ei vastaa kissan tarpeisiin, kissasta tulee tyytymätön omistajaansa ja karkaa.


## Perusversion tarjoama toiminnallisuus

- Käyttäjän nimi luodaan
- Käyttäjä valitsee kissalle nimen

- Käyttäjä näkee:
	- kissan
	- miten nälkäinen kissa on
	- jos kissa tarvitsee leikittämistä
- Käyttäjä voi:
	- ruokkia kissaa
	- leikittää kissaa
	- poistua sovelluksesta
- Jos käyttäjä ei syötä tai leiki kissan kanssa tietyn aikaikkunan sisällä, kissa karkaa.


## Jatkokehitysideoita

Kun tekstikäyttöliittymä on saatu toimimaan päivitetään se graafiseksi käyttöliittymäksi, joka voi sisältää esimerkiksi seuraavia elementtejä riippuen miten aikaa riittää:

- Alkusivu, missä on kentät oman nimen ja kissan nimen täyttämiselle, sekä painike mistä pääsee siirtymään kissa-näkymään.
-Ohjeet-painike, missä pääsee lukemaan ohjeet sovelluksen käyttöä varten.
Kissa-näkymä:
- Kissa:
	- Kissan ilme muuttuu sen mukaan, miten täynnä tarpeet-palkit ovat.
	- Kissan keho kapeutuu kun nälkä-palkki on lähes tyhjä
	- Kissan keho suurentuu kun nälkä-palkki on täynnä ja syöttäminen jatkuu
	- Kissa sanoo asioita, esimerkiksi varoittaa ennen kun palkit ovat tyhjät, ja ilmaisee onnellisuutta kun ovat täynnä.
	
- Palkit tai prosentit, missä näkyy ruoka- ja leikki-tarpeet (esim. nälkä: 50/100).
- Taustakuva
- Poistu-painike


Jos aikaa riittää täydennetään ohjelmaa esim. seuraavin toiminnallisuuksin:
- lisätään muita tarpeita kissalle, kuten: nukkuminen, käynti hiekkalaatikolla, ulkoiluttaminen.
- Tiedon tallennus tiedostoon tai tietokantaan, jolloin käyttäjän nimellä voi seuraavan kerran avata saman kissan
- Käyttäjä saa valita kissan värin

## Käyttöliittymäluonnos

Kolme näkymää: aloitusnäkymä, info-näkymä ja itse kissa-näkymä. Siirtymiset näkymien välillä nuolten mukaisesti.

![](./kuvat/kayttoliittyma_luonnos.jpg)


