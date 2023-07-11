"""Defines test cases for the base model"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines test cases for BaseModel class"""
    def test_obj_creation(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertIsInstance(b2, BaseModel)
        self.assertNotEqual(b1, b2)


if __name__ == '__main__':
    unittest.main()
