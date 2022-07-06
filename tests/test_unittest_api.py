import unittest
from api import YaDisk

with open('token.txt', 'r') as f:
    token_YD = f.read().strip()


class TestYaDisk(unittest.TestCase):

    def SetUp(self):
        pass

    # Первое создание папки "TEST"
    def test_get_folder_201(self):
        d = YaDisk(token_YD, "TEST")
        self.assertEqual(d.get_folder(), 201)

    # Папка "TEST" уже существует
    def test_get_folder_409(self):
        d = YaDisk(token_YD, "TEST")
        self.assertEqual(d.get_folder(), 409)

    # Папка не найдена
    def test_info_to_folder_404(self):
        d = YaDisk(token_YD, "TEST")
        d.del_folder()
        self.assertEqual(d.info_to_folder(), 404)

    def TearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
