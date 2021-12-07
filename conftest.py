import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymssql
import json


@pytest.fixture
def driver():
    _driver = webdriver.Chrome(ChromeDriverManager().install())
    yield _driver
    _driver.quit()


@pytest.fixture
def get_conn(data):
    _conn = pymssql.connect(
        server=data['db_connection']['server'],
        user=data['db_connection']['user'],
        password=data['db_connection']['password'],
        database=data['db_connection']['database']
    )
    return _conn


@pytest.fixture
def data():
    with open("data.json", 'r') as f:
        return json.load(f)
