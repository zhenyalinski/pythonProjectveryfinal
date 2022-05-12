"""This tests user functionality"""

import logging
import socket

from app import db
from app.db.models import User, Transactions
from app import create_app

def test_login_for_user(client, application):
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    log = logging.getLogger("upload")
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    lm = "hostname logging as well as IP_address: " + host_name + " /  " + host_ip
    log.info(lm)

    data = {
        'email': "zv3@test.edu'",
        'password': "12345678"
    }
    response = client.post('/login', follow_redirects=True, data=data)
    log.info("user test + test login: ")
    # log.info(response.status_code)
    assert response.status_code == 200
    # assert used to verify response


def test_registration(client,application):
    """ user registration test here """
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    log = logging.getLogger("upload")
    log.info("response on user test and test_registration: ")
    data = {
        'email': "zv3@test.edu'",
        'password': "12345678"
    }
    response = client.post('/register', follow_redirects=True, data=data)
    #log.info(response.status_code)
    #log.info(response.data)
    assert response.status_code == 200

def test_dashboard_user(client,application):
    """ Testing out user login - user case"""
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    log = logging.getLogger("upload")
    log.info("testing dash with user  ")
    data = {
        'email': "dash@test.com'",
        'password': "dash"
    }

def test_transaction_uploads(client,application):
    """ Transaction Uploads """
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    log = logging.getLogger("upload")
    log.info("testing bank transaction uploads ")
    data = {
        'email': "teststest@upload.com'",
        'password': "12345678"
    }
    response = client.post('/transactions/upload', follow_redirects=True, data=data)
    #log.info(response.status_code)
    #log.info(response.data)
    assert response.status_code == 200
