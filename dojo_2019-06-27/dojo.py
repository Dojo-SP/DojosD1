import pytest


def test_joao_silva():
    assert author("Joao Silva") == "SILVA, Joao"

def test_paulo_coelho():
    assert author("Paulo Coelho") == "COELHO, Paulo"

def test_celso_araujo():
    assert author("Celso de Araujo") == "ARAUJO, Celso de"

def test_gustavo_souza():
    assert author("Gustavo Souza") == "SOUZA, Gustavo"

def test_lowercase():
    assert author("jhonny guielebo") == "GUIELEBO, Jhonny"

def test_uppercase():
    assert author("RENAN CARDOSO") == "CARDOSO, Renan"

def test_upper_lower_da_de_do():
    assert author("MACHADO DE ASSIS") == "ASSIS, Machado de"
    assert author("JHONNY DA SILVA") == "SILVA, Jhonny da"
    assert author("MaRiA dA sIlvA") == "SILVA, Maria da"
    assert author("JoAo Da Perreira") == "PERREIRA, Joao da"
    assert author("Miguel do Sul") == "SUL, Miguel do"

def test_upper_lower_das_dos():
    assert author("JOSE DAS neVes") == "NEVES, Jose das"
    assert author("JOSE dos Palmares") == "PALMARES, Jose dos"

def test_filho():
    assert author("Tarsizio Filho") == "FILHO, Tarsizio"


@pytest.mark.parametrize("name, expected", [
    ("", ""),
    ("LEandro pIGA", "PIGA, Leandro"),
])
def test_io(name, expected):
    assert author(name) == expected


def author(name):
    if name == "": return ""
    listname = name.split()
    lastname = listname[-1].upper() + ","
    firstname = ""
    for word in listname[:-1]:
        if word.lower() in ["de", "da", "do", "das", "dos"]:
            firstname = firstname + " " + word.lower()
        else:
            firstname = firstname + " " + word.capitalize()
    return lastname + firstname





# Só para dizer que existe:

# from unittest import TestCase

# class TestAlgo(TestCase):
#     def test_blah(self):
#         self.assertEqual(0, 0)
