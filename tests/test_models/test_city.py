#!/usr/bin/python3
"""Defines unittests for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Defines unittests for the City class."""

    def test_instance(self):
        """Test instantiation of City class."""
        city = City()
        self.assertIsInstance(city, City)

    def test_attributes(self):
        """Test attributes of City class."""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))


if __name__ == '__main__':
    unittest.main()
