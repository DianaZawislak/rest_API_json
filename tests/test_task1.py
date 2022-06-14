"""Task 1"""
import json
import logging

import app


def test_task1(sleep, setup_logs, load_env):
    # pylint: unused-import, disable=unused-argument, comparison-with-itself, singleton-comparison
    """Testing API Response"""

    response_logger = logging.getLogger("api_response")
    endpoint = "/v1/geo/cities"
    response = app.geo_api_request(endpoint)
    python_object = json.loads(response)
    response_logger.info(python_object)

    cities = python_object['data']
    response_logger.info(cities)

    assert len(cities) > 0

    assert True
