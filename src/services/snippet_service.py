from repositories.snippet_repository import snippet_repository
from services.user_service import user_service
from entities.snippet import Snippet

class InvalidInputError(Exception):
    pass


class CodeSnippetService:

    def __init__(self):
        self._user_service = user_service
        self._snippet_repository = snippet_repository

    def create_new(self, content):
        if not content:
            raise InvalidInputError("Nothing to add")

        return self._snippet_repository.create(self._user_service.get_user_id(), content)

    def get_snippets_list(self):
        results = self._snippet_repository.get_all(self._user_service.get_user_id())
        if not results:
            return None

        snippets = []
        for row in results:
            snippets.append(Snippet(row[0], row[1], row[2], row[3]))

        return snippets

snippet_service = CodeSnippetService()
