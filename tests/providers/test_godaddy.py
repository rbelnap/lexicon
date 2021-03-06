"""Integration tests for Goddady"""
from unittest import TestCase

from integration_tests import IntegrationTests
from lexicon.providers.godaddy import Provider


# Hook into testing framework by inheriting unittest.TestCase and reuse
# the tests which *each and every* implementation of the interface must
# pass, by inheritance from integration_tests.IntegrationTests
class GoDaddyProviderTests(TestCase, IntegrationTests):
    """TestCase for Godaddy"""
    Provider = Provider
    provider_name = 'godaddy'
    domain = 'fullm3tal.online'

    def _filter_headers(self):
        return ['Authorization']
