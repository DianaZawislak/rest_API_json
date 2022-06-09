"""These tests should not be changed because they are your examples that hopefully work """
import json
import logging
import app


def test_api_response_geo(sleep, setup_logs, load_env):
    """Testing API Response"""
    # pylint: disable=unused-argument, comparison-with-itself, singleton-comparison

    response_logger = logging.getLogger("api_response")
    endpoint = "/v1/geo/cities"
    response = app.geo_api_request(endpoint)
    python_object = json.loads(response)
    response_logger.info(python_object)

    cities = python_object['data']
    response_logger.info(cities)

    assert len(cities) > 0
