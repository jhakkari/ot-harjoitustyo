import unittest
from repositories.snippet_repository import snippet_repository
from initialize_db import initialize_database


class TestSnippetRepository(unittest.TestCase):
    def setUp(self):
        self.db = initialize_database()

    def test_create_new_snippet_succeeds(self):
        result = snippet_repository.create(1, "ThisIsATestSnippet")
        self.assertTrue(result)

    def test_get_all_return_all_snippets(self):
        snippet_repository.create(1, "ThisIsATestSnippet")
        snippet_repository.create(1, "SecondTestSnippet")
        snippet_repository.create(1, "ThirdTestSnippet")
        snippet_repository.create(1, "FourthTestSnippet")
        results = snippet_repository.get_all(1)
        self.assertEqual(len(results), 4)

    def test_get_all_returns_only_own_snippets(self):
        snippet_repository.create(1, "ThisIsATestSnippet")
        snippet_repository.create(3, "SecondTestSnippet")
        snippet_repository.create(4, "ThirdTestSnippet")
        results = snippet_repository.get_all(2)
        self.assertEqual(results, None)

    def test_delete_all_removes_all_snippets(self):
        snippet_repository.create(3, "ThisIsATestSnippet")
        snippet_repository.create(3, "SecondTestSnippet")
        snippet_repository.create(3, "ThirdTestSnippet")
        results = snippet_repository.get_all(3)
        self.assertEqual(len(results), 3)
        snippet_repository.delete_all(3)
        results_after_delete_all = snippet_repository.get_all(3)
        self.assertEqual(results_after_delete_all, None)

    def test_delete_removes_correct_snippet(self):
        snippet_repository.create(1, "ThisIsATestSnippet")
        snippet_repository.create(1, "SecondTestSnippet")
        snippet_repository.create(1, "ThirdTestSnippet")

        snippet_repository.create(2, "ThisIsATestSnippet")
        snippet_repository.create(2, "SecondTestSnippet")
        snippet_repository.create(2, "ThirdTestSnippet")

        snippet_repository.create(3, "ThisIsATestSnippet")
        snippet_repository.create(3, "SecondTestSnippet")
        snippet_repository.create(3, "ThirdTestSnippet")

        snippet_repository.delete(2)

        self.assertEqual(len(snippet_repository.get_all(1)), 2)
        self.assertEqual(len(snippet_repository.get_all(2)), 3)
        self.assertEqual(len(snippet_repository.get_all(3)), 3)