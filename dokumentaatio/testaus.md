## Testausdokumentti
- Sovellusta on testattu automatisoiduilla testeillä ja pelaamalla

### Asennus
- Sovellus on testattu [käyttöohjeen](./kayttoohje.md) mukaan vain linux ympäristössä

### Manuaalinen testaus
- Peliä on pelattu manuaalisesti monia tunteja, johtaen monien bugien löyntiin ja eliminoimiseen

### Testauskattavuus
Yksikkötestien kattavuus noin 70% main_loopin huono suunitelun takia

### Testaukseen liittyvät laatuongelmat
- Aiemmin mainittu main_loop vaikue testata huono suunnitelun takia, sillä riippuvuuksia vaikea injektoida monien suorien riippuvuuksien takia
