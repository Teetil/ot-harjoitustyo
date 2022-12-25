# Käyttöohje
- Lataa lähdekoodi [Releases](https://github.com/Teetil/ot-harjoitustyo/releases) sivulta
- Asenna riippuvuudet komentoriviltä komennolla
```bash
poetry install
```
Käynnistä peli komennolla
```
poetry run invoke start
```
## Pelaaminen
- Paina mitä tahansa näppäintä aloittaaksesi
- Aseet ampuvat itsestään lähimpiä vihollisia, joten voit rentutua ja vain liikkua wasd näppämistä.
- Viholliset pudottavat kuolessaan sinisiä neliötä joiden päälle juostessa saa XP:tä
- Kun pohjassa oleva XP palkki täyttyy, saat, joka valita uuden aseen, parantaa satunnaisesti nykyistä tai täyttää elämäsi
- Yritä selvitä mahdollisimman pitkään, peli vaikenee joka 20 sekuntti huomatavasti, mutta niin lisäntyvät saamasi pisteetkin.
- Aseiden vahinkoa, nopeutta ja muuta voi muuttaa JSON tiedostosta, jokainen satunnainen päivitys on prosentuaalinen, joten näillä on oikeasti väliä
