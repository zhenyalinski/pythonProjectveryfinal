"""This test the homepage"""
import logging


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/transactions/upload"' in response.data
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Account Management System" in response.data

def test_request_dashboard_simple(client):
    """This makes the index page"""
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Transactions" in response.data

def test_request_register(client):
    """This makes the index page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"register" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

def test_request_login(client):
    """This makes the index page"""
    response = client.get("/login")
    assert response.status_code == 200
    assert b"login" in response.data

    """This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

# def test_request_bank_statements(client):
#     """This makes the index page"""
#     response = client.get("/transactions")
#
#     log = logging.getLogger("upload")
#     log.info("inside simple_pages_test + test_request_bank_statements")
#
#     assert response.status_code == 200
#     assert b"transactions" in response.data





