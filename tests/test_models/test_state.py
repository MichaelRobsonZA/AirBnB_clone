#!/usr/bin/python3
"""Test module for class State"""

import unittest
import datetime
from models import state


class TestState(unittest.TestCase):
    """Tests for the State class"""

    def test_documentation(self):
        """Test module and class docstring"""
        self.assertIsNotNone(state.__doc__)
        self.assertIsNotNone(state.State.__doc__)

    def test_class(self):
        """Test instance class"""
        instance = state.State()
        self.assertIsInstance(instance, state.State)

    def test_type(self):
        """Test type of instance attributes"""
        instance = state.State()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)


if __name__ == "__main__":
    unittest.main()
