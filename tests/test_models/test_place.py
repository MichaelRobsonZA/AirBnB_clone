#!/usr/bin/python3
"""Test module for class Place"""

import unittest
import models
import datetime


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def test_documentation(self):
        """Test module and class docstring"""
        self.assertIsNotNone(models.place.__doc__)
        self.assertIsNotNone(models.place.Place.__doc__)

    def test_class(self):
        """Test instance class"""
        instance = models.place.Place()
        self.assertIsInstance(instance, models.place.Place)

    def test_type(self):
        """Test type of instance attributes"""
        instance = models.place.Place()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.city_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.description, str)
        self.assertIsInstance(instance.number_rooms, int)
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertIsInstance(instance.max_guest, int)
        self.assertIsInstance(instance.price_by_night, int)
        self.assertIsInstance(instance.latitude, float)
        self.assertIsInstance(instance.longitude, float)
        self.assertIsInstance(instance.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
