#!/usr/bin/env python3
"""
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test Class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock):
        """test_org method"""
        some_client = GithubOrgClient(org_name)
        some_client.org()
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


    def test_public_repos_url(self):
        """test the public_repos_url method of the GithubOrgClient class"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "World"}
            mock.return_value = payload
            some_client = GithubOrgClient("abc")
            result = some_client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self):
        """test public_repos method of the GithubOrgClient class"""


if __name__ == '__main__':
  unittest.main()
