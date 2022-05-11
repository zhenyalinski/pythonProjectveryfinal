"""This tests user functionality"""

import logging
import socket


from app import db
from app.db.models import
from app import create_app

def test_login_for_user(client, application):
    application.app_context()
    application.config['WTF_CSRF_ENABLED'] = False
    log = logging.getLogger("myapp")
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