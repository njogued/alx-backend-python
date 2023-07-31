#!/usr/bin/env python3
"""Unittest for the nested map function"""
import unittest
from parameterized import parameterized
access_nested_map = __import__("utils").access_nested_map


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
        ("no dict", {}, ["a"]),
        ("no key b", {"a": 1}, ["a", "b"]),
    ])
    def test_access_nested_map_exception(self, _, nested_dict, path):
        """Check whether the access nested map raises an exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_dict, path)


if __name__ == "__main__":
    unittest.main()
