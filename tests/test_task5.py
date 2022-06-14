"""Task 5"""

import json
import logging
import app


def test_task5():
    """Signup for another API and write your own test to verify the data you receive"""
    # pylint: disable=unused-argument, comparison-with-itself, singleton-comparison

    response_logger = logging.getLogger("netflix_api_response")
    endpoint = "/search/titles?order_by=date&type=movie"

    response = app.netflix_api_request(endpoint)
    python_object = json.loads(response)
    response_logger.info(python_object)

    movies = python_object
    response_logger.info(movies)

    assert len(movies) > 0
