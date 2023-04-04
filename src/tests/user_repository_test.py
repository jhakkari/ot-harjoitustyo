import unittest
from repositories import user_repository
from initialize_db import initialize_database

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.db = initialize_database()

    def test_register_new_user(self):
        result = user_repository.register("testuser", "testpassword")
        self.assertTrue(result)
