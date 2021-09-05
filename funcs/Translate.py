import time
from selenium import webdriver


def translate(keyword):
    PATH = 'C:\Program Files (x86)/chromedriver.exe'

    driver = webdriver.Chrome(PATH)

    driver.get('https://www.google.com/search?q=%D8%AA%D8%B1%D8%AC%D9%85%D9%87&oq=%D8%AA%D8%B1%D8%AC%D9%85%D9%87&aqs=chrome..69i57j0i512l9.1474j0j15&sourceid=chrome&ie=UTF-8')

    search = driver.find_element_by_id('tw-source-text-ta')
    search.send_keys(keyword)
    try:
        time.sleep(1)
        translated = (driver.find_element_by_id('tw-target-text')).text
        if translated == 'Translation':
            return 'False, Try again'
        else:
            return translated
    finally:
        driver.quit()