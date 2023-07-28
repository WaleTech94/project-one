import pytest
from lib.todolist import *
# Given a string that contains #TODO, it should return the string
# check_for_todo("#TODO Wash Dishes") == "#TODO Wash Dishes"
def test_todo_in_string():
    result = check_for_todo("#TODO Wash Dishes")
    assert result == "#TODO Wash Dishes"

# Given a string without #TODO, it should return False
# check_for_todo("Tidy Bathroom") == False
def test_todo_not_in_string():
    result = check_for_todo("Tidy Bathroom")
    assert result == False

# Given a non string, it should raise an error
# check_for_todo(123) == "This is not a valid string"
def test_for_non_string():
    with pytest.raises(Exception) as err:
        check_for_todo(123)
    error_message = str(err.value)
    assert error_message == "This is not a valid string"

# Given an empty string, it should raise an error
# check_for_todo("") == "This is not a valid string
def test_for_empty_string():
    with pytest.raises(Exception) as err:
        check_for_todo("")
    error_message = str(err.value)