def geo_logs():
    geo_logs = [
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
    ]

    geo_logs[:] = [geo for geo in geo_logs if 'Россия' in list(geo.values())[0]]
    return geo_logs


def queries():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]

    counter = {}

    for requ in queries:
        lenght = len(requ.split())
        if counter.get(lenght, False):
            counter[lenght] += 1
        else:
            counter[lenght] = 1

    counter_sorted = dict(sorted(counter.items()))

    for key, qty in counter_sorted.items():
        print(f'Поисковых запросов из {key} слов: {round(100 / len(queries) * qty, 2)} %')

    return counter_sorted


def geo_data(ids):
    return sorted(list(set([geo_point for geo_data in ids.values() for geo_point in geo_data])))


def ad_channel(stats):
    maximum = 0
    for max_stats in stats.items():
        if max_stats[1] > maximum:
            max_name = max_stats[0]
            maximum = max_stats[1]
    return max_name


if __name__ == '__main__':
    stats = {'facebook': 4955, 'yandex': 120, 'vk': 3115, 'google': 99, 'email': 42, 'ok': 98}
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    print(len(geo_logs()))
    print('----------')
    print(queries())
    print('----------')
    print(geo_data(ids))
    print('----------')
    print(ad_channel(stats))
