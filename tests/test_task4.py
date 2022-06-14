
"""Task 4"""

import json
import logging
import app

def test_task4():
    """Signup for another API and write your own test to verify the data you receive"""
    # pylint: disable=unused-argument, comparison-with-itself, singleton-comparison

    response_logger = logging.getLogger("currency_api_response")
    endpoint ="/currency/convert?format=json&from=AUD&to=CAD&amount=1"

    response = app.currency_api_request(endpoint)
    python_object = json.loads(response)
    response_logger.info(python_object)

    currency = python_object
    response_logger.info(currency)

    assert len(currency) > 0
