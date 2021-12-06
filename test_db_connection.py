import pytest


def test_connection_to_db(driver, get_connection_to_db):
    driver.get()

