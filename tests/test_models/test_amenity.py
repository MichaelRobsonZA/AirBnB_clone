#!/usr/bin/python3
"""Test module for class Amenity"""

import unittest
import datetime
from models import amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def test_documentation(self):
        """Test module and class docstring"""
        self.assertIsNotNone(amenity.__doc__)
        self.assertIsNotNone(amenity.Amenity.__doc__)

    def test_class(self):
        """Test instance class"""
        instance = amenity.Amenity()
        self.assertIsInstance(instance, amenity.Amenity)

    def test_type(self):
        """Test type of instance attributes"""
        instance = amenity.Amenity()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
