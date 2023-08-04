#!/usr/bin/env python3
"""Unittest for the nested map function"""
from parameterized import parameterized
import unittest
import utils
from unittest import mock
from unittest.mock import patch
access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """Unittesting the nestedmap class"""
    @parameterized.expand([
        ("one k/v dict", {"a": 1}, ["a"], 1),
        ("nested dict", {"a": {"b": 2}}, ["a"], {"b": 2}),
        ("to last element", {"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, _, nested_dict, path, output):
        """Check the correct output of nested map function"""
        self.assertEqual(access_nested_map(nested_dict, path), output)

    @parameterized.expand([
        ("no dict", {}, ["a"], KeyError),
        ("no key b", {"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception(self, _, nested_dict, path, expected_error):
        """Check whether the access nested map raises an exception"""
        with self.assertRaises(expected_error):
            access_nested_map(nested_dict, path)


class TestGetJson(unittest.TestCase):
    """Class to test the get_json method in utils file"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, url, expected_output):
        """Test whether the get json method works"""

        with unittest.mock.patch('utils.requests') as mock_req:
            mock_resp = mock.Mock()
            mock_resp.json.return_value = expected_output
            mock_req.get.return_value = mock_resp
            payload = get_json(url)
            mock_req.get.assert_called_once_with(url)
            self.assertEqual(payload, expected_output)


if __name__ == "__main__":
    unittest.main()
