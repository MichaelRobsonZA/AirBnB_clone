#!/usr/bin/python3
"""Defines unittests for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Defines unittests for the User class."""

    def test_instance(self):
        """Test instantiation of User class."""
        user = User()
        self.assertIsInstance(user, User)

    def test_attributes(self):
        """Test attributes of User class."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))


if __name__ == '__main__':
    unittest.main()
