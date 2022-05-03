## Viikko 3
- Luotu sovelluksen ydinluokat:
	- Owner: vastaa käyttäjän toiminnoista
	- PetCat: vastaa kissan tiedoista
	- UserInterface: vastaa käyttöliittymästä
- Eriytetty käyttöliittymästä sovelluksen käynnistäminen omaan tiedostoon index.py.
- Aloitettu testaaminen PetCat luokasta.

## Viikko 4
- Kissan tarve-prosentteihin liittyvä countdown luotu, eli prosentit pienenevät 5sek välein. 
- Kun joku tarpeista päätyy nollaan, kissa karkaa ja sovellus lopettaa itsensä (täytyy vielä hienosäätää).
- Alustava graafinen käyttöliittymään luotu:
	- Start näkymä: tarvittavat elementit lisätty ja napeista siirtymät toisiin näkymiin toimivat
	- Cat näkymä: Karkeasti tarvittavat elementit hahmoteltu
	- Info näkymä (tyhjä)
	- Graafista käyttöliittymää ei vielä yhdistetty muun sovelluksen koodiin vaan toimii erillään.
- Laajennettu testikattavuutta.
- Ohjelmaan lisätty pylint työkalu.
- Luokkakaavio tehty arkkitehtuuritiedostoon.

## Viikko 5
- Sovelluslogiikkaa alettu yhdistämään graafiseen käyttöliittymään:
	- Käyttäjän nimi ja kissan nimi saadaan käsin syötettyä ja ne siirtyvät Cat näkymään
	- Cat näkymässä näkyy reaaliaikaiset kissan statukset 
	- "Leiki kanssani" ja "Ruoki minua" napit korottavat oikeaa statusta ja oikealla tavalla 		reaaliaikaisesti.
	- Statuksien countdown toiminto ei ole vielä yhdistetty graafiseen käyttöliittymään.
- Piirretty kissa ja siitä eri versiot statuksien mukaan (iloinen, surullinen, laiha, kookas). Kuvia ei integroitu vielä ohjelmaan.
- Laajennettu testikattavuutta ja siistitty koodia pylintin mukaan.
- Pakkausrakennekaavio tehty arkkitehtuuritiedostoon.
- Tehty GitHub release.

## Viikko 6
- Countdown integroitu graafiseen käyttöliittymään, eli ruoka ja leikkiprosentit vähenevät automaattisesti kissanäkymässä.
- Ulkoinen `emoji` kirjasto lisätty ja käytetty sovelluksessa.
- Kissakuvat integroitu käyttöliittymään. Kuvien vaihto ei vielä saatu toimimaan. 
- Lisätty kommenttikenttiä start- ja kissanäkymiin. Kissanäkymän kommentteja vielä lisätään.
- Asetettu reunaehtoja:
	- Jos nimikenttä/-kentät ovat tyhjiä, ei päästä eteenpäin:kommenttikenttään tästä ilmoitus
	- Jos syöttää tai leikittää kissaa tietyn rajan yli, prosentit eivät enää nouse: kommenttikenttään ilmoitus
	- Jos jompikumpi prosentti putoaa nollan alle, prosentteja ei saa enää nostettua. Jos nappeja painaa, tulee ilmoitus kissan karanneen.
- Alustava arkkitehtuurikuvaus tehty, sisältäen mm. edellisviikon poisjääneen sekvenssikaavion.
- Alustava käyttöohje tehty.
- Docstring dokumentaatio aloitettu ja katettu yli 50%. 
- Laajennettu testikattavuutta
- Siistitty koodia pylintin mukaan sekä itse tarkasteltu mm. Clean Code ja Single responsibility näkökulmista.
- Tehty toka GitHub release.
