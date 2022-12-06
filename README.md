# Ohjelmistotekniikka harjoitustyö
## Uni Survivors

### Dokumentaatio 

[Changelog](dokumentaatio/changelog.md)

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Tyäaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

[Julkaisu 1.0](https://github.com/Teetil/ot-harjoitustyo/releases/tag/viikko5)


## Ohjelman käyttäminen

### Asenna riippuvuudet komennolla

```bash
poetry install
```

### Aloita sovellus komennolla

```bash
poetry run invoke start
```
### Testit voi suorittaa komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla

```bash
poetry run invoke coverage-report
```

Raportti löytyy htmlcov hakemistosta

### Pylint

Tiedoston .pylintrc määrittelemät tarkastukset pystyy suorittamaan komennolla

```bash
poetry run invoke lint
```
