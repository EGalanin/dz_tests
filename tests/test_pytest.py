import pytest
import main

OWNERS_SET = {"Аристарх Павлов", "Геннадий Покемонов", "Василий Гупкин"}


def setup():
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

    def teardown():
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


@pytest.mark.parametrize('number, result',
                         [("2207 876234", True),
                          ("11-2", True),
                          ("10006", True),
                          ("19906", False)
                          ])
def test_check_document_existance(number, result):
    assert main.check_document_existance(number) == result


@pytest.mark.parametrize('number, result',
                         [("2207 876234", "Василий Гупкин"),
                          ("11-2", "Геннадий Покемонов"),
                          ("10006", "Аристарх Павлов"),
                          ("19906", None)
                          ])
def test_get_doc_owner_name(number, result):
    assert main.get_doc_owner_name(number) == result


def test_get_all_doc_owners_names():
    assert main.get_all_doc_owners_names() == OWNERS_SET


def test_remove_doc_from_shelf():
    doc_number = '10006'
    main.remove_doc_from_shelf(doc_number)
    assert main.directories['2'] == []


@pytest.mark.parametrize('shelf, result',
                         [('4', ('4', True)),
                          ('5', ('5', True)),
                          ('3', ('3', False))
                          ])
def test_add_new_shelf(shelf, result):
    assert main.add_new_shelf(shelf) == result


@pytest.mark.parametrize('number, result',
                         [('10006', ('10006', True)),
                          ])
def test_delete_doc(number, result):
    assert main.delete_doc(number) == result
