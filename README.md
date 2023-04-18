# Ohjelmistotekniikka, harjoitustyö

## Dokumentaatio

[vaatimusmäärittely](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuuri](https://github.com/jhakkari/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)



## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Alusta tietokanta komennolla:

```bash
poetry run invoke built
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

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
