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
