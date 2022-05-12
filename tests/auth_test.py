"""This perticular test - tests for homepage"""

import logging
import pytest



def test_request_auth_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")

    log = logging.getLogger("upload")
    log.info("inside auth_test / test request main menu link")

    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
