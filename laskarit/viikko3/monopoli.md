Tehtävä 1

```mermaid
 classDiagram
 
      MonopoliLauta "1" -- "*" Nopat
      MonopoliLauta "1" -- "*" Ruutu
      Pelaaja "1" -- "1" Pelinappula
      Ruutu "1" -- "1" Pelinappula
      class Pelaaja{
      }
      class Pelinappula{
      }
      class Ruutu{
      }
      class Nopat{
      }
      
```

Tehtävä 2

```mermaid
 classDiagram
 
      MonopoliLauta "1" -- "*" Nopat
      MonopoliLauta "1" -- "*" Ruutu
      Pelaaja "1" -- "1" Pelinappula
      Ruutu "1" -- "1" Pelinappula
      Ruutu "1" -- "1" Aloitusruutu
      Ruutu "1" -- "1" Vankila
      MonopoliLauta "1" -- "*" Kadut
      Kadut "*" -- "1" Pelaaja
      Pelaaja "1" -- "*" Rahaa
      MonopoliLauta "1" -- "1" Vankila
      MonopoliLauta "1" -- "1" Aloitusruutu
      Ruutu "1" -- "1" Asema
      Ruutu "1" -- "1" Laitos
      Sattuma "1" -- "1" Kortti
      Yhteismaa "1" -- "1" Kortti
      
      class Pelaaja{
      }
      class Pelinappula{
      }
      class Nopat{
      }
      class Ruutu{
      }
      class Aloitusruutu{
      }
      class Vankila{
      }
      class Kadut{
      }
      class Asema{
      }
      class Laitos{
      }
      class Rahaa{
      }
      class Sattuma{
      }
      class Yhteismaa{
      }
      class Kortti{
      }
```
/* Huom, monopolipelin säännöt eivät olleet entuudestaan tuttuja. Menin materiaalin mukaan sillä oletuksella, ettei yksittäisiä funktioita tai parametreja täydy alustaa tai mainita luokkakaaviossa.
