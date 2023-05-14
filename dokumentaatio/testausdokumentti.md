# Testausdokumentti

Sovellusta on testattu automaatisoiduin yksikkö- ja integraatiotestein unittestilla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikan luokkia `UserService` ja `CodeSnippetService` testataan `TestUserService` ja `TestCodeSnippetService` testiluokilla. Sovellusluokkien testit alustetaan tyhjentämällä tietokanta ja luomalla tarvittavat taulut uudelleen. Testit testaavat sovelluslogiikan ja repositioiden yhteistä toimintaa.

### Repositio-luokat

Tietokantaoperaatioista vastaavia `UserRepository`:a ja `SnippetRepository`:a testataan `TestUserRepository` ja `TestSnippetRepository` luokilla. Testeissä käytetään sovelluksen varsinaista tietokantaa, joka alustetaan kokonaisuudessaan ennen jokaista testiä.

## Testikattavuus

![testikattavuus](./kuvat/testikattavuus.jpg)