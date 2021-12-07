from selenium.webdriver.common.by import By


def test_connection_to_db(driver, get_conn, data):
    driver.get(data['url'])
    driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(data['search_keyword'])
    driver.find_element(By.ID, 'nav-search-submit-button').click()
    titles = [i.text for i in driver.find_elements(By.XPATH,
                                                   '//div[@class="a-section"]//span[@class="a-size-medium a-color-base a-text-normal"]')
              if data['search_keyword'].lower() in i.text.lower()]
    result = parsing_prices(driver, titles)
    cursor = get_conn.cursor()
    cursor.execute(data['SQL']['create_table'])
    get_conn.commit()
    cursor.execute(data['SQL']['insert_data'])
    get_conn.commit()


def parsing_prices(driver, titles):
    result = {}
    for i in titles:
        try:
            result.update({i: driver.find_element(By.XPATH,
                                                  f'//span[contains(text(), "{i}")]/../../../following-sibling::div//span[@class ="a-price"]/span[1]').get_attribute(
                'innerHTML')})
        except Exception:
            continue
    return result
