import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pymssql
import json
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument('--headless')
    _driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
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
    cursor = _conn.cursor()
    cursor.execute(data['SQL']['drop_table'])
    _conn.commit()
    yield _conn
    _conn.close()


@pytest.fixture
def data():
    with open("data.json", 'r') as f:
        return json.load(f)
