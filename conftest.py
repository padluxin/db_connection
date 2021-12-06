import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymssql


@pytest.fixture
def driver():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    yield _driver
    _driver.quit()


@pytest.fixture
def get_connection_to_db(server, user, password, database):
    _conn = pymssql.connect(
        server=server,
        user=user,
        password=password,
        database=database
    )
    return _conn
