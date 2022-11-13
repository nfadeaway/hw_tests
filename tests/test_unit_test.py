import unittest
from parameterized import parameterized, parameterized_class

from main import filter_geo_logs, unic_geo, sort_stats

FIXTURE_FILTER_GEO_LOGS = [
    ([
         {'visit1': ['Москва', 'Россия']},
         {'visit2': ['Дели', 'Индия']},
         {'visit3': ['Владимир', 'Россия']},
         {'visit4': ['Лиссабон', 'Португалия']},
         {'visit5': ['Париж', 'Франция']},
         {'visit6': ['Лиссабон', 'Португалия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Архангельск', 'Россия']}
     ],
     'Россия',
     [
         {'visit1': ['Москва', 'Россия']},
         {'visit3': ['Владимир', 'Россия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Архангельск', 'Россия']}
     ]),
    ([
         {'visit1': ['Лиссабон', 'Португалия']},
         {'visit2': ['Лиссабон', 'Португалия']},
         {'visit3': ['Лиссабон', 'Португалия']},
         {'visit4': ['Лиссабон', 'Португалия']},
         {'visit5': ['Париж', 'Франция']},
         {'visit6': ['Лиссабон', 'Португалия']},
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']},
         {'visit10': ['Париж', 'Франция']}
     ],
     'Россия',
     [
         {'visit7': ['Тула', 'Россия']},
         {'visit8': ['Тула', 'Россия']},
         {'visit9': ['Курск', 'Россия']}
     ]),
    ([
         {'visit10': ['Париж', 'Франция']}
     ],
     'Россия',
     [])
]

FIXTURE_UNIC_GEO = [
    (
        {'user1': [213, 213, 213, 15, 213], 'user2': [54, 54, 119, 119, 119], 'user3': [213, 98, 98, 35]},
        [98, 35, 15, 213, 54, 119]
    ),
    (
        {'user1': [0, 213, 213, 15, 213], 'user2': [54, 54, 119, 13, 119], 'user3': [213, 98, 100, 35]},
        [0, 13, 15, 213, 98, 35, 100, 54, 119]
    ),
    (
        {'user1': [0, 1, 2, 3, 4], 'user2': [0, 0, 0, 0, 5]},
        [0, 1, 2, 3, 4, 5]
    )
]

FIXTURE_SORT_STATS = [
    (
        {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98},
        'yandex'
    ),
    (
        {'facebook': 55, 'yandex': 120, 'vk': 300, 'google': 99, 'email': 42, 'ok': 98},
        'vk'
    ),
    (
        {'facebook': 55, 'yandex': 120, 'vk': 300, 'google': 99, 'email': 42, 'ok': 500},
        'ok'
    )
]


class TestFunc(unittest.TestCase):

    @parameterized.expand(FIXTURE_FILTER_GEO_LOGS)
    def test_filter_geo_logs(self, dirty_geo_logs, target_country, etalon):
        result = filter_geo_logs(dirty_geo_logs, target_country)
        self.assertEqual(result, etalon)

    @parameterized.expand(FIXTURE_UNIC_GEO)
    def test_unic_geo(self, dirty_ids, etalon):
        result = unic_geo(dirty_ids)
        self.assertEqual(result, etalon)

    @parameterized.expand(FIXTURE_SORT_STATS)
    def test_sort_stats(self, unsorted_stats, etalon):
        result = sort_stats(unsorted_stats)
        self.assertEqual(result, etalon)
