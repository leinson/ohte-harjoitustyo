
### Luokkakaavio

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
          stats_percent(action, percent)
          stats_decrease()
          stats_thread()
          run_away()
      }
      class UI{
      }
```
Luokka PetCat sisältää metodeja liittyen kissan toimintaan, Owner luokka taas käyttäjään liittyvää toimintaa sekä toimintoja, mitä käyttäjä voi tehdä kissalle. PetCat luokkaa käsitellään vain Owner luokan kautta. 

### Pakkauskaavio

```mermaid
 classDiagram
      ui  ..>  entities_and_services
      
      
      class ui{
      }
      class entities_and_services{
      }
```

Kansio ui sisältää käyttöliittymään liittyviä tiedostoja, ja kansio entities_and_services sisältää sovelluslogiikkaan ja luokkiin liittyviä tiedostoja. 

### Kommentti
Jos aikaa riittää, eriytetään mahdollisesti PetCat ja Owner metodeja järkevämmin eri luokkiin entities ja services rakenteen mukaisesti.


