#!/usr/bin/env python3
"""Module to test the client module in client.py"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing class for function GithubOrgClient"""
    @parameterized.expand([("google", ), ("abc", )])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the return value of github org client"""
        org_json = GithubOrgClient(org_name)
        org_json.org.return_value = mock_get_json
        mock_get_json.assert_called_once_with(org_json.
                                              ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test the public repos method in client module"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_obj:
            repo = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_obj.return_value = repo
            self.assertEqual(GithubOrgClient('google').
                             _public_repos_url, repo['repos_url'])

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo, key, expected):
        """Tests the has license method."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)
