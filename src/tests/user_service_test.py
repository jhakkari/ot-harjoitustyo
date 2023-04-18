import unittest
from services.user_service import UserService, PasswordsDoNotMatchError, IncorrectInputError, UsernameAlreadyExistsError
from initialize_db import initialize_database


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.db = initialize_database()
        self.user_service = UserService()

    def test_register_with_correct_credentials_succeeds(self):
        self.user_service.register("username", "password", "password")
        self.assertTrue(self.user_service.login_status())

    def test_register_with_existing_username_fails(self):
        self.user_service.register("kayttaja", "sala", "sala")
        self.assertRaises(
            UsernameAlreadyExistsError,
            lambda: self.user_service.register("kayttaja", "sala", "sala")
        )

    def test_register_with_empty_username_and_password_fails(self):
        self.assertRaises(
            IncorrectInputError,
            lambda: self.user_service.register("", "", "")
        )

    def test_register_with_different_passwords_fails(self):
        self.assertRaises(
            PasswordsDoNotMatchError,
            lambda: self.user_service.register("testikayttaja", "1234", "5678")
        )

    def test_register_with_too_long_username_amd_password_fails(self):
            self.assertRaises(
            IncorrectInputError,
            lambda: self.user_service.register("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "11111111111111111111111111111", "11111111111111111111111111111")
            )

    def test_login_with_correct_username_and_password_succeeds(self):
        self.user_service.register("testuser", "password", "password")
        self.user_service.logout()
        self.user_service.login("testuser", "password")
        status = self.user_service.login_status()
        self.assertTrue(status)
    
    def test_logout_succeeds(self):
        self.user_service.register("testuser", "password", "password")
        self.assertTrue(self.user_service.login_status())
        self.user_service.logout()
        self.assertFalse(self.user_service.login_status())
