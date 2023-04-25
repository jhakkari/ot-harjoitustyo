import unittest
from services.snippet_service import snippet_service, InvalidInputError
from services.user_service import user_service
from entities.snippet import Snippet
from initialize_db import initialize_database

class TestCodeSnippetService(unittest.TestCase):
    def setUp(self):
        self.db = initialize_database()
        user_service.register("testikayttaja", "testi123", "testi123")

    def test_create_new_snippet_succeeds(self):
        result = snippet_service.create_new("SELECT id, user_id, content, created_at FROM")
        self.assertTrue(result)

    def test_create_new_blank_snippet_fails(self):
        self.assertRaises(InvalidInputError, lambda: snippet_service.create_new(""))

    def test_get_snippets_list_returns_correct_list_of_objects(self):
        snippet_service.create_new("Another test")
        snippet_service.create_new("Second snippet")
        snippet_service.create_new("One more test")
        results = snippet_service.get_snippets_list()
        self.assertEqual(len(results), 3)
        self.assertEqual(results[0].content, "Another test")
        self.assertEqual(results[0].id, 1)
        self.assertEqual(results[0].user_id, 1)
        self.assertEqual(results[1].content, "Second snippet")
        self.assertEqual(results[2].content, "One more test")