
# Arkkitehtuurikuvaus

## Rakenne

Ohjelman tärkeiden kansioiden pakkausrakenne on seuraava:

```mermaid
 classDiagram
      ui  ..>  entities_and_services
      
      
      class ui{
      }
      class entities_and_services{
      }
```

Kansio ui sisältää käyttöliittymään liittyviä tiedostoja, ja kansio entities_and_services sisältää sovelluslogiikkaan ja luokkiin liittyviä tiedostoja. Käyttöliittymästä kutsutaan entities_and_services luokan metodeja sovelluslogiikkaan liittyvissä toiminnoissa. 

### Käyttöliittymä

Käyttöliittymä koostuu kolmesta näkymästä: aloitusnäkymä, ohjeet-näkymä ja kissa-näkymä. Käyttöliittymä on toteutettu tkinter:lla. Joka näkymälle on oma luokkansa, ja käyttöliittymä on pyritty eristämään sovelluslogiikasta mahdollisimman hyvin.

### Sovelluslogiikka

Sovelluksen sovelluslogiikan muodostaa luokat Owner sekä PetCat. Ohjelman luokkakaavio on seuraava:

```mermaid
 classDiagram
      Owner "1" -- "1" PetCat
      UI "1" -- "1" Owner
      
      class Owner{
          name
          owners_cat
          add_owner_name(owner_name)
          add_cat_name(cat_name)
          feed_cat(cat)
          play_cat(cat)
      }
      class PetCat{
          name
          food_percent
          play_percent
          countdown
          timer
          set_difficulty(level)
          stats_percent(action, percent)
          stats_decrease()
          stats_thread()
      }
      class UI{
      }
```
Luokka PetCat sisältää metodeja liittyen kissan toimintaan, Owner luokka taas käyttäjään liittyvää toimintaa sekä toimintoja, mitä käyttäjä voi tehdä kissalle. Luokkakaaviossa näkyy myös luokkien metodit. PetCat luokkaa käsitellään vain Owner luokan kautta. 

### Tietojen pysyväistallennus

Sovelluksessa ei ole tällä hetkellä toteutettu tietojen pysyväistallennusta. Tämä toteutetaan mahdollisesti tulevaisuudessa. Ohjelman suoritusaikainen tallennus tapahtuu Owner sekä PetCat-olioissa. Tieto säilyy niissä niin kauan, kuin käyttäjä pitää Cat-näkymää auki. 

### Päätoiminnallisuudet

Ohjelman päätoiminnallisuudet ovat käyttäjän ja kissan luominen sekä kissan syöttäminen ja leikittäminen.
Alle on kuvastettu muutamat sekvenssikaavioina. 

#### Käyttäjän ja kissan luominen:

```mermaid
sequenceDiagram
   actor Käyttäjä
   participant UI
   participant Owner
   participant PetCat
   Käyttäjä->>UI: Paina "Aloita" nappia
   UI->>UI: _handle_start_button_click()
   UI->>UI: self._are_names_valid(käyttäjännimi, kissannimi)
   UI->>Owner: self.owner.add_owner_name(käyttäjänimi)
   UI->>Owner: self.owner.add_cat_and_name(kissanimi)
   Owner->>PetCat: PetCat(kissannimi)
   UI->>PetCat: self._owner.owners_cat.set_difficulty(self.level)
   UI->>PetCat: self.owner.owners_cat.countdown=True
   UI->>UI: _handle_cat()
  
```
Painikkeen painaminen tarkistaa ensin UI-luokan sisäisellä metodilla, onko nimet ja vaikeustaso valittu. Jos nimet ovat kunnossa aktivoituu metodi joka yhdistää nimitiedot owner olioon. Kissa-olio luodaan Owner-luokassa, ja kissa yhdistetään samalla käyttäjään. Asetetaan vaikeustaso, joka määräytyy sen mukaan mitä nappia käyttäjä on painanut. Countdown arvo laitetaan päälle jotta kissan tarve-prosentit voivat seuraavassa näkymässä toimia oikein. Käyttöjärjestelmä kutsuu omaa metodiaan joka siirtää käyttäjän seuraavaan Cat-näkymään.



#### Kissan ruokkiminen

```mermaid
sequenceDiagram
   actor Käyttäjä
   participant UI
   participant Owner
   participant PetCat
   Käyttäjä->>UI: Paina "Ruoki minua!" nappia
   UI->>UI: _handle_food_button_click()
   UI->>Owner: self._owner.feed_cat(self._owner.owners_cat)
   Owner->>PetCat: cat.stats_percent("food", 5)
   PetCat-->>Owner: "under_limit" tai "over_limit"
   Owner-->> UI: "under_limit" tai "over_limit"
  
```  
Painikkeen painaminen johtaa metodiin, joka kutsuu Owner luokan feed_cat metodia. Kyseisessä metodissa annetaan parametrit kissan prosenttien päivittämiselle, ja kutsutaan PetCat luokan metodia stats_percent. Siellä tarkistetaan, jos prosentit ovat jo yli 100 tai alle 0. Jos ovat, metodi palauttaa "under_limit" tai "over_limit". Muuten se korottaa PetCat olion food_percent muuttujaa. Palautusarvo välitetään käyttöliittymään, missä päivitetään tarpeen mukaan kommentti liiallisesta ruokamäärästä tai karannut-viesti. Jos paluuarvo ei ole kumpikaan, päivitetään kommentti hyvästä ruuasta.

#### Kissan leikittäminen

```mermaid
sequenceDiagram
   actor Käyttäjä
   participant UI
   participant Owner
   participant PetCat
   Käyttäjä->>UI: Paina "Leiki kanssani!" nappia
   UI->>UI: _handle_play_button_click()
   UI->>Owner: self._owner.play_cat(self._owner.owners_cat)
   Owner->>PetCat: cat.stats_percent("play", 5)
   PetCat-->>Owner: "under_limit" tai "over_limit"
   Owner-->> UI: "under_limit" tai "over_limit"

``` 
Toimii samalla lailla kuin yllä oleva kissan ruokkiminen.


#### Muut sovelluksen toiminnallisuudet 
Ne toteutuvat myös nappia painamalla, jolloin tapahtumakäsittelijä kutsuu siihen sopivaa metodia joka joko päivittää tai muuttaa arvoja, tai siirtyy näkymästä toiseen. Taustalla tapahtuvat toiminnallisuudet kuin kissan prosenttien vähenemien ja kuvien muuttuminen lähtevät käyntiin Cat-näkymään siirtyessä ja päivittyvät taustalla sovelluslogiikan metodien ehtojen mukaan.

### Ohjelman rakenteeseen jääneet heikkoudet

PetCat ja Owner luokat olisi voitu refaktoroida paremmin service ja entities rakenteen mukaisesti. Tiedontalletus puuttuu.
