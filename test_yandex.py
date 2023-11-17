import ya_disk
import config

from unittest import TestCase


class YaDiskTest(TestCase):

    def setUp(self):
        token = config.TOKEN
        self.disk = ya_disk.YaDisk(token)

    def test_status(self):
        expected = 201
        self.disk.delete_item('test')
        result = self.disk.make_dir('test')
        self.assertEqual(expected, result)

    def test_exist(self):
        expected = 'test'
        result = self.disk.disk_list()
        self.assertIn(expected, result)
