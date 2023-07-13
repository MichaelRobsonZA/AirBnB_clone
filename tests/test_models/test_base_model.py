"""Defines test cases for the base model"""
from models.base_model import BaseModel
import datetime
import unittest


class TestBaseModel(unittest.TestCase):
    """Defines test cases for BaseModel class"""
    def setUp(self):
        """Here we set up an instance to test the attributes
        and mmethods of BaseModel so that we don't have to
        create an instance with every test case

        Why? I'm glad you asked. To avoid repetition
        """
        self.b = BaseModel()

    def tearDown(self):
        """ A cleanup method"""
        del(self.b)

    def test_obj_creation(self):
        """This tests the instantiation of BaseModel objects"""
        b1 = BaseModel()
        self.assertIsInstance(self.b, BaseModel)
        self.assertIsInstance(b1, BaseModel)
        self.assertNotEqual(self.b, b1)

    def test_obj_creation_from_dict(self):
        """Tests the creation of an instance from a dictionary"""
        my_model_dict = self.b.to_dict()
        self.assertIsInstance(my_model_dict, dict)
        new = BaseModel(**my_model_dict)
        self.assertIsInstance(new, BaseModel)
        self.assertTrue(hasattr(new, 'id'))
        self.assertTrue(hasattr(new, 'created_at'))
        self.assertTrue(hasattr(new, 'updated_at'))

        # Compare attribute names
        b_attrs = dir(self.b)
        new_attrs = dir(new)
        self.assertEqual(set(b_attrs), set(new_attrs))
        self.assertNotEqual(self.b, new)

    def test_id_attr(self):
        """Each object has a unique uuid, we test the presence of
        the id attribute
        """
        self.assertTrue(hasattr(self.b, 'id'))
        self.assertIsInstance(self.b.id, str)

    def test_created_at_attr(self):
        """Once an object is created, it's time is recorded"""
        self.assertIsInstance(self.b.created_at, datetime.datetime)

    def test_updated_at_attr(self):
        """Does more or less the same thing as test_created_at_attr
        When the object is first created. the attributes created_at
        and updated_at store the same time until a change is made on
        the object
        """
        self.assertIsInstance(self.b.updated_at, datetime.datetime)

    def test_str_method(self):
        """The overwritten str rep of the object is tested"""
        expected_str = f"[BaseModel] ({self.b.id}) {self.b.__dict__}"
        self.assertEqual(str(self.b), expected_str)

    def test_save_method(self):
        """This tests if the updated_at attribute is truly updated"""
        first_update = self.b.updated_at
        self.b.save()
        self.assertNotEqual(self.b.updated_at, first_update)

    def test_to_dict_method(self):
        """The to_dict method adds a new key __class__ with the value
        of the class name. Moreover, the created_at and updated_at(both
        originally being datetime objects) are changed into isoformat

        ::
            This tests the to_dict method and it's return value
        ::
        """
        # Create a dictionary representation and confirm value types
        dict_rep = self.b.to_dict()
        self.assertIsInstance(dict_rep, dict)
        self.assertNotEqual(dict_rep, self.b.__dict__)
        self.assertTrue('__class__' in dict_rep)
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        expected_created_at = self.b.created_at.isoformat()
        self.assertEqual(dict_rep['created_at'], expected_created_at)
        expected_updated_at = self.b.updated_at.isoformat()
        self.assertEqual(dict_rep['updated_at'], expected_updated_at)
        self.assertIsInstance(dict_rep['__class__'], str)
        self.assertIsInstance(dict_rep['id'], str)
        self.assertIsInstance(dict_rep['created_at'], str)
        self.assertIsInstance(dict_rep['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
