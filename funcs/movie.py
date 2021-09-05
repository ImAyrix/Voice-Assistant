from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def movie(keyword):
    PATH = 'C:\Program Files (x86)/chromedriver.exe'

    driver = webdriver.Chrome(PATH)

    driver.get('https://www.movie-map.com/')

    search = driver.find_element_by_id('f')
    search.send_keys(keyword)
    search.send_keys(Keys.RETURN)

    movie_lst = list()

    try:
        main = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'gnodMap'))
        )
        movies = main.find_elements_by_css_selector('a.S')
        for name in movies:
            name_movie = name.text
            movie_lst.append(name_movie)
        return movie_lst
    finally:
        driver.quit()