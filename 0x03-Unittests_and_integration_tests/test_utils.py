#!/usr/bin/env python3
"""
- Parameterizing a unit test
- Mock HTTPS Calls
"""
import unittest
from parameterized import parameterized
import requests
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1)
        ({"a": {"b": 2}}, ("a",), {"b": 2})
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method to test access_nested_map function with valid input"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """method to test exception raise for invalid key"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)

        self.assertEqual(
            f'KeyError({str(e.exception)})', repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls
    """
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        """test utils.get_json function"""
        with patch('requests.get') as mock_request:
            mock_request.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """class to test the memoize function
    """
    def test_memoize(self):
        """method to test memoize function"""
        class TestClass:
            """test class"""
            @Mock()
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()


if __name__ == '__main__':
  unittest.main()
