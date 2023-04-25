## Arkkitehtuurikuvaus

### Alustava rakenne pakkauskaaviona
![Pakkauskaavio](./kuvat/alustava_pakkauskaavio.jpg)

### Päätoiminnallisuudet

Sovelluksen päätoiminnallisuuden kuvaaminen sekvenssikaavioina.

#### Uuden koodinpätkän tallentaminen

```mermaid
sequenceDiagram
    actor User
    participant UI
    participant CodeSnippetService
    participant UserService
    participant SnippetRepository
    User->>UI: click "Save" button
    UI->>CodeSnippetService: create_new("Code snippet to be added")
    CodeSnipperService->>UserService: get_user_id()
    UserService->>CodeSnippetService: id
    CodeSnipperService->>SnipperRepository: create(id, "Code snippet to be added")
    SnippetRepository-->CodeSnippetService: True
    CodeSnippetService-->UI: Void
    UI->>UI: _handle_show_main_view
```

Painikkeen painamiseen reagoiva tapahtumankäsittelijä kutsuu koodinpätkien sovelluslogiikasta vastaavan CodeSnippetService metodia create new, antaen parametriksi lisättävän koodinpätkän. CodeSnipperService kutsuu käyttäjätietojen sovelluslogiikasta vastaavan UserService metodia get_user_id(), pyytäen siltä sisäänkirjautuneen käyttäjän id-tunnuksen. Kun tunnus on saatu, CodeSnippetServise kutsuu koodinpätkien tietokantaoperaatioista vastaavan SnipperRepository luokan metodia create, antaen sille parametreina tallennuksen tehneen käyttäjän id-numeron ja tallennettavan koodinpätkän. UserRepository palauttaa True tallennuksen onnistuessa ja CodeSnippetServicestä palataan takaisin käyttöliittymään. Tämän seurauksena käyttöliittymän näkymästä palataan takaisin sovelluksen etusivulle.