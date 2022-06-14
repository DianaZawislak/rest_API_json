"""task 2"""
import json


def test_task2():
    """Create a python dictionary and turn it into a json and test that it is a string"""
    # pylint: unused-import, disable=unused-argument, comparison-with-itself, singleton-comparison
    python_dictionary = {
        "name":"John",
        "age": 30,
        "city": "New York"
    }
    dictionary_to_json = json.dumps(python_dictionary)

    assert isinstance(dictionary_to_json, str)
