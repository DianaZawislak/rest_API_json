"""task 3"""
import json


def test_task3():
    """Create a json string and turn it into a dictionary and test that it is a dictionary"""
    # pylint: unused-import, disable=unused-argument, comparison-with-itself, singleton-comparison

    #JSON string
    json_string = '{"name":"John"."age":30, "city":"New York"}'

    #convert json to python dictionary using json.loads:
    json_string_to_python_dictionary = json.loads(json_string)


    assert isinstance(json_string_to_python_dictionary, dict)
