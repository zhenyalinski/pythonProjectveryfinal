"""This test the homepage"""

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
    assert b"Index" in response.data

def test_request_upload_transactions(client):
    """This makes the index page"""
    response = client.get("/transactions/upload")
    assert response.status_code == 200
    assert b"accounts/transactions/upload" in response.data

def test_request_register(client):
    """This makes the index page"""
    response = client.get("/register")
    assert response.status_code == 200
    assert b"register" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404

    def test_request_register(client):
        """This makes the index page"""
        response = client.get("/register")
        assert response.status_code == 200
        assert b"register" in response.data
