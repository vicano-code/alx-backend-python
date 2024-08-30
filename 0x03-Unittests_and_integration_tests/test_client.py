#!/usr/bin/env python3
"""
Module for testing client
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
        payload = {"repos_url": "https://api.github.com/orgs/test-org/repos"}
        with patch.object("client.GithubOrgClient.org", return_value=payload):
            some_client = GithubOrgClient("test-org")
            result = some_client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self):
        """test public_repos method of the GithubOrgClient class"""
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "my_license")
    ])
    def test_has_license(self, repo, license_key, expected):
        """unit-test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
    )
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Integration test: fixtures
            Integration test for GithubOrgClient.public_repos method
        """


if __name__ == '__main__':
    unittest.main()
