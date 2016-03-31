import logging
from flask import url_for
from flask import redirect
from db import db_create
from db import db_write


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename='system.log')


def validate_login(username, password):
    logging.debug('validate login' + username + password)
    return True


def log_the_user_in(username):
    logging.debug('log the user in')
    return redirect(url_for('index'))


def handle_message(name, email, message):
    logging.debug(name + " " + email + " " + message)
    return True
