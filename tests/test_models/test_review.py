#!/usr/bin/python3
"""Test module for class Review"""

import unittest
import datetime
from models import review


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def test_documentation(self):
        """Test module and class docstring"""
        self.assertIsNotNone(review.__doc__)
        self.assertIsNotNone(review.Review.__doc__)

    def test_class(self):
        """Test instance class"""
        instance = review.Review()
        self.assertIsInstance(instance, review.Review)

    def test_type(self):
        """Test type of instance attributes"""
        instance = review.Review()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)


if __name__ == "__main__":
    unittest.main()
