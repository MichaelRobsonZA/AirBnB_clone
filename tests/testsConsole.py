#!/usr/bin/python3
"""
Unittests for the Console!
"""
import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestConsole(unittest.TestCase):
    """
    Contains unit tests for the Console class.
    """

    def test_create(self):
        """
        Test the 'create' command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_help(self):
        """
        Test the 'help' command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", f.getvalue())

    def test_show(self):
        """
        Test the 'show' command.
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), "** class name missing **\n")


if __name__ == '__main__':
    unittest.main()
