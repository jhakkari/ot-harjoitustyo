import pyperclip
from repositories.snippet_repository import snippet_repository
from services.user_service import user_service
from entities.snippet import Snippet

class InvalidInputError(Exception):
    pass

class SnippetCopiedToClipboard(Exception):
    pass

class CodeSnippetService:
    """Koodinpätkien hallintaan liittyvästä logiikasta vastaava luokka.
    """

    def __init__(self):
        self._user_service = user_service
        self._snippet_repository = snippet_repository

    def create_new(self, content):
        """Luo uuden koodinpätkän.

        Args:
            content: Luotavan koodinpätkän haluttu sisältö.

        Raises:
            InvalidInputError: Virhe, tapahtuu kun yritetään luoda tyhjää koodinpätkää.

        Returns:
            True luomisen onnistuessa, muussa tapauksessa False.
        """

        if not content:
            raise InvalidInputError("Nothing to add")

        return self._snippet_repository.create(self._user_service.get_user_id(), content)

    def get_snippets_list(self):
        """Palauttaa käyttäjän tallentamat koodinpätkät.

        Returns:
            Palauttaa kirjautuneen käyttäjän tallentamat koodinpätkät Snippet-olioiden listana.
            Mikäli ei tallennettuja, palauttaa None.
        """

        results = self._snippet_repository.get_all(self._user_service.get_user_id())
        if not results:
            return None

        snippets = []
        for row in results:
            snippets.append(Snippet(row[0], row[1], row[2], row[3]))

        return snippets

    def remove(self, snippet_id):
        """Poistaa koodinpätkän.

        Args:
            snippet_id: Poistettavan koodinpätkän yksilöivä id-tunnus.

        Returns:
            True poistamisen onnistuessa, muussa tapauksessa False.
        """

        return snippet_repository.delete(snippet_id)

    def remove_all_user_snippets(self):
        """Poistaa kirjautuneen käyttäjän koodinpätkät.

        Returns:
            Palauttaa True
        """

        return self._snippet_repository.delete_all(self._user_service.get_user_id())

    def set_clipboard_contents(self, snippet):
        """Lisää koodinpätkän käyttäjän tietokoneen leikepöydälle.

        Args:
            snippet: Lisättävä koodinpätkä.

        Raises:
            SnippetCopiedToClipboard: Virhe, (tai ilmoitus) toteutuneesta lisäämisestä.
        """

        pyperclip.copy(snippet)

        raise SnippetCopiedToClipboard("Copied to clipboard")

    def get_clipboard_contents(self):
        """Hakee käyttäjän tietokoneen leikepöydän sisällön.

        Returns:
            Käyttäjän leikepöydän sisältö tekstimuodossa.
        """

        return pyperclip.paste()

snippet_service = CodeSnippetService()
