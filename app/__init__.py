"""This is the app demonstrates logging configuration and unit testing"""

import http.client
import json
import logging
import logging.config
import logging.config
import os

from dotenv import load_dotenv
from ratelimiter import RateLimiter


class Config(object):
    """This provides configuration information"""
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'logs'))


@RateLimiter(max_calls=1, period=1)
def geo_api_request(endpoint):

    """This makes a request to hotels on rapid api and saves the request to the hotels_api_response logger"""
    # This creates an HTTP connection to make a request
    conn = http.client.HTTPSConnection('wft-geo-db.p.rapidapi.com')

    # this sets up an HTTP Request
    headers = {
        'X-RapidAPI-Key': str(os.getenv('GEO_DATA_KEY')),  # gets the rapid API key from the .env file
        'X-RapidAPI-Host': 'wft-geo-db.p.rapidapi.com',
    }

    try:
        # this makes the actual request.
        conn.request("GET", endpoint, headers=headers)
    except Exception as e:
        app_log = logging.getLogger("errors")
        app_log.error(e, exc_info=True)
    # this gets the response data
    res = conn.getresponse()
    # this reads the response data and returns it as a python object

    data = res.read()

    return data.decode("utf-8")


def main():
    """This is the main function that is run"""
    # this loads the info from the .env file
    load_dotenv()
    setup_logs()
    data = geo_api_request()
    response_logger = logging.getLogger("api_response")
    response_logger.info(data)
    # a Python object (dict):
    python_dictionary = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    # JSON String
    json_string = '{"name":"John", "age":30, "city":"New York"}'

    # convert json to python dictionary using json.loads:
    json_string_to_python_dictionary = json.loads(json_string)

    # python dictionary to json string text
    dictionary_to_json = json.dumps(python_dictionary)
    response_logger.info(json_string_to_python_dictionary)
    response_logger.info("above is the json string to python and below is dictionary to json")
    response_logger.info(dictionary_to_json)
    pass


def setup_logs():
    # set the name of the apps log folder to logs
    logdir = Config.LOG_DIR
    # make a directory if it doesn't exist
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    # this loads the log configuration
    logging.config.dictConfig(LOGGING_CONFIG)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'just_message': {
            'format': '%(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file.handler.errors': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'errors.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
        'file.handler.api_response': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'just_message',
            'filename': os.path.join(Config.LOG_DIR, 'api_response.json'),
            'encoding': 'utf-8',
            'maxBytes': 10000000,
            'backupCount': 5,
        },
        'file.handler.default_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': os.path.join(Config.LOG_DIR, 'root_logger_default.log'),
            'maxBytes': 10000000,
            'encoding': 'utf-8',
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.default_file'],
            'level': 'DEBUG',
            'propagate': False
        },
        'api_response': {
            'handlers': ['file.handler.api_response'],
            'level': 'INFO',
            'propagate': False
        },
        'errors': {  # if __name__ == '__main__'
            'handlers': ['default', 'file.handler.errors'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

if __name__ == '__main__':
    """This causes the app to run"""
    main()
