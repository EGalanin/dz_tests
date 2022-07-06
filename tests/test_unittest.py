import unittest
from unittest.mock import patch
from parameterized import parameterized
import main

OWNERS_SET = {"Аристарх Павлов", "Геннадий Покемонов", "Василий Гупкин"}


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        main.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]

        main.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    def tearDown(self) -> None:
        main.documents = [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]

        main.directories = {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        }

    @parameterized.expand([
        ["2207 876234", True],
        ["11-2", True],
        ["10006", True],
        ["19906", False]
    ])
    def test_check_document_existance(self, user_input, output):
        self.assertEqual(main.check_document_existance(user_input), output)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(main.get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(main.get_all_doc_owners_names(), OWNERS_SET)

    def test_remove_doc_from_shelf(self):
        doc_number = '10006'
        main.remove_doc_from_shelf(doc_number)
        self.assertEqual(main.directories['2'], [])

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['10006']
        self.assertEqual(main.delete_doc(), ('10006', True))

    @parameterized.expand([
        ['4', ('4', True)],
        ['5', ('5', True)],
        ['3', ('3', False)]
    ])
    def test_add_new_shelf(self, user_input, output):
        self.assertEqual(main.add_new_shelf(user_input), output)

    @patch('builtins.input')
    def test_get_doc_shelf(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(main.get_doc_shelf(), '1')


if __name__ == '__main__':
    unittest.main()
