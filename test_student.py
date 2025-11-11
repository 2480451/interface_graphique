# test
import pytest
from student import Student
from unittest.mock import patch

def test_name_is_striped():
    s = Student("  Sam  ")
    assert s.name == "Sam"

def test_creation_nom():
    s = Student("Nom")
    assert s.name == "Nom"

@pytest.mark.parametrize("bad", ["", " ", None, 123])
def test_nom_invalide(bad):
    with pytest.raises(ValueError):
        Student(bad)

def test_note_valide():
    s = Student("Sam")
    s.add_note(75)
    s.add_note(80)
    g = s.grades
    assert g ==[75, 80]
    assert s ==[75,80]

@pytest.fixture
def student():
    s = Student("Nom")
    yield s


def test_ajout_note(student):
    student.add_note(100)
    student.add_note(50)
    student.add_note(70)
    student.add_note(90)

    assert len(student._grades) == 4
