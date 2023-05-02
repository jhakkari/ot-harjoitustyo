# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio

[Käyttöohje](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Releaset

[Viikko 6 release](https://github.com/jhakkari/ot-harjoitustyo/releases/tag/viikko6)

[Viikko 5 release](https://github.com/jhakkari/ot-harjoitustyo/releases/tag/viikko5)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta tietokanta komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```
Huom!
Sovellus käyttää riippuvuutenaan pyperclip moduulia. Tämän pitäisi toimia ongelmitta Windows, Mac ja Linux laitteilla.
Ongelmatilanteessa lisätietoa [täältä](https://pypi.org/project/pyperclip/)

## Komentorivitoiminnot

Ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Koodin laadun voi tarkastaa pylintin avulla, komennolla:

```bash
poetry run invoke lint
```
