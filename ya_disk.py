import requests

import config


class YaDisk:
    def __init__(self, token: str):
        self.HOST = 'https://cloud-api.yandex.net:443'
        self.headers = {'Accept': 'application/json', 'Authorization': token}
        self.uri = '/v1/disk/resources'

    def make_dir(self, item: str):
        url = self.HOST + self.uri
        params = {'path': item}
        request = requests.put(url, headers=self.headers, params=params)
        return request.status_code

    def disk_list(self):
        url = self.HOST + self.uri
        request = requests.get(url, headers=self.headers, params={'path': '/'}).json()
        result = [i['name'] for i in request['_embedded']['items']]
        return result

    def delete_item(self, item: str):
        url = self.HOST + self.uri
        params = {'path': item, 'force_async': 'false', 'permanently': 'true'}
        request = requests.delete(url, headers=self.headers, params=params)
        return request.status_code


if __name__ == '__main__':
    token = config.TOKEN  # input('Введите токен: ')
    disk = YaDisk(token)
    dir_name = 'test'  # input('Введите имя создаваемой папки: ')
    print(disk.make_dir(dir_name))
    print(disk.disk_list())
    print(disk.delete_item(dir_name))
