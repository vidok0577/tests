import pytest
import collection_data
from unittest import TestCase


class CollectionData(TestCase):

    def test_geo_logs(self):
        expected = 6
        result = len(collection_data.geo_logs())
        self.assertEqual(result, expected)

    def test_queries(self):
        expected = 2
        result = len(collection_data.queries())
        self.assertGreaterEqual(expected, result)

    def test_geo_data(self):
        expected = 213
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        self.assertIn(expected, collection_data.geo_data(ids))


@pytest.mark.parametrize(
    'stats, expected',
    [
        ({'facebook': 4955, 'yandex': 120, 'vk': 3115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook'),
        ({'facebook': 495, 'yandex': 120, 'vk': 3115, 'google': 99, 'email': 42, 'ok': 98}, 'vk'),
        ({'facebook': 49, 'yandex': 120, 'vk': 31, 'google': 99, 'email': 42, 'ok': 98}, 'yandex')
    ]
)
def test_ad_channel(stats, expected):
    assert collection_data.ad_channel(stats) == expected


@pytest.mark.parametrize(
    'ids, expected',
    [
        ({'user1': [213, 213, 213, 15, 213],
          'user2': [54, 54, 119, 119, 119],
          'user3': [213, 98, 98, 35]},
         213),
        ({'user1': [21, 21, 213, 15, 213],
          'user2': [54, 54, 21, 119, 119],
          'user3': [213, 98, 21, 35]},
         21)
    ]
)
def test_geo_data(ids, expected):
    assert expected in collection_data.geo_data(ids)