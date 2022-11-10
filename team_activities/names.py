# Copyright 2020, Brigham Young University-Idaho. All rights reserved.
import pytest as pytest

def make_full_name(given_name, family_name):
    """Return a string in this form "family_name; given_name". For
    example, if this function were called like this:
    make_full_name("Sally", "Brown"), it would return "Brown; Sally".

    Parameters
        given_name: a string that contains a person's given name
        family_name: a string that contains a person's family name
    Return: a string in the form "family_name; given_name"
    """
    full_name = f"{family_name}; {given_name}"
    return full_name


def extract_family_name(full_name):
    """Extract and return the family name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_family_name("Brown; Sally"), it would return "Brown".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's family name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index("; ")

    # Extract a substring from the full name and return it.
    family_name = full_name[0 : semicolon_index]
    return family_name


def extract_given_name(full_name):
    """Extract and return the given name from a string in this form:
    "family_name; given_name". For example, if this function were
    called like this:
    extract_given_name("Brown; Sally"), it would return "Sally".

    Parameter:
        full_name: a string in the form "family_name; given_name"
    Return: a string that contains a person's given name
    """
    # Find the index where "; " appears within the full name string.
    semicolon_index = full_name.index(";")

    # Extract a substring from the full name and return it.
    given_name = full_name[semicolon_index + 2 : ]
    return given_name

#Return: a string in the form "family_name; given_name"


def test_make_full():
    assert make_full_name("Sally", "Brown") == ("Brown; Sally")
    assert make_full_name("Kyle", "Baker") == ("Baker; Kyle")
    assert make_full_name("Jp", "Highfuchown") == ("Highfuchown; Jp")

def test_extract_family():
    assert extract_family_name("Brown; Sally") == ("Brown")
    assert extract_family_name("Highfuchown; Jp") == ("Highfuchown")

def test_given_name():
    assert extract_given_name("Brown; Sally") == ("Sally")
    assert extract_given_name("Highfuchown; Jp") == ("Jp")




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])