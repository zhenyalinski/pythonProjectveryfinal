"""This perticular test - tests for homepage"""

import logging
import pytest

def test_auth_pages_register_login(client):
    """This makes the index page"""
    response = client.get("/dashboard")

    log = logging.getLogger("upload")
    log.info("test_auth_pages register + login")

    response = client.get("/register")
    assert response.status_code == 200
    response = client.get("/login")
    assert response.status_code == 200


def test_request_auth_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")

    log = logging.getLogger("upload")
    log.info("equest main menu link in auth pages")

    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data
