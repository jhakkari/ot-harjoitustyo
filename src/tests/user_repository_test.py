import unittest
from repositories.user_repository import user_repository
from initialize_db import initialize_database


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.db = initialize_database()

    def test_create_new_user(self):
        result = user_repository.create("testuser", "testpassword")
        self.assertTrue(result)

    def test_create_new_user_with_existing_username_fails(self):
        result = user_repository.create("testuser", "testpassword")
        self.assertTrue(result)
        result = user_repository.create("testuser", "testpassword")
        self.assertFalse(result)

    def test_existing_user_found_on_db(self):
        result = user_repository.create("test", "testpassword")
        self.assertTrue(result)
        result = user_repository.check_existing("test")
        self.assertTrue(result)

    def test_nonexisting_user_not_found_on_db(self):
        result = user_repository.check_existing("testikayttaja")
        self.assertFalse(result)
